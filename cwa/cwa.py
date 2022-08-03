# # -*- coding: utf-8 -*-

import csv
from datetime import date
import os

import cv2 as cv
import pandas as pd


class CremmawikiImageAnonymizer:
    def anonymize(self):
        """Will draw a dark rectangle on the top of the image and return the image as an cv.im object"""
        height, width = self.img.shape[:2]
        img_with_rect = cv.rectangle(img=self.img, 
                                    pt1=(0, int(height*0.042)), 
                                    pt2=(width, int(height*0.231)), 
                                    color=(10,10,20), 
                                    thickness=cv.FILLED)
        img_with_rect_and_text = cv.putText(img=img_with_rect,
                                    text="anonymized",
                                    org=(int(width*0.1), int(height*0.12)),
                                    fontFace=cv.FONT_HERSHEY_TRIPLEX,
                                    fontScale=3,
                                    color=(0,255, 255),
                                    thickness=3) 
        return img_with_rect_and_text
    
    def anonymize_and_save(self):
        """Will draw a dark rectangle on the top of the image and save it in a new file"""
        cv.imwrite(self.path_out, self.anonymize())

    def _make_path_out(self):
        bits = os.path.basename(self.path_in).split(".")
        bits.insert(-1, "out")
        filename = ".".join(bits)
        return os.path.join(os.path.dirname(self.path_in), filename)

    def _load_image(self):
        return cv.imread(self.path_in)

    def __init__(self, path_in):
        self.path_in = path_in
        self.path_out = self._make_path_out()
        self.img = self._load_image()
    

class MetadataInSafeExposure: #MI6()
    def _load_conv_table(self) -> dict:
        """Load a csv to build a dictionnary of equivalence between writers' names and id."""
        if os.path.exists(self.path_to_conv_table):
            with open(self.path_to_conv_table, "r", encoding="utf8") as csvfile:
                reader = csv.reader(csvfile)
                conv_table = {row[0]:row[1] for row in reader if len(row) > 0}
        else:
            conv_table = None
            print(f""""{self.path_to_conv_table}" does not exist. Please provide a correct path to the writer id conversion table.""")
        return conv_table
    
    def _save_conv_table(self, conv_table:dict):
        """Save dictionnary of equivalence between writers' names and ids as a csv file."""
        try:
            with open(self.path_to_conv_table, "w", newline='', encoding="utf8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([[k,v] for k, v in conv_table.items()])
        except Exception as e:
            print("Error while saving the conversion table.")
            print(e)
        
    def generate_initial_conv_table(self, names:list):
        """Create a new csv file containing secret ids to replace writers' names."""
        name_table = {name: "" for name in set(names)}
        for n, writer in enumerate(name_table.keys()):
            n = "0"* (4 - len(str(n + 1))) + str(n + 1)
            name_table[writer] = f"AW{n}"
        self._save_conv_table(conv_table=name_table)

    def update_conv_table(self, names:list):
        name_table = self._load_conv_table()
        # if there are names not already included in the conversion table, proceed
        new_names = set(names).difference([name for name in name_table.keys()])
        if len(new_names) > 0:
            print(f"{len(new_names)} names will be added.")
            for n, name in enumerate(new_names):
                n = n + 1 + len(name_table.keys())
                n = "0" * (4 - len(str(n))) + str(n)
                name_table[name] = f"AW{n}"
            self._save_conv_table(name_table)
        else:
            print("The new names provided are already in the conversion table.")

    def anonymize_metadata(self):
        if not isinstance(self.metadata, type(pd.DataFrame())):
            print("Error. The metadata must take the form of a DataFrame.")
            return False
        else:
            conv_table = self._load_conv_table()
            match = False
            for elem in self.metadata["writer_name"]:
                if elem.startswith("AW00"):
                    match = True
                    break
            if match:
                print("It looks like at least part of the dataframe was already anonymized.")
            else:
                self.metadata["writer_name"] = self.metadata["writer_name"].replace(conv_table.keys(), conv_table.values())

    def is_anonymized(self):
        match = 0
        for elem in self.metadata["writer_name"]:
            if not elem.startswith("AW0"):
                match += 1
        if match == 0:
            return True
        else:
            print(f"It looks like some cells ({match}) were not anonymized.")
            return False

    def __init__(self, path_to_conversion_table, path_to_metadata) -> None:
        self.path_to_conv_table = path_to_conversion_table
        self.metadata = None
        if os.path.exists(path_to_metadata):
            self.metadata = pd.read_csv(path_to_metadata)
        else:
            print(f"There is no file at {path_to_metadata}.")
        if self.metadata is not None:
            self.metadata = self.metadata.fillna("N/A") #fill empty cells with N/A

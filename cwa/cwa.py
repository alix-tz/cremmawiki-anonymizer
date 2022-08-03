# # -*- coding: utf-8 -*-

import cv2 as cv

import os 


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
    
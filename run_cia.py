# # -*- coding: utf-8 -*-

import os
import sys

from cwa.cwa import CremmawikiImageAnonymizer as CIA

from CONST import IMG_EXT, EX_PATH_TO_DATA

# indicate the correct path to your data!
path_to_data = ""

# default path is ./data/
if len(path_to_data) == 0:
    path_to_data = EX_PATH_TO_DATA

# load images and apply transformations
for file in os.listdir(path_to_data):
    if file.lower().split(".")[-1] in IMG_EXT:
        if not ".out" in file:
            image = CIA(os.path.join(path_to_data, file))
            if image.img is None:
                sys.exit(f"Could not read the image at: {image.path_in}")
            image.anonymize_and_save()



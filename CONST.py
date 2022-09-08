# # -*- coding: utf-8 -*-
 
import os

# for Cremmawiki Image anonymization
EX_PATH_TO_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data") 
EX_IMG_EXTENSIONS = ["png", "jpeg", "jpg", "tif", "jp2", "gif"]

# for Cremmawiki Metadata anonymization
EX_PATH_TO_CONVERSION_TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_secret", "conversion_table.csv")
EX_PATH_TO_METADATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_secret", "metadata.csv")
EX_PATH_TO_NEW_METADATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_secret", "public_metadata.csv")

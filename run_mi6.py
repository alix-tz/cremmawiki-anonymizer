# # -*- coding: utf-8 -*-

import os
import sys

from cwa.cwa import MetadataInSafeExposure as MI6

from CONST import EX_PATH_TO_CONVERSION_TABLE, EX_PATH_TO_METADATA, EX_PATH_TO_NEW_METADATA

# change these values!
path_to_conversion_table = ""
path_to_metadata = ""
path_to_new_metadata = ""

if len(path_to_conversion_table) == 0:
    path_to_conversion_table = EX_PATH_TO_CONVERSION_TABLE
if len(path_to_metadata) == 0:
    path_to_metadata = EX_PATH_TO_METADATA
if len(path_to_new_metadata) == 0:
    path_to_new_metadata = EX_PATH_TO_NEW_METADATA

# create MI6
new_metadata = MI6(path_to_conversion_table, path_to_metadata)

# create/update list of ids in conversion table and apply to the metadata
# save the result in a new CSV file

names = new_metadata.metadata.get("writer_name", [])
if len(names) > 0:
    if not os.path.exists(path_to_conversion_table):
        new_metadata.generate_initial_conv_table(names)
    else:
        new_metadata.update_conv_table(names)

    new_metadata.anonymize_metadata()

    if new_metadata.is_anonymized():
        new_metadata.metadata.to_csv(path_to_new_metadata)
else:
    print("Error. Are you sure the metadata file your pointed at is correct? It should contain a column named 'writer_name'.")

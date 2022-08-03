# CREMMAWIKI_Anonymizer (CWA)

CWA is an anonymizer for the [CREMMAWIKI corpus](https://github.com/HTR-United/cremma-wikipedia).

## Set up

Create a virtual environment and use PiPy to install the dependencies (ex: `pip install -r requirements.txt`)

## Run

`run_cia.py` and `run_mi6.py` show examples of how to use the CWA module, repectively for CremmawikiImageAnonymizer (CIA) and MetadataInSafeExposure (MI6). 

You can clone this repository, replace the images in data with yours, set up an environment and execute `run_cia.py`.

If you want to change the path the source images, you can also change the value of:
- `path_to_data` in `run_cia.py`
- or `path_to_conversion_table`, `path_to_metadata` and/or `path_to_new_metadata` in `run_mi6.py`

The new files (image or csv) will be created within the source folder. They will be named such as `my_source_img.png` becomes `my_source_img.out.png`, or `my_source.csv` becomes `public_my_source.csv`. Which means that CWA will not overwrite your original images, except for the name conversion table (in MI6). 

## CIA example

| source | output |
| :----: | :----: |
| ![image](https://user-images.githubusercontent.com/33317799/161180583-74f908ad-6f29-45b2-b121-4c1bbd36291a.png) | ![image](https://user-images.githubusercontent.com/33317799/161180643-cf4e70b8-026b-4e7c-9797-1ac07ac13497.png) |

## MI6 example

### Before

- `metadata.csv` (secret):

| col1 | col2 | writer_name | col3 |
| :--: | :--: | :---------: | :--: |
| bla  | bli  | James Bond  | blo  |
| blu  | bly  | Q           | ble  |

### After

- `public_metadata.csv`:

| col1 | col2 | writer_name | col3 |
| :--: | :--: | :---------: | :--: |
| bla  | bli  | AW0007      | blo  |
| blu  | bly  | AW0001      | ble  |

- `conversion_table.csv` (secret):

```txt
James Bond,AW0007
Q,AW0001
```

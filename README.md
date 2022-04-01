# CREMMAWIKI_Anonymizer (CWA)

CWA is an anonymizer for the [CREMMAWIKI corpus](https://github.com/HTR-United/cremma-wikipedia).

## Set up

Create virtual environment and use PiPy to install the dependencies (ex: `pip install -r requirements.txt`)

## Run

`run.py` show you an example of how to use the CWA module. 

You can clone this repository, change the images in data to place yours, setup an environment and execute `run.py`.

If you want to change the path the source image, you can also change the value of `path_to_data` in `run.py`.

The new images will be created within the source folder. They will be named such as `my_source_img.png` becomes `my_source_img.out.png` which means that CWA will not overwrite your original images. 


## Example 

| source | output |
| :----: | :----: |
| ![image](https://user-images.githubusercontent.com/33317799/161180583-74f908ad-6f29-45b2-b121-4c1bbd36291a.png) | ![image](https://user-images.githubusercontent.com/33317799/161180643-cf4e70b8-026b-4e7c-9797-1ac07ac13497.png) |




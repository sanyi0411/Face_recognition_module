# Face_recognition_module
Face recognition module for a school project

This repo contains a project that is part of a bigger, semester project at our university.

It is used to identify people on pictures if a set of pictures is given where it is known who is on the picture.

## Prerequisities

1. Have python 3 installed on your machine
2. Have pip (package manager) installed on your machine (should came with python 3)

## Usage

1. Run the install script only once. This will install all the needed packages via pip 

```
python install.py
```

2. Run the main.py
- It needs 2 arguments:
    - First is the path to the unknown image. This should be a single image.
    - The second is the path to the folder where the known images are
- The program will compare the single, unknown image with all the known images and return the name of the best matching image. Note that it is the best matching not the 100% matching! The result is the full name of the image, so that it is easier later to query, show, send this image.
- The result will be printed onto the console and written into a `result.txt` file, next to the `main.py`. The content of the `result.txt` will be overwritten after every run, so only the latest result in the file.

```
python main.py sample_unknown_images/unknown1.jpg sample_known_images
```
## Testing

Due to the shortage of time, testing was limited to some manual testing. The test images used can be found under `sample_unknown_images` and `sample_known_images`. Even with this you can see that quite nice results were achieved:

![testing](./testing.jpg)
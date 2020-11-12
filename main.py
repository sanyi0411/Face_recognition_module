import sys
import dlib
import face_recognition
import cv2
import numpy as np
import os

def get_image_names(folder):
    image_names = []
    for filename in os.listdir(folder):
        image_names.append(filename)
    return image_names

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            # Convert from BGR to RGB
            rgb_img = img[:, :, ::-1]
            images.append(rgb_img)
    return images

def encode_known_images(images):
    known_encodings = []
    for img in images:
        face_location = face_recognition.face_locations(img)
        face_encoding = face_recognition.face_encodings(img, face_location)[0]
        known_encodings.append(face_encoding)
    return known_encodings

def main():
    # Read the command line arguments
    unknown_face_path = sys.argv[1]
    known_faces_folder_path = sys.argv[2]

    # Load a picture and learn how to recognize it
    unknown_image = face_recognition.load_image_file(unknown_face_path)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Load the known images
    known_images = load_images_from_folder(known_faces_folder_path)
    # Then encode them
    known_images_encodings = encode_known_images(known_images)

    # Comparison to the known encodings
    matches = face_recognition.compare_faces(known_images_encodings, unknown_face_encoding) 
    name = "Unknown"
    face_distances = face_recognition.face_distance(known_images_encodings, unknown_face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = get_image_names(known_faces_folder_path)[best_match_index]

    # Print and write results
    print(name)
    f = open("result.txt", "w")  # "w" will create a file if it doesn't exist and overwrite its content
    f.write(name)

if __name__ == '__main__':
    main()


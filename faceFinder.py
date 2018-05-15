
import os
from PIL import Image, ImageDraw
import face_recognition

class FaceFinder():
    def __init__(self, fp):
        self.img = face_recognition.load_image_file(fp)
        self.encoding = face_recognition.face_encodings(self.img)[0]

    def find_in_dir(self, dirpath):
        for (root, dirs, files) in os.walk(dirpath):
            for file in files:
                filepath = os.path.abspath(os.path.join(root, file))
                img = face_recognition.load_image_file(filepath)
                encodings = face_recognition.face_encodings(img)
                results = face_recognition.compare_faces(encodings, self.encoding, tolerance=0.5)
                print(file, results)
                if True in results:
                    face_locations = face_recognition.face_locations(img)
                    location = face_locations[results.index(True)]
                    self.draw(filepath, location, file)

    def draw(self, filepath, location, filename):
        img = Image.open(filepath)
        draw = ImageDraw.Draw(img)
        location = (location[1], location[0], location[3], location[2])
        draw.rectangle(location, outline='red')
        img.save('./output/' + filename)


# 不能正确区分黄子韬和 杨洋的某张图
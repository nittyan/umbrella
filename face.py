import cv2
from cv2 import CascadeClassifier


def main():
    find_face('face.jpg')

def find_face(img_path):
    classifier = create_classifier()
    origin, grayed = read_and_gray(img_path)
    faces = detect(classifier, grayed)

    for (x, y, w, h) in faces:
        face = origin[y: y + h, x: x + w]
        mozaiced = mozaic(face)
        origin[y: y + h, x: x + w] = mozaiced
        cv2.imwrite(img_path, origin)
        break


def create_classifier():
    return cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def read_and_gray(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, grayed


def detect(classifier, grayed_img):
    return classifier.detectMultiScale(grayed_img, 1.1, 5)


def mozaic(img):
    cut = img.shape[:2][:: -1]
    shrinked = cv2.resize(img, (int(cut[0]/ 5), int(cut[0] / 5)))
    exp = cv2.resize(shrinked, cut, interpolation=cv2.INTER_NEAREST)
    return exp


if __name__ == '__main__':
    main()

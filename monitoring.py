import ConfigParser

import RPi.GPIO as GPIO
from time import sleep

from face import find_face_with_mosaic
from camera import Camera
from uploader import Uploader


def main():
    monitor()


def get_bucket_name():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    return config.get('S3', 'bucket_name')
    

def monitor():
    bucket_name = get_bucket_name()
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)

    cam = Camera(2, 0.7)

    while True:
        if GPIO.input(18):
            print("monitor!!!")
            paths = cam.capture()
            find_faces(paths)
            upload(bucket_name, paths)
        sleep(1)

        
def find_faces(paths):
    for path in paths:
        find_face_with_mosaic(path)
        

def upload(bucket_name, paths):
    uploader = Uploader(bucket_name)
    for path in paths:
        uploader.upload(path, path)
        print('%s uploaded' % path)
        


if __name__ == '__main__':
    main()

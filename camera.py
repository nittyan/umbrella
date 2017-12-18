import datetime
import os
import time

import picamera


class Camera(object):

    def __init__(self, num, delay):
        self._num = num
        self._delay = delay
        self._camera = picamera.PiCamera()

    def capture(self):
        dir_path = 'img/' + self._get_now_string()
        self._make_dir(dir_path)
        return self._sequential_shooting(dir_path)

    def _get_now_string(self):
        now = datetime.datetime.now()
        l = [now.year, now.month, now.day, now.hour, now.minute, now.second]
        l = map(str, l)
        return '-'.join(l)
    
    def _make_dir(self, path):
        os.mkdir(path)

    def _sequential_shooting(self, dir_path):
        paths = []

        for n in xrange(self._num):
            path = dir_path + '/{}.jpg'.format(str(n))
            paths.append(path)
            self._capture(path)
            time.sleep(self._delay)

        return paths

    def _capture(self, path, size=(640, 360)):
        self._camera.capture(path, resize=size)
        print('capture %s' % path)

        
def main():
    camera = Camera(2, 0.5)
    camera.capture()
        

if __name__ == '__main__':
    main()

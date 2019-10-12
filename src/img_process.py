import cv2

class ImageProcess(object):
    path = None
    
    def __init__(self, path):
        self.path = path
        self.img_height = None
        self.img_weight = None
        self.img_original = None
        self.img_array = None

        self.read_image()

    def read_image(self):
        self.img_original = cv2.imread(self.path)
        self.img_array = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
        self.img_height = self.img_array.shape[0]
        self.img_weight = self.img_array.shape[1]

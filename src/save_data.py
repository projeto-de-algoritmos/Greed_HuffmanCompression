import cv2
import collections
import json
import os
from matplotlib import pyplot as plt

class SaveData(object):
    def __init__(self, directory, gray_image, hist, codes):
        self.directory = directory

        self.create_directory()
        self.save_gray_image(gray_image)
        self.save_hist(hist)
        self.save_codes(codes)
        self.save_compressed_image(gray_image, codes)
        self.save_uncompressed_image(gray_image)
    
    def create_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def save_gray_image(self, image):
        cv2.imwrite(self.directory + 'gray_scale.png',image)
    
    def save_hist(self, hist):
        plt.plot(hist)
        plt.title('Histograma da Imagem em Escala de Cinza')
        plt.xlabel('Escala de cinza')
        plt.ylabel('Quantidade')
        plt.xlim([0, 256])
        plt.savefig(self.directory + 'histogram.png')

    def save_codes(self, codes):
        od = collections.OrderedDict(sorted(codes.items()))
        with open(self.directory + 'codes.json', 'w+') as f:
            json.dump(od, f, indent=4)
    
    def save_compressed_image(self, img_array, codes):
        with open(self.directory + 'img_compressed.txt', 'wb') as f:
            for row in img_array:
                for value in row:
                    f.write(codes[value].encode())
    
    def save_uncompressed_image(self, img_array):
        with open(self.directory + 'img_uncompressed.txt', 'wb') as f:
            for row in img_array:
                for value in row:
                    my_s = '{:08b}'.format(value)
                    f.write(my_s.encode())

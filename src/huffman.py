import cv2
from heapq import heapify, heappop, heappush
from node import Node

class Huffman(object):

    def __init__(self, img_array):
        self.tree = None
        self.codes = {}
        self.rev_codes = {}
        self.hist = None
        self.img_array = img_array
        self.img_compressed = ''

        self.compute_histogram()
        self.generate_huffman_tree()
        self.generate_huffman_codes('',self.tree)


    def compute_histogram(self):
        self.hist = cv2.calcHist([self.img_array], [0], None, [256], [0, 256])

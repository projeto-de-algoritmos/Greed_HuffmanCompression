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

    def generate_huffman_tree(self):
        nodes = []
        for i, frequency in enumerate(self.hist):
            if int(frequency) != 0:
                node = Node(i, int(frequency))
                nodes.append(node)
        heapify(nodes)
        while len(nodes) > 1:
            first = heappop(nodes)
            second = heappop(nodes)
            new_node = Node(None, first.frequency+second.frequency)
            new_node.set_children(first, second)
            heappush(nodes, new_node)
        
        self.tree = nodes[0]
    
    def generate_huffman_codes(self, code, node):
        if node == None:
            return
        if node.color != None:
            if not code:
                self.codes[node.color] = '0'
                self.rev_codes['0'] = node.color
            else:
                self.codes[node.color] = code
                self.rev_codes[code] = node.color
        else:
            self.generate_huffman_codes(code+'0', node.left_node)
            self.generate_huffman_codes(code+'1', node.right_node)

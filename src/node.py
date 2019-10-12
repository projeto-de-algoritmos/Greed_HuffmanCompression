class Node(object):
    def __init__(self, color, frequency):
        self.left_node = None
        self.right_node = None
        self.color = color
        self.frequency = frequency
    
    def set_children(self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node

    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

#nosetests test.py

class Node(object):
    def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right

def visit(node):
    yield node
    if node.left:
        for elem in visit(node.left):
            yield elem
    if node.right:
        for elem in visit(node.right):
            yield elem

def has_cycles(node):
    def verify_cycles(node, stack={}):
        id_node = '{}'.format(id(node))
        if id_node in stack:
            return True
        stack[id_node] = 1
        if node.left:
            if verify_cycles(node.left, stack):
                return True
        if node.right:
            if verify_cycles(node.right, stack):
                return True
        del stack[id_node]
        return False
    return verify_cycles(node)

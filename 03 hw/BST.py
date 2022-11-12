class BST:

    def __init__(self):
        d1 = {
            'parent': 'root',
            'data': 'root',
            'l_child': None,
            'r_child': None
        }
        data = []
        data.append(d1)

    def Insert(self, element, parent=0):
        if self.data[0]['data'] == 'root':
            self.data[0]['data'] == element
        else:
            if element > self.data[0]['data']:
                if self.data[0]['r_child'] is None:
                    d1 = {
                        'parent': 0,
                        'data': element,
                        'l_child': None,
                        'r_child': None}
                else:



if __name__ == "__main__":
    bTree = BST()
    bTree.Insert(5)
    bTree.Insert(6)

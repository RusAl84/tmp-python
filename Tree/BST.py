class BST:

    def __init__(self):
        d1 = {
            'parent': 'root',
            'data': 'root',
            'l_child': None,
            'r_child': None
        }
        self.data = []
        self.data.append(d1)

    def Insert(self, element, parent=0):
        print(self.data[parent]['data'])
        if self.data[parent]['data'] == 'root':
            self.data[parent]['data'] = element
        else:  # не первый элемент
            if element > self.data[parent]['data']:
                if self.data[parent]['r_child'] is None:
                    size = len(self.data)
                    d1 = {
                        'parent': parent,
                        'data': element,
                        'l_child': None,
                        'r_child': size}
                    self.data.append(d1)
                else:
                    self.Insert(element, parent)
            else:
                if self.data[parent]['l_child'] is None:
                    size = len(self.data)
                    d1 = {
                        'parent': parent,
                        'data': element,
                        'l_child': size,
                        'r_child': None}
                    self.data.append(d1)
                else:
                    self.Insert(element, parent)
if __name__ == "__main__":
    bTree = BST()
    bTree.Insert(5,0)
    bTree.Insert(6)
    bTree.Insert(7)
    bTree.Insert(8)

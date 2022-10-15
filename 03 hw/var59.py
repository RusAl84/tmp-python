class BST:
    def __init__(self):
        self.data = {}
        self.l_child = None
        self.r_child = None

    def binary_insert(self, root, val):
        if len(self.data) == 0:
            self.data[0] = val
        else:
            index = 1
            l = self.data[index]
            # if val > self.data[0]:

        #     if val in self.data:
        #         l = self.data[val]
        #
        #     else:
        #         self.data[val]


r = BST(5)

print(r)

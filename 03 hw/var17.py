# https://medium.com/analytics-vidhya/a-brief-introduction-to-binary-search-tree-bst-in-python-2da1813abd7e#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImVlMWI5Zjg4Y2ZlMzE1MWRkZDI4NGE2MWJmOGNlY2Y2NTliMTMwY2YiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NjU4MTYxMDIsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExNjg5MzAxMzU1NTY4MzQwODE2OCIsImVtYWlsIjoicnVzYWtvdmFtODRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF6cCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsIm5hbWUiOiLQkNC70LXQutGB0LXQuSDQoNGD0YHQsNC60L7QsiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BTG01d3UzVXgyaG96TDNLZ0hOb1ZLX183a09RUDJURlg3bkVHOV93YXZvRWdnPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6ItCQ0LvQtdC60YHQtdC5IiwiZmFtaWx5X25hbWUiOiLQoNGD0YHQsNC60L7QsiIsImlhdCI6MTY2NTgxNjQwMiwiZXhwIjoxNjY1ODIwMDAyLCJqdGkiOiI3Yjc3NTEzOWQ3NzIzOGQ3OTY4ZDEwMTI4NzQ2MzA0ZWRmYjQ0NGUxIn0.VqjdK7w2g8tJ3rI2re008Hi9uSZ3f4Xw-GZElqHhoGxxyq0RA3sap9fITVNJtaCNraCrZYTGptrYK7KM_fkVkE3nHVFFvDuLFXhQaNo0tVPXfKXnbyU7cK3IC5U0r08K76cHSjfS9B4eXGLMJnsrtU-is44HvjmhVqMdEw7h46AeDsPLoKdFnZOkKddWdcFQVhbxNimsVolLJTGilSQGkl-emUqA4Ei28OYkb5AKnHRvaMn4bWkhPk01yMs_1kNxSsDnIOdEd93MdL4BTt85VJbGsBXR7fsdCYbs4mEbbGmlfLAZGQH9hGJZpETDmVWcmrIOxX57aGX_qLB_GlJKFw

# Дерево двоичного поиска
# А– прямой, В – симметричный
# Левый сын, правый брат (таблица, массив)	А=A ⋃обрB

class BST:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.root = None
        self.data = val

    def binary_insert(self, root, node):
        if self.root is None:
            self.root = node
        else:
            if self.root.data > node.data:
                if root.l_child is None:
                    root.l_child = node
                else:
                    self.binary_insert(root.l_child, node)
            else:
                if root.r_child is None:
                    root.r_child = node
                else:
                    self.binary_insert(root.r_child, node)

    def in_order_print(self, root):
        if not root:
            return
        self.in_order_print(root.l_child)
        print(root.data)
        self.in_order_print(root.r_child)

    # def pre_order_print(self, root):
    #     if not root:
    #         return
    #     print(root.data)
    #     pre_order_print(root.l_child)
    #     pre_order_print(root.r_child)

    def edge_list(self, root):
        elist= []
        if not root:
            return
        e = self.edge_list(root.l_child)
        if e is not None:
            for item in e:
                if len(item)>0:
                    elist.append(item)
        print(root.data)
        edge=[]
        if root.l_child is not None:
            edge = (root.data, root.l_child.data)
        elist.append(edge)
        if root.r_child is not None:
            edge = (root.data, root.r_child.data)
        elist.append(edge)
        e = self.edge_list(root.r_child)
        if e is not None:
            for item in e:
                if len(item) > 0:
                    elist.append(item)
        return elist

    def draw(self):
        # G = nx.Graph()
        elist = self.edge_list(self.root)
        # for item in elist:
        print(elist)



r = BST("root")
r.binary_insert(r.root, BST(3))
r.binary_insert(r.root, BST(7))
r.binary_insert(r.root, BST(1))
r.binary_insert(r.root, BST(5))
r.binary_insert(r.root, BST(9))
#    3
#  /   \
# 1     7
#        \
#         9
#        /
#       5

# print(r.edge_list(r.root))
r.draw()

# r = BST("ROOT")
# for i in range(10):
#     import random
#     r.binary_insert(r.root, BST(random.randint(2, 20)))

# print("in order:")
# r.in_order_print(r.root)
#
# print("pre order")
# pre_order_print(r)

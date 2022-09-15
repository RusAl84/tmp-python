from StackPtr import StackPtr


class AdapterStackPtr:

    def __init__(self):
        self.st = StackPtr()

    def getSize(self):
        return self.st.getSize()

    def isEmpty(self):
        return self.st.getSize() == 0

    def peek(self):
        return self.st.peek()

    def push(self, value):
        self.st.push(value)

    def pop(self):
        self.st.pop()

    def display(self):
        self.st.display()

    def getElement(self, ind):
        size = self.st.getSize()
        element = -1
        # 1 4
        # 2 3
        # 3 2
        # 4 1
        # 5 0  size-ind
        # print(f"{ind}  {size-ind}")
        ind = size - ind - 1
        if ind >= 0 and ind < size:
            st1 = StackPtr()
            for item in range(ind + 1):
                st1.push(self.peek())
                element = self.peek()
                self.pop()
            for item in range(ind + 1):
                self.push(st1.peek())
                st1.pop()
        return element

    def setElement(self, ind, element):
        size = self.st.getSize()
        ind = size - ind - 1
        if ind >= 0 and ind < size:
            st1 = StackPtr()
            for item in range(ind):
                st1.push(self.peek())
                self.pop()
            st1.push(element)
            self.pop()
            for item in range(ind + 1):
                self.push(st1.peek())
                st1.pop()

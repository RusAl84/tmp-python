# https://www.geeksforgeeks.org/dsa/implement-a-stack-using-singly-linked-list/

# Node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Stack implementation using linked list


class myStack:
    def __init__(self):
        # initially stack is empty
        self.top = None
        self.count = 0

    # push operation
    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp

        self.count += 1

    # pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return -1
        temp = self.top
        self.top = self.top.next
        val = temp.data

        self.count -= 1
        return val

    # peek operation
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return -1
        return self.top.data

    # check if stack is empty
    def isEmpty(self):
        return self.top is None

    # size of stack
    def size(self):
        return self.count


if __name__ == "__main__":
    st = myStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())

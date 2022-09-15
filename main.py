from StackPtr import StackPtr

def example_work_stackPtr():
    st = StackPtr()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    size = st.getSize()
    print(f"size of stack: {size}")
    st.display()
    st.push(9)
    st.pop()
    st.pop()
    st.display()

def example_work_AdapterStackPtr():
    st = StackPtr()

if __name__ == '__main__':
    example_work_stackPtr()

from StackPtr import StackPtr
from AdapterStackPtr import AdapterStackPtr


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
    ast = AdapterStackPtr()
    size = ast.getSize()
    print(f"size of stack: {size}")
    ast.push(1)
    ast.push(2)
    ast.push(3)
    ast.push(4)
    ast.push(5)
    ast.display()
    size = ast.getSize()
    print(f"size of stack: {size}")
    print(f"element: {ast.getElement(0)}")
    print(f"element: {ast.getElement(1)}")
    print(f"element: {ast.getElement(2)}")
    print(f"element: {ast.getElement(3)}")
    print(f"element: {ast.getElement(4)}")
    print(f"element: {ast.getElement(5)}")
    print(f"element: {ast.getElement(-1)}")
    ast.display()
    ast.setElement(0, 9)
    ast.setElement(4, 7)
    ast.setElement(5, 7)
    print("example setElement")
    ast.display()


def swap(A, i, j):
    # temp = A[i]
    # A[j] = temp
    # A[i] = A[j]
    temp = A.getElement(i)
    A.setElement(i, A.getElement(j))
    A.setElement(j, temp)

# Раздел # с использованием схемы разделов Lomuto
def partition(a, start, end):
    # Выберите крайний правый элемент в качестве опорного элемента из списка.
    # pivot = a[end]
    pivot = a.getElement(end)

    # Элементы #, меньшие, чем точка поворота, будут перемещены влево от `pIndex`
    # Элементы # больше, чем точка поворота, будут перемещены вправо от `pIndex`
    # равные элементы могут идти в любом направлении
    pIndex = start

    # каждый раз, когда мы находим элемент, меньший или равный опорному,
    # `pIndex` увеличивается, и этот элемент будет помещен
    # перед разворотом.
    for i in range(start, end):
        # if a[i] <= pivot:
        if a.getElement(i) <= pivot:
            # swap(a, i, pIndex)
            temp = a.getElement(i)
            a.setElement(i, a.getElement(pIndex))
            a.setElement(pIndex, temp)
            pIndex = pIndex + 1

    # поменять `pIndex` на пивот
    # swap(a, end, pIndex)
    temp = a.getElement(end)
    a.setElement(end, a.getElement(pIndex))
    a.setElement(pIndex, temp)

    # возвращает `pIndex` (индекс опорного элемента)
    return pIndex


# Процедура быстрой сортировки
def quicksort(a, start, end):
    # базовое состояние
    if start >= end:
        return

    # переставить элементы по оси
    pivot = partition(a, start, end)

    # повторяется в подсписке, содержащем меньше элементов, чем основной
    quicksort(a, start, pivot - 1)

    # повторяется в подсписке, содержащем больше элементов, чем основной
    quicksort(a, pivot + 1, end)


def example_work_QuickSort():
    ast = AdapterStackPtr()
    size = ast.getSize()
    print(f"size of stack: {size}")
    ast.push(5)
    ast.push(4)
    ast.push(3)
    ast.push(2)
    ast.push(5)
    ast.display()
    print("sorted: ")
    size = ast.getSize()
    quicksort(ast, 0, size - 1)
    ast.display()


if __name__ == '__main__':
    # example_work_stackPtr()
    # example_work_AdapterStackPtr()
    example_work_QuickSort()

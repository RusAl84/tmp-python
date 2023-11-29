import random

def bubbleSort(arr):
    n = len(arr)
    nop=0
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False;  nop += 1 #1

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            nop += 1 #1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]; nop += 2 #2
                swapped = True; nop += 1 #1
        nop += 1 #1
        if (swapped == False):
            break
    return nop

def genData(n):
    numbers=[]
    for i   in range(n):
        numbers.append(random.randrange(10000))
    return numbers

def printArr(arr):
    for i in range(len(arr)):
        print(f"{arr[i]} ")

# Driver code to test above
if __name__ == "__main__":

    presets = [500, 1000, 3000, 5000, 8000, 10000, 20000, 30000]
    for preset in presets:
        arr = genData(preset)
        nop  = bubbleSort(arr)
        print(f"N={preset} nop={nop}")
    # printArr(arr)
    # bubbleSort(arr)
    # print("\nSorted array:")
    # printArr(arr)
    


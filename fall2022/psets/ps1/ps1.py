from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

# 914 606 2697 -- Nick DeSanctis

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    # if n > 0:
        # raise ValueError()
    return reverse(digits)

def new_universe(univsize):
    universe = []
    for i in range(univsize):
        universe.append([])
    return universe

def deBucket(universe):
    tmp = []
    for lst in universe:
        for elt in lst:
            tmp.append(elt)
    return tmp


def newCountSort(base, arr, place):
    universe = new_universe(base)
    for elt in arr:
        universe[elt[0][place]].append(elt)
    sortedArr = deBucket(universe)

    return sortedArr

def reverse(arr):
    ptr1 = 0
    ptr2 = len(arr)-1
    while(ptr1 < ptr2):
        tmp = arr[ptr1]
        arr[ptr1] = arr[ptr2]
        arr[ptr2] = tmp
        ptr1 += 1
        ptr2 -= 1
    return arr

def castBack(super_list):
    tmp = []
    for elt in super_list:
        tmp.append(elt[0], elt[1])
    return tmp
        
def radixSort(univsize, base, arr):
    k = math.ceil(math.log(univsize,base))
    n = len(arr)
    super_list = []
    for i in range(n):
        super_list.append([arr[i][0], arr[i][1], BC(arr[i][0],base,k)])
    for j in range(k):
        for i in range(n):
            super_list[i][0] = super_list[i][2]
        super_list = newCountSort(base, super_list, k-j-1)
    result = []
    for i in range(n):
        tmp2 = 0
        for j in range(k):
            tmp2 += super_list[i][0][j] * (base ** (k-j-1))
        result.append([tmp2,super_list[i][1]])
    return(result)
        


def create_arr (n, U):
    array = []
    for i in range(n):
        array.append([random.randint(0, U), "item"])
    return array


def plt_graph():
    merge_win = []
    count_win = []
    radix_win = []
    
    for i in range(1,16):
        n = 2**i
        for j in range(1,20):
            U =  2**j
            arr = create_arr(n, U)
            print(arr)
            start1 = time()
            mergeSort(arr)
            end1 = time()
            merge_time = end1 - start1
            
            start2 = time()
            countSort(U+1, arr)
            stop2 = time()
            count_time = stop2 - start2

            start3 = time()
            radixSort(U,n,arr)
            stop3 = time()
            radix_time = stop3 - start3
            

            best_time = min(merge_time, count_time, radix_time)
            if best_time == merge_time:
                merge_win.append((i, j))
            elif best_time == count_time:
                count_win.append((i, j))
            else:
                radix_win.append((i,j))
        

    df1 = pd.DataFrame(merge_win, columns=['x','y'])
    df2 = pd.DataFrame(count_win, columns=['x','y'])
    df3 = pd.DataFrame(radix_win, columns=['x','y'])

    ax = df1.plot.scatter(x="y", y="x", color="Red", label ="merge sort")
    df2.plot.scatter(x="y", y="x", color="Green", label="count sort", ax=ax)
    df3.plot.scatter(x="y", y="x", color="Blue", label="radix sort", ax=ax)
    plt.ylabel("log n")
    plt.xlabel("log U")
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.show()


#if __name__ == "__main__":
    # plt_graph()

tmp1 = [819,123]
arr = [[819,3],[123,1], [131, 9],[571,2],[591,8]]
arr = [[2, 'item'], [16, 'item'], [25, 'item'], [26, 'item'], [5, 'item'], [30, 'item'], [12, 'item'], [32, 'item'], [3, 'item'], [10, 'item'], [8, 'item'], [7, 'item'], [7, 'item'], [16, 'item'], [6, 'item'], [11, 'item'], [21, 'item'], [12, 'item'], [3, 'item'], [12, 'item'], [9, 'item'], [17, 'item'], [11, 'item'], [0, 'item'], [19, 'item'], [22, 'item'], [24, 'item'], [5, 'item'], [31, 'item'], [10, 'item'], [15, 'item'], [2, 'item']]
def main():
    
    print(countSort(1000, arr))
    print(mergeSort(arr))
    print(radixSort(1000,10,arr))
    plt_graph()
    

main()


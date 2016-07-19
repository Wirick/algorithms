from math import *
import numpy
import array


def fib(n):
    """Returns the Nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    past1, past2, newFib = 0, 1, None
    for i in range(n - 1):
        newFib = past1 + past2
        past1, past2 = past2, newFib
    return newFib

def binary_search(sortd, n, x):
    """Given SORTED integer array of length N, together with an
    integer X, returns a positive integer i so that Sorted[i-1] = X
    and -1 otherwise."""
    halfway, start_index, end_index, end = math.floor(n/2), 0, n - 1, False
    while end_index > start_index and not end:
        if end_index - start_index == 1:
            end = True
        if sortd[halfway] < x:
            start_index = halfway
            halfway += math.ceil((end_index - start_index)/2)
        elif sortd[halfway] > x:
            end_index = halfway
            halfway -= math.ceil((end_index - start_index)/2)
        else:
            return int(halfway) + 1
    return -1
    
def insertion_sort(arr, x):
    """Given an ARR of integers with order a positive integer X <= 10^3, returns
    the sorted arr and the number of swaps performed by the algorithm."""
    count = 0
    for n in range(x-1):
        for m in range(n+1):
            if arr[n - m + 1] < arr[n - m]:
                arr[n - m + 1], arr[n - m] = arr[n - m], arr[n - m + 1]
                count += 1
    return arr, count

def merge_sort(arr, x):
    """Performs a merge sort on a given ARRay of order X and returns the
    sorted array."""
    ms = merge_sort
    half = int(floor(float(x/2)))
    if x == 1:
        return arr
    else:
        arr1 = ms(arr[:half], half)  
        arr2 = ms(arr[half:], x - half)
        size2 = x - half
        size1 = half
        x, y = merge(arr1, arr2, size1, size2)
        return x

def has_additive_inverse(arr, end):
    """Given an ARRay of length END, searches the array and returns
    the (indexed from 1) indicies in (a, b) format of two elements such
    that ARR[a] = -ARR[b], and -1 if such indicies do not exist"""
    key, count = {}, 0
    for x in range(end):
        count += 1
        if arr[x] in key:
            return (key[arr[x]] + 1, x + 1), count
        else:
            key[-arr[x]] = x
    return -1, count

def merge(first, second, size1, size2):
    """Given sorted arrays FIRST and SECOND of SIZE1, SIZE2, respectively,
    returns the array representing the merge of FIRST and SECOND, along
    with its size."""
    size = size1 + size2
    first_place, second_place = 0, 0
    merged = []
    while size1 + size2 - first_place - second_place > 0:
        if size1 - first_place == 0:
            merged.append(second[second_place])
            second_place += 1
            continue
        if size2 - second_place == 0:
            merged.append(first[first_place])
            first_place += 1
            continue
        val1, val2 = first[first_place], second[second_place]
        if val1 <= val2:
            merged.append(val1)
            first_place += 1
        else:
            merged.append(val2)
            second_place += 1
    return numpy.asarray(merged), size

def get_majority_element(arr, n):
    """single value occupies more than half the indicies of ARR."""
    val = float(n/2)
    vals = defaultdict(int)
    for i in range(n):
        vals[arr[i]] += 1
    for value in vals:
        if vals[value] > val:
            return value
    return -1
    

class Sorter:
    """A sorter object using
    a certain ALGORITHM"""

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.number_of_actions = None

    def sort_from_file(self, fl):
        f = open(fl)
        contents = [lines.rstrip() for lines in f]
        f.close()
        self.size = int(contents[0])
        cont = [int(x) for x in contents[1].split(" ")]
        self.arr = numpy.asarray(cont)
        self.arr, self.number_of_actions  = self.algorithm(self.arr, self.size)
        print "Efficiency: " + str(self.number_of_actions)
        g = open("generalSoln.txt", "w")
        g.write(self.arr)
        print "Wrote to generalSoln.txt"
        g.close()

    def set_array(self, lst):
        self.arr = numpy.asarray(lst)
        self.sorted = False

    def get_sorted(self):
        if self.sorted:
            return self.arr
        else:
            self.sort(self.size)
            return self.arr

    def sort(self):
        self.arr, self.number_of_actions  = self.algorithm(self.arr, self.size)
        print "Efficiency: " + str(self.number_of_actions)


def split(f):
    """Returns a list containing the stripped lines 
    of a graph in edge list format file F."""
    lines = [line.rstrip() for line in f]
    a, b = lines[0].split(" ")
    a, b = int(a), int(b)
    return a, b, lines[1:]
        
    

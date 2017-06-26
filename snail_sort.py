"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements
to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest;
      the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE: The 0x0 (empty matrix) is represented as [[]]
"""

def snail(array):
    """
    return the sorted array
    """
    pass

def main():
    """
    testing
    """
    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    tmp = [x for x in array[0]]
    tmp2 = [x[-1] for x in array[1:]]
    for val in tmp2:
        tmp.append(val)
    tmp3 = [x for x in array[-1][-2::-1]]
    for val in tmp3:
        tmp.append(val)
    tmp4 = [x[0] for x in array[-2:0:-1]]
    for val in tmp4:
        tmp.append(val)
    print(tmp)

if __name__ == '__main__':
    main()

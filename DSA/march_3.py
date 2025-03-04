def multiplication_table(rows: int, cols: int):
    res = [[0 for i in range(rows)] for j in range(cols)]
    return res

def merge_sorted_lists(list1, list2):
    i = j = 0
    res = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    
    res.extend(list2[j:])
    res.extend(list1[i:])

    return res

def sum_diagonals(matrix):
    n = len(matrix)
    if n == 0: return 0

    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n-1-i]

    # Subtract the middle intersect number
    if n % 2 == 0:
        total -= matrix[i//2][i//2]

def first_occurrence(array, target):
    return array.index(target)

def find_missing_number(array):
    x = array[0]
    for num in array[1:]:
        x += 1
        if x != num:
            return x
    return -1

def running_sum(array):
    prev_sum = array[0]
    for index in range(1,len(array)):
        array[index] += prev_sum
        prev_sum = array[index]
    return array

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0,1]
        while len(sequence) < n:
            next_item = sequence[-1] + sequence[-2]
            sequence.append(next_item)
    return sequence[-1]

def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])

    res, n, i = [], len(intervals), 1
    start, end = intervals[0]
    while i < n:
        while i < n and start <= intervals[i][0] < end:
            if end < intervals[i][1]:
                end = intervals[i][1]
            i += 1
        res.append([start,end])
        if i < n:
            start, end = intervals[i]
    return res
    
    




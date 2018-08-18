def swap(list, i, j):
    print('Swap', i, j)
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def quick_sort(list, left, right):
    if left > right:
        return None
    i, j = left, right
    pivot = list[left]
    
    while i < j:
        while i < j and list[j] >= pivot:
            j -= 1
        while i < j and list[i] <= pivot:
            i += 1
        swap(list, i, j)
    swap(list, left, i)
    quick_sort(list, left, i - 1)
    quick_sort(list, i + 1, right)


list = [4, 1, 5, 8, 3, 7, 4, 6, 2]
quick_sort(list, 0, len(list) - 1)
print(list)

# http://developer.51cto.com/art/201403/430986.htm
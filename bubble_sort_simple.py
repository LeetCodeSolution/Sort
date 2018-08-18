def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def swap_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if list[j] < list[i]:
                swap(list, i, j)


list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
swap_sort(list)
print(list)

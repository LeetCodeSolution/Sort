def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def select_sort(list):
    length = len(list)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != 0:
            swap(list, i, min_index)


list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
select_sort(list)
print(list)

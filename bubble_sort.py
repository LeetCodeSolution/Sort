def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(length - 1, i, -1):
            if list[j] < list[j - 1]:
                swap(list, j, j - 1)


list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
bubble_sort(list)
print(list)

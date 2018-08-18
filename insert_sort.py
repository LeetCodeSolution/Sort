def insert_sort(list):
    length = len(list)
    for i in range(1, length):
        if list[i] < list[i - 1]:
            temp = list[i]
            list[i] = list[i - 1]
            j = i - 1
            while temp < list[j - 1] and j > 0:
                list[j] = list[j - 1]
                j -= 1
            list[j] = temp


list = [9, 1, 5, 8, 3, 7, 4, 6, 2]
insert_sort(list)
print(list)

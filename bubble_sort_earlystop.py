def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def bubble_sort(list):
    length = len(list)
    for i in range(length):
        flag = False
        for j in range(length - 1, i, -1):
            if list[j] < list[j - 1]:
                swap(list, j, j - 1)
                flag = True
        if flag == False:
            print('Early Stop')
            break


list = [2, 3, 4, 5, 6, 7, 8, 9, 1]
bubble_sort(list)
print(list)

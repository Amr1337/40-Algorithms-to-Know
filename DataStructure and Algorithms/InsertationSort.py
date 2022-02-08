
def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i-1
        element_next = lst[i]
        while (lst[j] > element_next) and (j>=0):
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = element_next
    return lst

mylist = [25, 21, 22, 24, 23, 27, 26]

print(insertion_sort(mylist))
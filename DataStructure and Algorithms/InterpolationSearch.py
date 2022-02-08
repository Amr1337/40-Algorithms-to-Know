from BubbleSort import bubble_sort

def interpol_search(list, item):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False
    while idx0 <= idxn and list[idx0] <= item <= list[idxn]:
        # Find the mid-point
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) *
                          (item - list[idx0])))

        # Compare the value at mid-point with search value
        if list[mid] == item:
            found = True
            return found
        if list[mid] < item:
            idx0 = mid + 1
    return found


list = [12, 33, 11, 99, 22, 55, 90]
# list needs to be sorted before calling the
sorted_list = bubble_sort(list)
print(interpol_search(sorted_list, 12))
print(interpol_search(sorted_list, 91))

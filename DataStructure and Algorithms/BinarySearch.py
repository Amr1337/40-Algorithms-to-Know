def binary_search(mylist, item):
    first = 0
    last = len(mylist) - 1
    found_flag = False
    while (first <= last) and not found_flag:
        mid = (first + last) // 2
        if mylist[mid] == item:
            found_flag = True
        else:
            if item < mylist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found_flag


mylist = [1, 4, 5, 6, 40, 23, 105]
item = int(input("Enter number: "))
print(binary_search(mylist, item))

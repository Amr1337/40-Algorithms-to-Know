def linear_search(list, item):
    found = False
    index = 0

    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index += 1
    return found


list = [12, 33, 11, 99, 22, 55, 90]
print(linear_search(list, 12))
print(linear_search(list, 91))

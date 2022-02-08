def shell_sort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            # Sort the sub list for this distance
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        # Reduce the distance for the next element
        distance = distance // 2
    return list


list = [26, 17, 20, 11, 23, 13, 18, 24, 14, 12, 22, 16, 15, 19, 25]
print(shell_sort(list))

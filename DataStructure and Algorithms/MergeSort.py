def merge_sort(lst):
    if len(lst)> 1:
        mid = len(lst) // 2  # splits list into half
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left) # repeats until list length is 1
        merge_sort(right)

        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a += 1
            else:
                lst[c] = right[b]
                b+= 1
            c += 1
        while a < len(left):
            lst[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            lst[c] = right[b]
            b += 1
            c += 1
    return lst


mylist = [44, 16, 83, 7, 67, 21, 34, 45, 10]
print(merge_sort(mylist))
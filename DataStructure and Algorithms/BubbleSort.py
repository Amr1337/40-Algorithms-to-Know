#Pass 1 of bubble sort
'''
mylist = [25, 21, 22, 24, 23, 27, 26]
lastElementIndex = len(mylist) - 1
print(0, mylist)
for idx in range (lastElementIndex):
    if mylist[idx] > mylist[idx+1]:
        mylist[idx], mylist[idx+1] = mylist[idx+1], mylist[idx]
    print(idx+1, mylist)
'''
#Complete implementation of bubble sort
def bubble_sort(lst):
    lastelementindex = len(lst)-1
    for passNo in range(lastelementindex, 0, -1):
        for idx in range(passNo):
            if lst[idx]>lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
    return lst
mylist = [25, 21, 22, 24, 23, 27, 26]

print(bubble_sort(mylist))
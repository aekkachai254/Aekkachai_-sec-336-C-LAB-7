arr = [11, 4, 7, 5, 10, 9, 13, 1]
bubble = arr.copy()
# bubble sort
for i in range(len(bubble)):
    for j in range(0, len(bubble)):
        if j+1 < len(bubble):
            if bubble[j] > bubble[j+1]:
                tmp = bubble[j+1]
                bubble[j+1] = bubble[j]
                bubble[j] = tmp
            elif j+1 < len(bubble) :
                j = j+1

# selection
selection = arr.copy()
for i in range(len(selection)):
    mini = 999
    for j in range(i+1, len(selection)):
        if mini > selection[j]:
            keep_index = j
            mini = selection[j]
    if mini < selection[i]:
        tmp = selection[i]
        selection[i] = selection[keep_index]
        selection[keep_index] = tmp

# insertion
insertion = arr.copy()
for i in range(0,len(insertion)):
    if i + 1 < len(insertion):
        if insertion[i] > insertion[i+1]:
            tmp = insertion[i+1]
            insertion[i+1] = insertion[i]
            insertion[i] = tmp
        while insertion[i] < insertion[i-1]:
            if i - 1 >= 0:
                tmp = insertion[i - 1]
                insertion[i - 1] = insertion[i]
                insertion[i] = tmp
            i = i - 1
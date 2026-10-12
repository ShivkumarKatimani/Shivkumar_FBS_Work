def conquer(li, start, mid, stop):
    temp = []
    i = start
    j = mid + 1

    while i <= mid and j <= stop:
        if li[i] < li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1

    while i <= mid:
        temp.append(li[i])
        i += 1

    while j <= stop:
        temp.append(li[j])
        j += 1

    li[start:stop + 1] = temp


def divide(li, start, stop):
    if start < stop:
        mid = (start + stop) // 2

        divide(li, start, mid)
        divide(li, mid + 1, stop)

        conquer(li, start, mid, stop)


li = [11, 3, 44, 2, 21, 18, 1]

print("Unsorted list:", li)

divide(li, 0, len(li) - 1)

print("Sorted list:", li)


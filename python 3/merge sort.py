x = int(input())
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(x)


def mergesort(sort_list):
    if len(sort_list) > 1:

        mid = len(sort_list) // 2
        L = sort_list[:mid]
        R = sort_list[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_list[k] = L[i]
                i += 1
            else:
                sort_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sort_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            sort_list[k] = R[j]
            j += 1
            k += 1


mergesort(arr)
print(arr)

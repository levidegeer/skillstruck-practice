arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
x = int(input())
arr.append(x)


def insertion_sort(sort_list):
    insert_spot = 0
    val_to_insert = 0
    for i in range(1, len(sort_list)):
        val_to_insert = sort_list[i]
        insert_spot = i
        while insert_spot > 0 and sort_list[insert_spot-1] > val_to_insert:
            sort_list[insert_spot] = sort_list[insert_spot - 1]
            insert_spot -= 1
        sort_list[insert_spot] = val_to_insert
    return sort_list


print(insertion_sort(arr))

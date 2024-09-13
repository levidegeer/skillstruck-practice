sort_list = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
sort_list.append(int(input()))

def selection(sort_list):
    for i in range(len(sort_list)):
        smaller_index = i
        for j in range(i+1, len(sort_list)):
            if sort_list[smaller_index] > sort_list[j]:
                smaller_index = j
        if smaller_index != i:
            sort_list[i], sort_list[smaller_index] = sort_list[smaller_index], sort_list[i]
        else:
            pass
    return(sort_list)

print(selection(sort_list))









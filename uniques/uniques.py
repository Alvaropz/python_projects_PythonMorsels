#Python Morsels

def uniques_only(iterable):
    list_of_lists = []
    for first_it in iterable:
        if not first_it in list_of_lists:
            list_of_lists.append(first_it)
    return list_of_lists

print(uniques_only([[1, 2], [3], [1], [3]])) #[[1, 2], [3], [1]]
print(uniques_only([1, 2, 3])) #[1, 2, 3]
print(uniques_only([1, 1, 2, 2, 3])) #[1, 2, 3]
print(uniques_only([1, 2, 3, 1, 2])) #[1, 2, 3]
print(uniques_only([1, 2, 2, 1, 1, 2, 1])) #[1, 2]
nums = (n**2 for n in [1, 2, 3])
print(uniques_only(nums)) #[1, 4, 9]
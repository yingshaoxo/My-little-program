def split_list_to_parts(list_, one_part_num):
    length = len(list_)
    parts_num = length // one_part_num
    list_result = []
    for i in range(1, parts_num+2):
        list_result.append(list_[one_part_num*(i-1):one_part_num*i])
    return list_result

list_ = list(range(1, 21))
print(split_list_to_parts(list_, 3))
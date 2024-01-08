test_list = [5, 6, 3, 8, 2, 1, 7, 1]
sub_list = [1, 7, 1]

def find_sequence(test_list, sub_list):
    for i in range(len(test_list) - len(sub_list) + 1):
        if sub_list == test_list[i:i+len(sub_list)]:
            return True
    return False

print(find_sequence(test_list, sub_list))
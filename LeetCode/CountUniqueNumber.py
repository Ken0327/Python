arr = [2, 1, 3, 1, 2, 2, 3, 1, 1, 1, 2, 3, 3, 0, -1, 0, 2, 2]

# Find unique number count
# Example1:
# input: arr = [1,2,3]
# output: true
# Example2:
# input: arr = [1,2,2,3,3]
# output: false


def function(arr):
    dic = dict()
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic.update({i: 1})
    print(dic)

    unique_list = []
    for i in dic.values():
        if i not in unique_list:
            unique_list.append(i)

    if len(dic) == len(unique_list):
        return True
    else:
        return False


result = function(arr)
print(result)

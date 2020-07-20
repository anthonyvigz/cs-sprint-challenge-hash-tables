def intersection(arrays):
    #input will be 2d array

    num_dict = {}

    for arr in arrays:
        for num in arr:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
    
    result = []

    for num in num_dict:
        if num_dict[num] == len(arrays):
            result.append(num)

    return result

    #result will be an array of numbers


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))

    arrs = [[1,2,3], [1,2,4], [1, 5,6,7]]

    print(intersection(arrs))
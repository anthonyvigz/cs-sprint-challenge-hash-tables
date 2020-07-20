def get_indices_of_item_weights(weights, length, limit):
    #weights is an array of numbers
    #length and limit are numbers
    weight_dict = {}

    for i in range(len(weights)):
        if weights[i] not in weight_dict:
            weight_dict[weights[i]] = [i]
        else:
            weight_dict[weights[i]].append(i)

    result = [-1,-1]
    for weight in weight_dict:
        if (limit-weight) in weight_dict:
            if weight == limit-weight:
                result[0] = weight_dict[weight][0]
                result[1] = weight_dict[limit-weight][1]
            else:
                result[0] = weight_dict[weight][0]
                result[1] = weight_dict[limit-weight][0]

    if -1 not in result:
        result.sort(reverse=True)
        return result

    #output is an array of numbers unless it's empty then it's None
    return None
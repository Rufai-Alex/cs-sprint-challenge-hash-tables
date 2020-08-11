def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    needed_weights = dict()

    # Check: If the input array is less than 2
    if len(weights) < 2:
        return None

    for current_weight_index in range(len(weights)):

        # keep track of the current weight
        current_weight = weights[current_weight_index]

        # if the weight is found, then that means that was inserted previously
        if current_weight in needed_weights:
            # get the index of the weight and add it to the needed_weights
            excisted_weight_index = needed_weights[current_weight]

            # return a tuple
            return (current_weight_index, excisted_weight_index)

        # store info about this current weight
        needed_weights[limit - current_weight] = current_weight_index
    return None

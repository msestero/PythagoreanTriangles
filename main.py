

def dimensional_counting(dimensions, sum_dimensions, starting_val, already_counted={}, first=True):

    # Set key value and check if we have already seen it
    key = (dimensions, sum_dimensions, starting_val)
    if key in already_counted:
        return already_counted[key]
    
    starting_dimensional_vals = [0] * dimensions
    starting_dimensional_vals[0] = starting_val
    dimensional_vals = [starting_dimensional_vals]
    if dimensions == 1 or sum_dimensions == 1:
        if dimensions < 4 and sum_dimensions < 20 and starting_val < 20:
            already_counted[key] = dimensional_vals
        return dimensional_vals

    curr_starting_val = starting_val
    new_dimensions = dimensions - 1
    counts = []

    # while statment is just checking that it is possible to spread the remaining value out 
    # in such a way that the first value is greater or equal to the largest value in the remaining cells
    while curr_starting_val >= (sum_dimensions - curr_starting_val) / new_dimensions:
        starting_val = min(curr_starting_val, sum_dimensions - curr_starting_val)
        new_sum_dimensions = sum_dimensions - curr_starting_val
        new_counts = dimensional_counting(new_dimensions, new_sum_dimensions, starting_val, already_counted, False)
        new_counts = list(map(lambda x: [curr_starting_val] + x, new_counts))
        # if first:
        #     print(curr_starting_val, len(new_counts))
        counts.extend(new_counts)
        curr_starting_val -= 1

    if dimensions < 4 and sum_dimensions < 20 and starting_val < 20:
        already_counted[key] = counts
    return counts
        
    
    
def add_one_all(dims):
    return list(map(lambda x: x + 1, dims))


def check_pythagorean_distance(dim_distances):
    summed_squares = sum(map(lambda x: x * x, dim_distances))
    i = 1
    while i * i < summed_squares:
        i += 1
    return i * i == summed_squares, i

if __name__ == "__main__":
    already_counted = {}
    counts = []
    pythag_found = 0
    sum_counts = 0
    for i in range(120, 130):
        counts = dimensional_counting(8, i, i, already_counted)
        counts = list(map(lambda x: add_one_all(x), counts))
        for count in counts:
            is_pythag, dist = check_pythagorean_distance(count)
            if is_pythag and dist == 45:
                print(count)
                print(dist)
                sum_counts += sum(count)
    print(sum_counts)
    
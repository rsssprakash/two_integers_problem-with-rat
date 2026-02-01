def rat_food(r, unit, arr):
    # If array is empty or None
    if arr is None or len(arr) == 0:
        return -1

    total_food_required = r * unit   # total food needed
    food_collected = 0               # track collected food
    house_count = 0                  # track houses visited

    # Iterate through houses
    for food in arr:
        food_collected += food
        house_count += 1
        if food_collected >= total_food_required:
            return house_count   # return number of houses needed

    # If not enough food even after all houses
    return 0


# Example usage
r = 7
unit = 2
arr = [2, 8, 3, 5, 7, 4, 1, 2]
# to print the output
print(rat_food(r, unit, arr))

#just modification for git pratice
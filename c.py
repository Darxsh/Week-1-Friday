def move_zeroes_to_end(arr):
    # Initialize a variable to track the position of non-zero elements
    position = 0

    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:
            # If the current element is not zero, place it at the 'position' index
            arr[position] = arr[i]
            position += 1
    
    # Fill the remaining positions with zeroes
    while position < len(arr):
        arr[position] = 0
        position += 1

    return arr

# Example usage
array = [1, 2, 0, 4, 3, 0, 5, 0]
result = move_zeroes_to_end(array)
print(f"Output array: {result}")

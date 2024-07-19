def move_zeroes_to_end(arr):
    position = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[position] = arr[i]
            position += 1
    while position < len(arr):
        arr[position] = 0
        position += 1
    return arr

array = [1, 2, 0, 4, 3, 0, 5, 0]
result = move_zeroes_to_end(array)
print(f"Output array: {result}")

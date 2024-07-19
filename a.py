def find_second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements."

  
    largest = second_largest = float('-inf')

   
    for number in arr:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    if second_largest == float('-inf'):
        return "There is no second largest element in the array."

    return second_largest

array = [12, 35, 1, 10, 34, 1]
result = find_second_largest(array)
print(f"The second largest element is {result}.")

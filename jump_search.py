import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))

    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1

# Input the array from the console
input_str = input("Enter the array as space-separated numbers: ")
arr = list(map(int, input_str.split()))

x = int(input("Enter the value to search for: "))

result = jump_search(arr, x)

if result != -1:
    print(f"Element {x} is found at position {result + 1}.")
else:
    print(f"Element {x} is not found.")

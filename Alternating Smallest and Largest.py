def strange_sort(arr):
    arr.sort()
    result = []
    left, right = 0, len(arr) - 1
    
    while left <= right:
        if left != right:
            result.append(arr[left])
            result.append(arr[right])
        else:
            result.append(arr[left])
        left += 1
        right -= 1
    
    return result

# Example usage
numbers = [5, 1, 9, 3, 7, 2]
sorted_numbers = strange_sort(numbers)
print(f"Strange Sorted List: {sorted_numbers}")

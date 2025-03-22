def find_closest_temperatures(temps):
    if len(temps) < 2:
        raise ValueError("At least two temperatures are required")
    
    min_diff = float('inf')
    index_pair = (-1, -1)
    
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            diff = abs(temps[i] - temps[j])
            if diff < min_diff:
                min_diff = diff
                index_pair = (i, j)
    
    return index_pair

# Example usage
temperatures = [32.5, 31.8, 29.4, 30.1, 32.4, 33.0]
closest_indices = find_closest_temperatures(temperatures)
print(f"Indices of closest temperatures: {closest_indices}")

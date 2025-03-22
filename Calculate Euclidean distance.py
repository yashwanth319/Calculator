import math

def euclidean_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensions")
    
    distance = math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
    return distance

# Example usage
pointA = (3, 4)
pointB = (6, 8)

distance = euclidean_distance(pointA, pointB)
print(f"Euclidean Distance: {distance}")

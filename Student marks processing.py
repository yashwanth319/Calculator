def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    if not all(isinstance(mark, (int, float)) for mark in marks):
        raise TypeError("All marks must be numbers.")
    return sum(marks) / len(marks)

def save_marks_to_file(filename, marks):
    try:
        with open(filename, 'w') as file:
            file.write(" ".join(map(str, marks)))
    except IOError:
        print("Error: Unable to write to file.")

def read_marks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(mark) for mark in file.read().split()]
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ValueError:
        print("Error: File contains invalid data.")
        return []

# Example usage
student_marks = [85, 90, 78]
avg = calculate_average(student_marks)
print("Average Marks:", avg)

save_marks_to_file("marks.txt", student_marks)
read_marks = read_marks_from_file("marks.txt")
print("Read Marks:", read_marks)

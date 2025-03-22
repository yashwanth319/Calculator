class UnderageError(Exception):
    """Custom exception for underage users."""
    pass

def verify_age(age):
    if age < 18:
        raise UnderageError("Age verification failed: User is under 18.")
    print("Age verification successful.")

def log_error(error_message):
    try:
        with open("error.log", "a") as file:
            file.write(error_message + "\n")
    except IOError:
        print("Error: Unable to write to log file.")

# Example usage
try:
    verify_age(16)  # This should raise UnderageError
except UnderageError as ue:
    print(f"UnderageError: {ue}")
    log_error(str(ue))

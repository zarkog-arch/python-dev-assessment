def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    # Logical Error: Incorrect average calculation for empty list
    return total / len(numbers)


data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")


# Function with logical error fixed using try-except
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Handles empty lists (ZeroDivisionError) by returning None.
    """
    total = 0
    # Note: Using sum(numbers) is the more Pythonic way, 
    # but the loop structure is maintained here for context.
    for i in range(len(numbers)):
        total += numbers[i]

    # FIX: Use try-except block to handle ZeroDivisionError
    try:
        # This line will raise ZeroDivisionError if len(numbers) is 0
        return total / len(numbers)
    except ZeroDivisionError:
        print("Debugging Challenge: List is empty. Returning None.")
        return None


# Error Handling Challenge Function
def get_list_element(my_list, index):
    """
    Attempts to return an element at a given index. 
    Catches IndexError (out of bounds) and TypeError (non-list input).
    Returns None on error.
    """
    try:
        # Check for list type first. If not a list, raise TypeError 
        # as requested, which will be caught by the second except block.
        if not isinstance(my_list, list):
            raise TypeError("Input 'my_list' must be a list.")
            
        # This operation can raise an IndexError
        return my_list[index]
    
    except IndexError:
        print(f"Error Handling Challenge: Index {index} is out of bounds for the list.")
        return None
    
    except TypeError as e:
        # Catching the custom TypeError raised for non-list input
        print(f"Error Handling Challenge: {e}")
        return None


# --- Debugging Challenge Example Usage (from file with tasks) ---

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This now gracefully returns None

print("\n--- calculate_average Examples ---")
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}") # Handled gracefully

# --- Error Handling Challenge Example Usage ---

test_list = ['a', 'b', 'c', 'd']
test_tuple = (1, 2, 3)

print("\n--- get_list_element Examples ---")

# 1. Valid input
print(f"Element at index 2 (Valid): {get_list_element(test_list, 2)}")

# 2. Out-of-bounds input (IndexError)
print(f"Element at index 10 (Out of bounds): {get_list_element(test_list, 10)}")

# 3. Incorrect type input (TypeError)
print(f"Element from tuple (Incorrect type): {get_list_element(test_tuple, 0)}")

# 4. Another valid input
print(f"Element at index 0 (Valid): {get_list_element(test_list, 0)}")


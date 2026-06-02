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

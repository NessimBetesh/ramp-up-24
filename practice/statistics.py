def statistics(numbers):
    sumNumbers = sum(numbers)
    minNumber = min(numbers)
    maxNumber = max(numbers)

    #calc average
    if len(numbers) > 0:
        average = sumNumbers / len(numbers)
    else:
        average = None
    
    return sumNumbers, minNumber, maxNumber, average

input_numbers = input("Enter a list of numbers separated by spaces:\n")
numbers = list(map(int, input_numbers.split()))

sumNumbers, minNumber, maxNumber, average = statistics(numbers)

print(f"Sum: {sumNumbers}")
print(f"Minimum: {minNumber}")
print(f"Maximum: {maxNumber}")
print(f"Average: {average}")
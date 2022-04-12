numbers = [1, 100]

for num in range(numbers):
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

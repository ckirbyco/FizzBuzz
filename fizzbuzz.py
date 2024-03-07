# Fizzbuzz code
# Branch step-three: Cleaning up the code

# Iterating through the numbers 1-100
for x in range(1, 101):

    # Multiples of both three and five print the word “FizzBuzz”.
    if x%3 == 0 and x%5 == 0:
        print("Fizzbuzz")

    # Multiples of three print “Fizz”.
    elif x%3 == 0:
        print("Fizz")

    # Multiples of five print “Buzz”.
    elif x%5 == 0:
        print("Buzz")

    # Else condition for when previous conditions aren't met.
    else:
        print(x)


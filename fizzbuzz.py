# Fizzbuzz code

# "Write a program that prints the numbers from 1 to 100.
# iterate through the number 1-100 
for x in range(101):
    #print(x)
    # For numbers which are multiples of both three and five print “FizzBuzz”.
    if x%3 == 0 and x%5 == 0:
        print("Fizzbuzz")
    # But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")




import sys

try: # checking entries for errors
    entry = int(sys.argv[1])
except(IndexError,ValueError):
    entry = input("Please enter a number: ")
    while True: #looping to check valid entries
        try:
            entry = int(entry)
            break
        except ValueError:
            entry = input("Entry a valid number: ")
print("User supplied number:", entry)
print("Fizz buzz is counting to:", entry)

def fizzbuzz(n): # function for the game
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
           print("Fizz")
        elif x % 5 == 0:
           print("Buzz")
        else:
            print(x)
print(fizzbuzz(int(entry)))
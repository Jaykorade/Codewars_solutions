#1 ; python work by Jayesh Korade
# # Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

n = [1,2,3,4,5,6,7,8,9,0]
create_phone_number(n)
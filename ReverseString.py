def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# function to test with
print(reverse_string("Nike Air Yeezy"))

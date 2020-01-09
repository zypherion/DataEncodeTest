from random import randint

def encode():
    seed = 0
    data = 0
    output = ""
    
    seed = int(input("Please enter a seed number (and make a note of it): "))
    data = input("Enter the data you'd like to encode: ")
    formatted = list(data)
    print(formatted)

    for char in formatted:
        chr(char)
        print (char)
    for char in formatted:
        output += char

    print(output)
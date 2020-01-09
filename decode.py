def decode():
    seed = 0
    data = 0
    
    seed = input("Please enter your seed number: ")
    data = input("Enter the data you'd like to decode: ")
    formatted = list(data)
    
    answer = str(formatted/seed)
    print ("Decoded data follows below: \n")
    print ("%s" % answer)
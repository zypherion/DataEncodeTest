def prompt():
    global prompt
    prompt = 0
    while prompt == 0:
        prompt = input("Are you (e)ncoding or (d)ecoding?: ")
        if prompt == "e":
            print("encoding!")
            rotor1 = input("Please set rotor 1: ")
            rotor2 = input("Please set rotor 2: ")
            rotor3 = input("Please set rotor 3: ")
        elif prompt == "d":
            print("decoding!")
        else:
            print("Sorry, please enter 'e' for encoding or 'd' for decoding.")
            prompt = 0
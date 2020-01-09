def process():
    global process
    process = 0
    while process == 0:
        process = input("Are you (e)ncoding or (d)coding?: ")
        if process == "e":
            print("encoding!")
        elif process == "d":
            print("decoding!")
        else:
            print("Sorry, please enter 'e' for encoding or 'd' for decoding.")
            process = 0
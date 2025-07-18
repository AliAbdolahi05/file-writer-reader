# Open file in read/write mode, create if not exists
my_text = open("mytext.txt", "a+")
my_text.seek(0)

while True:
    inp = input("Enter command (R=Read, W=Write, E=Exit): ").strip().upper()

    if inp == "R":
        my_text.seek(0)
        print("---- File Content ----")
        print(my_text.read())
        print("----------------------")

    elif inp == "W":
        print("Enter your text. Type 'E' on a new line to stop writing.")
        while True:
            W_inp = input("> ")
            if W_inp.strip().upper() == "E":
                print("Returning to main menu.")
                break
            else:
                my_text.write(W_inp + "\n")
                my_text.flush()
        my_text.seek(0)

    elif inp == "E":
        print("Okay, exiting...")
        break

    else:
        print("WHAT???__ ^_^", "Error404")

my_text.close()

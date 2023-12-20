print("Credit to TiComputer on Github!")
print("Options to say are 'I am not telling you' 'Bob' or your actual name ")

Question1 = str(input("Hi, I am a NPC, what is your name?"))

if Question1 == "I am not telling you":
    print("Options are 'My name is weird' or 'I don't know why I am doing this")
    Question2 = input(str("Why are you not telling me your name?"))

    if Question2 == "My name is weird":
        print("Okay, that's fine.")
        print("-- MY NAME IS WEIRD ENDING --")
    elif Question2 == "I don't know why I am doing this":
        print("Okay, next time think more.")
        print("-- THINK MORE ENDING --")
elif Question1 == "Bob":
    print("Bob is very common to be a name.")
    print("-- THE MOST COMMON NAME EVER IS BOB ENDING --")
else:
    print(f"Hello, {Question1}!")

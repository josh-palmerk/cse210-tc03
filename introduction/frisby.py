def frisby_intro():
    import random
    number = random.randint(0, 5)
    greetings = ["Hello there!", "Welcome to the jungle!", "This is a normal introduction", "Why hello there, didn't expect you to be here", "Hola! Como Esta! I don't know Spanish!", "Hello, this is a function that was called by a file named somthing."]

    print(f"\033[1;31;40m {greetings[number]}")

frisby_intro()
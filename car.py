command = ""
start = False

while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        if not start:
            print("Car started, ready to go,")
            start = True
        else:
            print("Car already started")
    elif command.lower() == "stop":
        if start:
            print("Car stopped")
            start = False
        else:
            print("car already stopped")
    elif command.lower() == "help":
        print(
            """
              start - to start the car
              stop - to stop the car
              help - to get help
              quit - to quit
              """
        )
    elif command.lower() == "quit":
        print("Thank you")
    else:
        print("I dont understand that")

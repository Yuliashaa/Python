print("Welcome to text adventure 'Adventure Time'")
print("Greetings from Jake the dog and Finn the human")
print("Lumpy Space Princess is in trouble")
print("As it comes.......")
print("Marceline Abadeer had stolen Lumpy Space Princess")
print("ᕙ〳 ರ ︿ ರೃ 〵ᕗ")
print("   ")
print("Save the princess")
room = 1
print("Choose way by printing one of the words in capitals")
while room > 0:
    if room == 1:
        print("Finn and Jake are sitting in their house")
        print("Choose the way by printing: 'Left', 'Right' or 'Straight'")
        direction = input()
        while direction != "Left" and direction != "Right" and direction != "Straight":
            direction = input()
        if direction == "Left":
            print("You are in the Cave. Princess must be here")
            room = 2
        elif direction == "Right":
            print("You meet Flame Princess. She is eating apple. She is waving to you:)")
            print("You didn`t save Lumpy Space Princess")
            room = 1
        elif direction == "Straight":
            print("You fall from the hill")
            print("Jake save you. You are in the tree house")
            room = 1
    elif room == 2:
        print("You entered the Cave. It is dark here.")
        print("Choose the way by printing: 'Fire', 'Dark' or 'Lighter'")
        direction = input()
        while direction != "Fire" and direction != "Dark" and direction != "Lighter":
            direction = input()
        if direction == "Fire":
            print("Ooooopppsss")
            print("There was bats in the Cave. They are very angry and hungry.")
            room = 1
        elif direction == "Dark":
            print("It is dark and cold here. You hurt your leg.")
            print("You are in the tree house. Jake gave you cacao")
            room = 1
        elif direction == "Lighter":
            print("It scares you. But you need to save Lumpy Space Princess")
            room = 3
    elif room == 3:
        print("There are 3 ways.")
        print("Choose your own way")
        print("Choose the way by printing: 'Left', 'Straight' or 'Right'")
        direction = input()
        while direction != "Left" and direction != "Right" and direction != "Straight":
            direction = input()
        if direction == "Left":
            print("It was a bridge here. But now it is rined.")
            print("Choose other way.")
            room = 3
        elif direction == "Straight":
            print("You find a door. But it was closed.")
            print("You need to find a key if you want to open it.")
            print("But Finn think that it`s not a good idea.")
            room = 3
        elif direction == "Right":
            print("You were going too long.")
            print("Jake was hungry")
            print("You find a 'Snikers'in your pocket")
            print("If you want to give it to Jake print 'Give', but if you don`t want to give it to Jake - print 'Not'")
            Jake = input()
            while Jake != "Give" and Jake != "Not":
                Jake = input()
            if Jake == "Give":
                print("Jake is so happy.")
                print("You ate 'Snikers' with Finn and Jake")
                Jake = True
            elif Jake == "Not":
                print("You ate 'Snikers' alone.")
                print("Jake becomes sad.")
                Jake = False
            print("You find a strange hall.")
            print("Jake said it a maze.")
            if Jake == True:
                print("Jake helped you to find exit from the maze.")
                room = 4
            elif Jake == False:
                print("Jake is still sad.")
                print("He don`t want to help you to find exit.")
                print("Find it!")
                print("Save Lumpy Space Princess")

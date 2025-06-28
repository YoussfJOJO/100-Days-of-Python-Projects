goal = "____"
word = "word"
guess = ""
idx=0
a =list(goal)
def at_goal():
    if goal == "word":
        print("Congrats, you have succeeded!\n")

    else:
        print("you are not there yet\n")

def replace():
    global goal
    a[idx] = guess
    goal = str("".join(a))



while not at_goal():
    print("""  /$$$$$$                                               /$$$$$$$$ /$$                       /$$      /$$                           /$$
 /$$__  $$                                             |__  $$__/| $$                      | $$  /$ | $$                          | $$
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$ /$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$/$$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$$$_  $$$$| $$  \ $$| $$  \__/| $$  | $$
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$$/ \  $$$| $$  | $$| $$      | $$  | $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$/   \  $$|  $$$$$$/| $$      |  $$$$$$$
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/     \__/ \______/ |__/       \_______/
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      """)
    idx=0
    print("word to guess: "+goal+"\n")
    guess = input("Guess a letter: ")
    for letter in word:
        if letter == guess:
            idx = word.index(guess)
            replace()
            print(goal)
    if goal == "word":
        at_goal()
        break
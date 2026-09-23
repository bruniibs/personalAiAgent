
print("Cognitive Assistant System starting...")

# CAS asks for your name => how she should adress you. When the name is received she will exclude any empty space, if the name is empty it'll use Miss instead.
name = input("What is your name? ").strip()
if not name:
    name = "Miss"
print(f"Hello, {name}!\nHow could I assist you today?")

while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! Have a great day!")
        break
    print(f"You said: '{user_input}'")
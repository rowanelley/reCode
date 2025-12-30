import os

# Startup process
os.system("clear")
print(r"""
                      /$$$$$$                  /$$          
                     /$$__  $$                | $$          
  /$$$$$$   /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$ 
 /$$__  $$ /$$__  $$| $$       /$$__  $$ /$$__  $$ /$$__  $$
| $$  \__/| $$$$$$$$| $$      | $$  \ $$| $$  | $$| $$$$$$$$
| $$      | $$_____/| $$    $$| $$  | $$| $$  | $$| $$_____/
| $$      |  $$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/       \_______/ \______/  \______/ \_______/ \_______/
""")
print("Copyright (c) 2025 Rowan Elley — Licensed under the MIT License")
print()
print("Enter Ciphertext:")
ciphertext = input()
os.system("clear")

# Parse ciphertext
ciphertext = ciphertext.upper()
plaintext = ciphertext
print(plaintext)
print()

mappings = {}

def addMapping(mappings):
    target = input("ADD MODE: What are we changing? ")
    change = input("ADD MODE: What to? ")

    mappings[target.upper()] = change.lower()

def applyMappings(plaintext, mappings):
    for target, change in mappings.items():
        temporaryPlaintext = ""

        for ch in plaintext:
            if ch == target:
                temporaryPlaintext += change
            else:
                temporaryPlaintext += ch

        # apply this mapping result for the next pass
        plaintext = temporaryPlaintext

    os.system("clear")
    print(plaintext)
    print()
    for target, change in mappings.items():
        print(target+" --> "+change)
    print()

while True:
    command = input("What do you want to do? (A)dd, (R)emove, (Q)uit: ")
    if command.lower() == "a":
        addMapping(mappings)
        applyMappings(plaintext, mappings)
        continue
    elif command.lower() == "r":
        mappings.popitem()
        applyMappings(plaintext, mappings)
        continue
    elif command.lower() == "q":
        break
    else:
        print("Unknown command.....")
        continue
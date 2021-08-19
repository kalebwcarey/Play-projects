# below are the lists that serve as the enigma rotors. These "rotors" do not replicate historical rotor patterns but
# do replicate the function of actual rotors. Switches determine at which change that the next rotor steps.

rotor1 = [12, 2, 16, 11, 14, 24, 10, 7, 15, 8, 22, 17, 9, 23, 5, 1, 19, 3, 25, 21, 18, 13, 20, 0, 6, 4]
switch1 = 17
rotor2 = [1, 13, 20, 18, 2, 17, 3, 12, 22, 19, 21, 10, 16, 6, 5, 11, 4, 25, 23, 14, 8, 0, 15, 7, 24, 9]
switch2 = 6
rotor3 = [7, 24, 16, 25, 10, 2, 22, 11, 4, 9, 6, 0, 5, 15, 8, 20, 14, 1, 13, 3, 19, 17, 23, 12, 18, 21]
switch3 = 25
rotor4 = [18, 23, 6, 11, 19, 3, 25, 12, 24, 4, 0, 21, 8, 15, 20, 17, 14, 13, 22, 1, 7, 9, 16, 10, 2, 5]
switch4 = 14
rotor5 = [11, 21, 23, 14, 1, 12, 22, 8, 25, 10, 7, 16, 6, 24, 4, 19, 13, 5, 3, 2, 9, 18, 17, 20, 15, 0]
switch5 = 16
rotor6 = [12, 3, 6, 1, 21, 14, 18, 0, 7, 4, 11, 2, 8, 22, 5, 15, 20, 23, 9, 10, 19, 17, 16, 13, 25, 24]
switch6 = 9

# below are the dictionaries that serve as the reflectors. The reflectors are dictionaries with identical but
# inverted pairs because the reflectors
reflector1 = {10: 12, 7: 2, 6: 18, 1: 19, 0: 13, 22: 15, 17: 8, 5: 20, 11: 24, 25: 23, 21: 4, 14: 9, 16: 3, 3: 16,
              9: 14, 4: 21, 23: 25, 24: 11, 20: 5, 8: 17, 15: 22, 13: 0, 19: 1, 18: 6, 2: 7, 12: 10}
reflector2 = {22: 20, 20: 22, 4: 23, 23: 4, 3: 0, 0: 3, 25: 10, 10: 25, 14: 12, 12: 14, 18: 21, 21: 18, 13: 24,
              24: 13, 6: 16, 16: 6, 11: 8, 8: 11, 1: 19, 19: 1, 2: 5, 5: 2, 17: 7, 7: 17, 9: 15, 15: 9}
reflector3 = {1: 8, 8: 1, 13: 3, 3: 13, 4: 6, 6: 4, 14: 23, 23: 14, 22: 7, 7: 22, 11: 24, 24: 11, 17: 19, 19: 17,
              10: 15, 15: 10, 2: 16, 16: 2, 0: 21, 21: 0, 12: 5, 5: 12, 9: 20, 20: 9, 25: 18, 18: 25}


def rotor_select(x):
    global rotor
    if x == 1:
        rotor = rotor1
    elif x == 2:
        rotor = rotor2
    elif x == 3:
        rotor = rotor3
    elif x == 4:
        rotor = rotor4
    elif x == 5:
        rotor = rotor5
    elif x == 6:
        rotor = rotor6
    return


def switch_select(x):
    global switch
    if x == 1:
        switch = switch1
    elif x == 2:
        switch = switch2
    elif x == 3:
        switch = switch3
    elif x == 4:
        switch = switch4
    elif x == 5:
        switch = switch5
    elif x == 6:
        switch = switch6
    return


def reflector_select(x):
    global reflector
    if x == 1:
        reflector = reflector1
    elif x == 2:
        reflector = reflector2
    elif x == 3:
        reflector = reflector3
    return


def rotor_action(which_rotor, n, text):
    global acted_text
    rotor_select(which_rotor)
    shift = text + n
    if shift >= 26:
        shift -= 26
    acted_text = rotor[shift]
    return


def rotor_action_reverse(which_rotor, n, text):
    global acted_text
    rotor_select(which_rotor)
    acted_text = rotor.index(text)
    acted_text = acted_text - n
    if acted_text <= -1:
        acted_text += 26

    return


def reflector_action(which_reflector, n, text):
    global acted_text
    shift = text + n
    if shift >= 26:
        shift -= 26
    acted_text = which_reflector[shift]
    acted_text -= n
    if acted_text <= -1:
        acted_text += 26
    return


def strip(to_be):
    to_be = to_be.replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(";", "")
    to_be = to_be.replace(":", "").replace("\"", "").replace("\'", "").replace("/", "").replace("-", "")
    return to_be


rotor = []
switch = 0
reflector = {}
acted_text = 0
print("Welcome to the Enigma Machine simulator! This simulator utilizes 3 rotors with 6 options and a rotating "
      "reflector with three options. The rotors do not replicate the shift of the historical rotors, but do function "
      "the ")
print("same. This simulator also does not replicate the function of the plugboard, as that is just a simple "
      "substitution cipher, would be painful to input, and does very little to increase the security of the enigma.")
input("Press the enter key to begin.")
while True:
    ro1 = input("Which rotor would you like to put in the first slot? (A whole number between 1 and 6)")
    if len(ro1) >= 2 or int(ro1) <= 0 or int(ro1) >= 7:
        print("Invalid input. Please enter a whole number between 1 and 6.")
    else:
        ro1 = int(ro1)
        break
while True:
    n1 = float(input("Which initial position would you like the 1st rotor in? (A whole number between 1 and 26)")) - 1
    if int(n1) != float(n1) or int(n1) <= -1 or int(n1) >= 25:
        print("Invalid input. Please enter a whole number between 1 and 26.")
    else:
        n1 = int(n1)
        break

while True:
    ro2 = input("Which rotor would you like to put in the 2nd slot? (A whole number between 1 and 6 different from "
                "previous rotors)")
    if len(ro2) >= 2 or int(ro2) <= 0 or int(ro2) >= 7:
        print("Invalid input. Please enter a whole number between 1 and 6.")
    elif int(ro2) == ro1:
        print("Invalid input. Please enter a rotor that has not been used yet")
    else:
        ro2 = int(ro2)
        break
while True:
    n2 = float(input("Which initial position would you like the 2nd rotor in? (A whole number between 1 and 26)")) - 1
    if int(n2) != float(n2) or int(n2) <= -1 or int(n2) >= 25:
        print("Invalid input. Please enter a whole number between 1 and 26.")
    else:
        n2 = int(n2)
        break

while True:
    ro3 = input("Which rotor would you like to put in the 3rd slot? (A whole number between 1 and 6 different from "
                "previous rotors)")
    if len(ro3) >= 2 or int(ro3) <= 0 or int(ro3) >= 7:
        print("Invalid input. Please enter a whole number between 1 and 6.")
    elif int(ro3) == ro1 or int(ro3) == ro2:
        print("Invalid input. Please enter a rotor that has not been used yet")
    else:
        ro3 = int(ro3)
        break
while True:
    n3 = float(input("Which initial position would you like the 3rd rotor in? (A whole number between 1 and 26)")) - 1
    if int(n3) != float(n3) or int(n3) <= -1 or int(n3) >= 25:
        print("Invalid input. Please enter a whole number between 1 and 26.")
    else:
        n3 = int(n3)
        break

while True:
    ref = input("Which reflector would you like to use? (A whole number between 1 and 3)")
    if len(ref) >= 2 or int(ref) <= 0 or int(ref) >= 4:
        print("Invalid input. Please enter a whole number between 1 and 6.")
    else:
        ref = int(ref)
        break
while True:
    n4 = float(input("Which initial position would you like the reflector in? (A whole number between 1 and 26)")) - 1
    if int(n4) != float(n4) or int(n4) <= -1 or int(n4) >= 25:
        print("Invalid input. Please enter a whole number between 1 and 26.")
    else:
        n4 = int(n4)
        break

while True:
    orig = strip(str(input(
        "What text would you like to encode/decode? (No special characters. Numbers must be typed. Ex: 1 would be "
        "\"one\")")))
    if orig.isalpha():
        break
orig = orig.lower()

orig_numeric = []
for character in orig:
    number = ord(character) - 97
    orig_numeric.append(number)

switch_select(ro1)
_1switch = switch
switch_select(ro2)
_2switch = switch
switch_select(ro3)
_3switch = switch
reflector_select(ref)

output_numeric = []
for number in orig_numeric:
    rotor_action(ro1, n1, number)
    rotor_action(ro2, n2, acted_text)
    rotor_action(ro3, n3, acted_text)
    reflector_action(reflector, n4, acted_text)
    rotor_action_reverse(ro3, n3, acted_text)
    rotor_action_reverse(ro2, n2, acted_text)
    rotor_action_reverse(ro1, n1, acted_text)
    int(acted_text)
    output_numeric.append(acted_text)

    # rotor rotation code below
    n1 = n1 + 1
    if n1 == 26:
        n1 = 0
    if n1 == _1switch:
        n2 = n2 + 1
    if n2 == 26:
        n2 = 0
    if n2 == _2switch:
        n3 = n3 + 1
    if n3 == 26:
        n3 = 0
    if n3 == _3switch:
        n4 = n4 + 1
    if n4 == 26:
        n4 = 0

output_char = []
for number in output_numeric:
    character2 = chr(number + 97)
    output_char.append(character2)
output_final = ""
output_final = output_final.join(output_char)
output_final = str(output_final)
print(output_final)

input("Press the enter key to close the program.")

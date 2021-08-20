# below are the lists that serve as the enigma rotors. These "rotors" do not replicate historical rotor patterns but
# do replicate the function of actual rotors. Switches determine at which change that the next rotor steps.

rotor1 = [93, 70, 25, 29, 63, 48, 44, 51, 30, 91, 10, 4, 13, 41, 1, 65, 17, 52, 28, 42, 59, 11, 2, 66, 92, 49, 24, 36,
          72, 87, 83, 6, 88, 80, 61, 81, 90, 71, 79, 15, 60, 32, 62, 45, 43, 78, 14, 67, 33, 31, 7, 75, 64, 89, 12, 57,
          55, 21, 9, 77, 26, 76, 84, 18, 19, 23, 53, 73, 22, 35, 86, 54, 8, 50, 20, 3, 5, 34, 68, 56, 47, 38, 0, 27, 85,
          46, 40, 39, 37, 58, 74, 82, 16, 69]
switch1 = [60, 40, 55, 38, 76]
rotor2 = [12, 3, 91, 4, 28, 16, 45, 68, 38, 47, 55, 77, 60, 86, 36, 20, 75, 78, 85, 19, 15, 14, 30, 46, 49, 5, 18, 0,
          65, 72, 79, 92, 88, 17, 66, 56, 52, 67, 76, 69, 54, 44, 64, 23, 83, 87, 9, 59, 80, 71, 58, 63, 24, 81, 51, 37,
          42, 8, 1, 7, 25, 35, 11, 6, 10, 84, 2, 89, 53, 93, 50, 82, 22, 34, 62, 90, 40, 39, 74, 27, 29, 73, 33, 61, 70,
          26, 13, 21, 41, 31, 48, 43, 32, 57]
switch2 = [14, 67, 37, 1, 47]
rotor3 = [20, 67, 16, 27, 37, 33, 56, 19, 38, 7, 64, 93, 39, 75, 0, 36, 51, 41, 40, 4, 83, 86, 31, 18, 74, 90, 21, 79,
          58, 6, 61, 60, 71, 59, 14, 85, 3, 72, 9, 80, 47, 17, 34, 62, 66, 50, 42, 87, 89, 12, 65, 26, 88, 48, 73, 78,
          2, 29, 52, 1, 8, 43, 49, 91, 45, 77, 68, 15, 23, 53, 76, 25, 92, 11, 69, 30, 81, 84, 54, 5, 63, 24, 35, 44,
          22, 82, 57, 13, 10, 32, 46, 28, 70, 55]
switch3 = [1, 67, 14, 47, 37]
rotor4 = [27, 43, 5, 73, 14, 45, 22, 62, 87, 8, 9, 23, 21, 1, 68, 60, 74, 16, 7, 38, 33, 76, 37, 91, 31, 86, 69, 36, 39,
          55, 25, 20, 64, 92, 10, 44, 71, 54, 89, 67, 34, 57, 80, 30, 19, 77, 28, 58, 88, 24, 11, 90, 93, 51, 52, 78,
          81, 61, 46, 49, 3, 40, 63, 50, 2, 12, 56, 6, 47, 32, 41, 13, 4, 82, 48, 53, 17, 15, 42, 59, 79, 29, 84, 35,
          65, 85, 75, 0, 72, 83, 18, 70, 66, 26]
switch4 = [25, 80, 63, 40, 0]
rotor5 = [31, 44, 33, 9, 70, 10, 2, 37, 92, 87, 47, 8, 50, 0, 26, 93, 59, 13, 27, 41, 42, 58, 57, 84, 83, 65, 19, 48, 1,
          80, 11, 64, 73, 76, 66, 32, 52, 56, 28, 4, 45, 61, 5, 22, 12, 7, 35, 14, 21, 71, 39, 68, 51, 89, 18, 55, 60,
          67, 74, 75, 69, 81, 77, 23, 3, 40, 36, 20, 86, 29, 82, 16, 54, 79, 38, 90, 43, 34, 85, 53, 88, 25, 30, 63, 17,
          72, 78, 46, 24, 91, 62, 15, 6, 49]
switch5 = [36, 7, 88, 64, 47]
rotor6 = [71, 56, 40, 82, 88, 84, 28, 50, 58, 54, 38, 67, 15, 85, 61, 30, 17, 13, 18, 51, 49, 66, 70, 65, 22, 83, 77,
          19, 0, 27, 42, 62, 10, 91, 79, 41, 12, 72, 37, 73, 76, 8, 3, 90, 92, 31, 52, 34, 78, 26, 69, 47, 33, 16, 74,
          93, 89, 1, 9, 75, 46, 60, 55, 29, 68, 81, 4, 45, 59, 80, 36, 21, 87, 25, 43, 5, 32, 24, 35, 64, 39, 6, 53, 44,
          20, 48, 14, 2, 57, 7, 86, 23, 11, 63]
switch6 = [92, 37, 47, 33, 65]
rotor7 = [39, 66, 38, 55, 5, 82, 83, 32, 3, 17, 36, 76, 41, 43, 42, 14, 31, 35, 33, 13, 56, 68, 70, 50, 59, 19, 64, 29,
          48, 28, 27, 67, 71, 26, 10, 58, 72, 88, 85, 7, 63, 1, 87, 11, 51, 84, 89, 40, 86, 77, 81, 74, 75, 12, 78, 92,
          21, 62, 20, 79, 69, 9, 53, 44, 25, 34, 49, 73, 6, 2, 23, 52, 0, 8, 4, 22, 91, 37, 80, 61, 24, 93, 90, 46, 54,
          65, 15, 16, 60, 30, 47, 57, 45, 18]
switch7 = [59, 34, 61, 71, 67]
rotor8 = [75, 70, 31, 37, 78, 8, 22, 2, 40, 56, 54, 71, 55, 19, 41, 81, 17, 64, 86, 0, 5, 50, 48, 10, 59, 1, 89, 33, 69,
          93, 18, 92, 9, 90, 88, 85, 32, 53, 29, 27, 11, 24, 67, 21, 57, 49, 28, 83, 72, 46, 60, 43, 36, 76, 12, 87, 45,
          6, 74, 20, 47, 73, 35, 84, 7, 30, 16, 66, 44, 61, 4, 62, 63, 25, 52, 13, 38, 15, 79, 3, 58, 14, 91, 68, 51,
          34, 80, 77, 65, 26, 23, 39, 42, 82]
switch8 = [18, 3, 33, 67, 41]
rotor9 = [47, 28, 4, 43, 73, 38, 8, 87, 13, 63, 5, 11, 77, 79, 36, 80, 24, 57, 69, 35, 6, 58, 41, 0, 33, 78, 17, 51, 64,
          31, 9, 72, 92, 32, 20, 30, 42, 81, 49, 67, 90, 10, 1, 40, 71, 55, 76, 45, 37, 52, 22, 21, 82, 60, 86, 7, 46,
          83, 56, 91, 34, 18, 44, 54, 70, 61, 16, 75, 14, 12, 66, 29, 15, 68, 88, 26, 25, 62, 50, 27, 48, 53, 84, 85,
          19, 93, 2, 89, 59, 39, 65, 23, 3, 74]
switch9 = [30, 6, 53, 83, 26]
rotor10 = [74, 42, 10, 13, 91, 41, 21, 75, 88, 43, 31, 46, 7, 6, 44, 8, 66, 16, 9, 25, 48, 20, 29, 23, 33, 89, 67, 79,
           58, 59, 92, 2, 80, 27, 30, 14, 15, 60, 18, 28, 5, 61, 35, 51, 0, 56, 86, 49, 77, 22, 64, 70, 36, 81, 32, 19,
           62, 24, 85, 11, 71, 39, 76, 53, 68, 55, 1, 12, 90, 40, 83, 52, 63, 87, 3, 34, 50, 57, 37, 93, 17, 47, 73, 65,
           54, 45, 69, 78, 84, 26, 4, 82, 72, 38]
switch10 = [76, 18, 49, 40, 16]
# below are the dictionaries that serve as the reflectors. The reflectors are dictionaries with identical but
# inverted pairs because the reflectors
reflector1 = {51: 19, 2: 14, 45: 35, 6: 26, 92: 60, 10: 65, 83: 61, 68: 28, 46: 22, 32: 37, 31: 67, 9: 36, 56: 64,
              66: 7, 50: 4, 30: 41, 42: 80, 81: 82, 71: 20, 87: 53, 77: 89, 85: 25, 23: 21, 76: 43, 38: 59, 5: 91,
              79: 84, 39: 48, 88: 58, 75: 73, 62: 74, 1: 72, 34: 12, 0: 29, 70: 33, 8: 15, 17: 57, 47: 13, 93: 49,
              11: 63, 27: 18, 86: 55, 16: 44, 52: 90, 24: 78, 54: 69, 3: 40, 40: 3, 69: 54, 78: 24, 90: 52, 44: 16,
              55: 86, 18: 27, 63: 11, 49: 93, 13: 47, 57: 17, 15: 8, 33: 70, 29: 0, 12: 34, 72: 1, 74: 62, 73: 75,
              58: 88, 48: 39, 84: 79, 91: 5, 59: 38, 43: 76, 21: 23, 25: 85, 89: 77, 53: 87, 20: 71, 82: 81, 80: 42,
              41: 30, 4: 50, 7: 66, 64: 56, 36: 9, 67: 31, 37: 32, 22: 46, 28: 68, 61: 83, 65: 10, 60: 92, 26: 6,
              35: 45, 14: 2, 19: 51}
reflector2 = {38: 44, 14: 87, 70: 37, 20: 24, 12: 2, 27: 66, 68: 83, 36: 23, 67: 73, 90: 71, 88: 65, 10: 84, 49: 30,
              17: 15, 35: 21, 18: 8, 74: 72, 31: 91, 93: 82, 41: 48, 11: 26, 55: 19, 56: 28, 29: 57, 22: 64, 86: 59,
              3: 51, 62: 61, 1: 45, 80: 75, 43: 16, 85: 92, 54: 42, 34: 81, 69: 52, 60: 58, 78: 32, 4: 79, 33: 39,
              25: 47, 50: 13, 6: 89, 7: 63, 5: 76, 40: 46, 53: 77, 0: 9, 9: 0, 77: 53, 46: 40, 76: 5, 63: 7, 89: 6,
              13: 50, 47: 25, 39: 33, 79: 4, 32: 78, 58: 60, 52: 69, 81: 34, 42: 54, 92: 85, 16: 43, 75: 80, 45: 1,
              61: 62, 51: 3, 59: 86, 64: 22, 57: 29, 28: 56, 19: 55, 26: 11, 48: 41, 82: 93, 91: 31, 72: 74, 8: 18,
              21: 35, 15: 17, 30: 49, 84: 10, 65: 88, 71: 90, 73: 67, 23: 36, 83: 68, 66: 27, 2: 12, 24: 20, 37: 70,
              87: 14, 44: 38}
reflector3 = {51: 36, 90: 85, 39: 48, 93: 58, 72: 43, 23: 9, 34: 18, 24: 49, 52: 77, 84: 86, 55: 21, 89: 74, 8: 79,
              26: 31, 73: 3, 50: 22, 7: 68, 82: 42, 29: 78, 37: 92, 28: 57, 6: 41, 46: 14, 33: 59, 40: 35, 53: 71,
              88: 16, 65: 60, 75: 80, 10: 61, 38: 47, 5: 76, 30: 45, 54: 11, 81: 66, 87: 44, 69: 12, 67: 25, 4: 0,
              13: 2, 70: 64, 1: 62, 27: 83, 15: 56, 17: 32, 20: 19, 91: 63, 63: 91, 19: 20, 32: 17, 56: 15, 83: 27,
              62: 1, 64: 70, 2: 13, 0: 4, 25: 67, 12: 69, 44: 87, 66: 81, 11: 54, 45: 30, 76: 5, 47: 38, 61: 10, 80: 75,
              60: 65, 16: 88, 71: 53, 35: 40, 59: 33, 14: 46, 41: 6, 57: 28, 92: 37, 78: 29, 42: 82, 68: 7, 22: 50,
              3: 73, 31: 26, 79: 8, 74: 89, 21: 55, 86: 84, 77: 52, 49: 24, 18: 34, 9: 23, 43: 72, 58: 93, 48: 39,
              85: 90, 36: 51}
reflector4 = {55: 83, 79: 45, 76: 91, 87: 53, 9: 49, 69: 16, 73: 21, 36: 68, 32: 0, 86: 92, 2: 82, 4: 12, 59: 51,
              89: 27, 19: 54, 6: 75, 26: 46, 38: 72, 74: 62, 93: 88, 17: 64, 84: 57, 60: 52, 1: 25, 50: 61, 43: 39,
              33: 71, 20: 22, 65: 24, 66: 58, 13: 11, 34: 56, 8: 29, 30: 90, 7: 10, 40: 18, 67: 47, 42: 15, 44: 85,
              14: 35, 48: 77, 63: 31, 3: 78, 81: 5, 70: 28, 80: 23, 37: 41, 41: 37, 23: 80, 28: 70, 5: 81, 78: 3,
              31: 63, 77: 48, 35: 14, 85: 44, 15: 42, 47: 67, 18: 40, 10: 7, 90: 30, 29: 8, 56: 34, 11: 13, 58: 66,
              24: 65, 22: 20, 71: 33, 39: 43, 61: 50, 25: 1, 52: 60, 57: 84, 64: 17, 88: 93, 62: 74, 72: 38, 46: 26,
              75: 6, 54: 19, 27: 89, 51: 59, 12: 4, 82: 2, 92: 86, 0: 32, 68: 36, 21: 73, 16: 69, 49: 9, 53: 87, 91: 76,
              45: 79, 83: 55}


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
    elif x == 7:
        rotor = rotor7
    elif x == 8:
        rotor = rotor8
    elif x == 9:
        rotor = rotor9
    elif x == 10:
        rotor = rotor10
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
    elif x == 7:
        switch = switch7
    elif x == 8:
        switch = switch8
    elif x == 9:
        switch = switch9
    elif x == 10:
        switch = switch10
    return


def reflector_select(x):
    global reflector
    if x == 1:
        reflector = reflector1
    elif x == 2:
        reflector = reflector2
    elif x == 3:
        reflector = reflector3
    elif x == 4:
        reflector = reflector4
    return


def rotor_action(which_rotor, n, text):
    global acted_text
    rotor_select(which_rotor)
    shift = text + n
    if shift >= 94:
        shift -= 94
    acted_text = rotor[shift]
    return


def rotor_action_reverse(which_rotor, n, text):
    global acted_text
    rotor_select(which_rotor)
    acted_text = rotor.index(text)
    acted_text = acted_text - n
    if acted_text <= -1:
        acted_text += 94

    return


def reflector_action(which_reflector, n, text):
    global acted_text
    shift = text + n
    if shift >= 94:
        shift -= 94
    acted_text = which_reflector[shift]
    acted_text -= n
    if acted_text <= -1:
        acted_text += 94
    return


rotor = []
switch = 0
reflector = {}
acted_text = 0
print("Welcome to the Improved Enigma Machine simulator! This simulator mimics the mechanics of the enigma machine ("
      "except without the plugboard), but with larger and more complex rotors,")
print("allowing more secure encryption and encoding of sentences with spaces and punctuation.")
input("Press the enter key to begin.")
while True:
    ro1 = input("Which rotor would you like to put in the first slot? (A whole number between 1 and 10)")
    if len(ro1) >= 3 or int(ro1) <= 0 or int(ro1) >= 11:
        print("Invalid input. Please enter a whole number between 1 and 10.")
    else:
        ro1 = int(ro1)
        break
while True:
    n1 = float(input("Which initial position would you like the 1st rotor in? (A whole number between 1 and 94)")) - 1
    if int(n1) != float(n1) or int(n1) <= -1 or int(n1) >= 94:
        print("Invalid input. Please enter a whole number between 1 and 94.")
    else:
        n1 = int(n1)
        break

while True:
    ro2 = input("Which rotor would you like to put in the 2nd slot? (A whole number between 1 and 10)")
    if len(ro2) >= 3 or int(ro2) <= 0 or int(ro2) >= 11:
        print("Invalid input. Please enter a whole number between 1 and 10.")
    else:
        ro2 = int(ro2)
        break
while True:
    n2 = float(input("Which initial position would you like the 2nd rotor in? (A whole number between 1 and 94)")) - 1
    if int(n2) != float(n2) or int(n2) <= -1 or int(n2) >= 94:
        print("Invalid input. Please enter a whole number between 1 and 94.")
    else:
        n2 = int(n2)
        break

while True:
    ro3 = input("Which rotor would you like to put in the 3rd slot? (A whole number between 1 and 10)")
    if len(ro3) >= 3 or int(ro3) <= 0 or int(ro3) >= 11:
        print("Invalid input. Please enter a whole number between 1 and 10.")
    else:
        ro3 = int(ro3)
        break
while True:
    n3 = float(input("Which initial position would you like the 3rd rotor in? (A whole number between 1 and 94)")) - 1
    if int(n3) != float(n3) or int(n3) <= -1 or int(n3) >= 94:
        print("Invalid input. Please enter a whole number between 1 and 94.")
    else:
        n3 = int(n3)
        break

while True:
    ref = input("Which reflector would you like to use? (A whole number between 1 and 4)")
    if len(ref) >= 2 or int(ref) <= 0 or int(ref) >= 5:
        print("Invalid input. Please enter a whole number between 1 and 6.")
    else:
        ref = int(ref)
        break
while True:
    n4 = float(input("Which initial position would you like the reflector in? (A whole number between 1 and 94)")) - 1
    if int(n4) != float(n4) or int(n4) <= -1 or int(n4) >= 94:
        print("Invalid input. Please enter a whole number between 1 and 26.")
    else:
        n4 = int(n4)
        break

orig = str(input("What text would you like to encode/decode?"))

orig_numeric = []
for character in orig:
    number = ord(character) - 32
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
    if n1 == 94:
        n1 = 0
    if n1 in _1switch:
        n2 = n2 + 1
    if n2 == 94:
        n2 = 0
    if n2 in _2switch:
        n3 = n3 + 1
    if n3 == 94:
        n3 = 0
    if n3 in _3switch:
        n4 = n4 + 1
    if n4 == 94:
        n4 = 0

output_char = []
for number in output_numeric:
    character2 = chr(number + 32)
    output_char.append(character2)
output_final = ""
output_final = output_final.join(output_char)
output_final = str(output_final)
print(output_final)

input("Press the enter key to close the program.")

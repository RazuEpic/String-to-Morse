morse_translation = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

user_input = input("Enter a sentence / paragraph using the english alphabet or numbers. And it will be translated to morse\n").lower()

translated_message = ""

for char in user_input:
    if char in morse_translation:
        translated_message += morse_translation[char] + " "
    else:
        translated_message += char + " "

print("Morse Code : ", translated_message)

code = { "a": "q", "b": "x", "c": "j", "d": "z", "e": "v", "f": "p", "g": "k", "h": "u", "i": "w", "j": "y", "k": "b", "l": "t", "m": "r", "n": "d", "o": "h", "p": "s", "q": "e", "r": "a", "s": "i", "t": "f", "u": "l", "v": "g", "w": "o", "x": "n", "y": "c", "z": "m", " ": "1" }
string = input()
string1 = ""
for x in string:
    y = code[x]
    string1 = string1 + y
print(string1)
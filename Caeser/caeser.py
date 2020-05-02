import sys
import string
teststring = "Hello this SHOULD be encoded!"
# dict with all available ciphers and encoding functions
ciphers = {"Caeser": ['encode_Caeser']}


def encode_Caeser(text, startletter):
    """[encodes the text shiftet by startletter and returns it as a string case not affected]

    Arguments:
        text {[string]} -- [text to be encoded]
        startletter {[int, string]} -- [value that the caeser cipher shifts the text]
    """
    out = []
    # alphabet doubles to acompish all shifts
    alpha = string.ascii_lowercase+string.ascii_lowercase
    # shift of the encoding
    shift = _get_shift(startletter)
    # check every character if in ascii lower shift by shift units
    for letter in text:
        if letter.lower() in alpha:
            outindex = int(alpha.index(letter.lower()))+shift
            if letter.islower():
                out.append(alpha[outindex])
            elif letter.isupper():
                out.append(alpha[outindex].upper())
        # For all other non letters
        else:
            out.append(letter)
    return "".join(out)


def runencoding():
    """Runs the encoding"""
    print("Available ciphers: \n{}".format("\n".join(ciphers.keys())))
    print("------------")
    while True:
        dec = input("What to do: (q = quit, e: encrypt, d: decrypt) \n")
        if dec == 'q':
            sys.exit()
        elif dec == 'e':
            instring, shift = _get_inputs()
            print(encode_Caeser(instring, shift))
        elif dec == 'd':
            instring, shift = _get_inputs()
            try:
                shift = -shift
            except ValueError:
                shift = -(string.ascii_lowercase.index(shift))
            print(encode_Caeser(instring, shift))


def _get_shift(startletter):
    """Get the number of the shift"""
    alpha = string.ascii_lowercase+string.ascii_lowercase
    if type(startletter) == int:
        shift = startletter
    else:
        shift = alpha.index(startletter.lower())
    return shift


def _get_inputs():
    """Gets inputs and checks if they are valid. returns instring (a string),
    returns shift either an int <27 or a ascii lowercase letter"""
    while True:
        instring = input("Enter a string to encrypt: ")
        if type(instring) == str:
            break
        print("Please enter a valid string ")
    while True:
        shift = input("Enter number shift or letter to shift: ")
        try:
            shift = int(shift)
            if shift < 27:
                break
        except ValueError:
            if shift.lower() in string.ascii_lowercase and len(shift) == 1:
                break
        print("Please enter a valid number or a single string")
    return instring, shift


runencoding()

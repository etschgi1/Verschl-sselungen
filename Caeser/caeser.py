import string
teststring = "Hello this SHOULD be encoded!"


def encode(text, startletter):
    """Input string to encode, only alphabet letters will be encoded. Start letter for the encoding
    out: a string with the encoded message"""
    try:
        out = []
        # alphabet doubles to acompish all shifts
        alpha = string.ascii_lowercase+string.ascii_lowercase
        # shift of the encoding
        if type(startletter) == int:
            shift = startletter
        else:
            shift = alpha.index(startletter.lower())
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
        return(out)
    except:
        print("not")


#instring = input("Enter a string to encrypt: ")


print(encode(teststring, 5))

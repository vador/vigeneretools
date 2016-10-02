def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def charstrxor(char, str):
    cc = ord(char)
    return "".join([chr(ord(x) ^ cc) for x in str])


def hex2string(hexstr):
    """
    :param hexstr: hex encoded string
    :return: litteral string of values
    """
    return bytearray.fromhex(hexstr).decode("iso-8859-1")


def printashex(s):
    return "".join("{:02x}".format(ord(c)) for c in s)


def computefreqs(text):
    myFreqs = [0] * 256
    for car in text:
        myFreqs[ord(car)] += 1
    for freq in range(len(myFreqs)):
        myFreqs[freq] /= len(text)

    return myFreqs

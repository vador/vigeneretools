def strxor(a, b):  # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def hex2string(hexstr):
    """
    :param hexstr: hex encoded string
    :return: litteral string of values
    """
    return bytearray.fromhex(hexstr).decode("iso-8859-1")


def printashex(s):
    return "".join("{:02x}".format(ord(c)) for c in s)


def encrypt(hexkey, hexmessage):
    key = hex2string(hexkey)
    message = hex2string(hexmessage)
    outputmsg = ""
    keypos = 0
    msgpos = 0
    keylen = len(key)
    while (msgpos < len(message)):
        if message[msgpos] == 13:
            msgpos += 1
            outputmsg += 13
        else:
            outputmsg += chr(ord(message[msgpos]) ^ ord(key[keypos]))
            msgpos += 1
            keypos = (keypos + 1) % keylen
    return outputmsg


def decrypt(hexkey, hexmessage):
    key = hex2string(hexkey)
    message = hex2string(hexmessage)
    outputmsg = ""
    keypos = 0
    msgpos = 0
    keylen = len(key)
    while (msgpos < len(message)):
        if message[msgpos] == 13:
            msgpos += 1
            outputmsg += 13
        else:
            outputmsg += chr(ord(message[msgpos]) ^ ord(key[keypos]))
            msgpos += 1
            keypos = (keypos + 1) % keylen
    return outputmsg


if __name__ == "__main__":
    with open("cyphertext-bis.txt", "r") as f:
        MSG = (f.read())
    # MSG2 = printashex(MSG)
    # MSG3 = hex2string(MSG2)
    KEY = "f4c8c9d380c9c1"
    KEY = "ba1f91b253cd3e"
    print((decrypt(KEY, MSG)))

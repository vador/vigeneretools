import hexHelpers

myFreqs = [0] * 256
nbCars = 0

with open("sourcetext.txt", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        nbCars += 1
        myFreqs[ord(byte)] +=1

        # Do stuff with byte.
        byte = f.read(1)

print(myFreqs)
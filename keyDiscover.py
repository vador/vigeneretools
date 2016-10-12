from math import sqrt

from hexHelpers.hexhelpers import computefreqs, charstrxor, hex2string, printashex

COUNTS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3955, 0, 0, 3955, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19112,
          1,
          10, 0, 5, 54, 0, 0, 451, 451, 214, 0, 962, 692, 1283, 295, 586, 609, 475, 248, 319, 234, 211, 189, 183, 164,
          722, 160, 7, 37, 6, 3, 24, 842, 238, 697, 771, 734, 189, 243, 47, 523, 4, 544, 372, 252, 415, 300, 523, 89,
          548, 851, 823, 233, 39, 114, 11, 48, 7, 152, 13, 152, 0, 661, 0, 6455, 674, 4412, 4227, 14104, 1451, 828, 855,
          7301, 142, 435, 4319, 2546, 6910, 5359, 3147, 657, 6763, 8023, 8920, 5177, 1206, 186, 421, 638, 25, 1, 1, 1,
          0, 0, 1047, 4, 4, 2, 1, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 1041, 0, 0, 0, 0, 41, 0,
          285, 0, 0, 0, 1, 0, 0, 12, 261, 2373, 156, 14, 0, 0, 26, 0, 0, 0, 0, 0, 73, 0, 0, 0, 0, 13, 0, 16, 0, 0, 0, 0,
          0, 0, 28, 3213, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          1070, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

FREQS = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.026902748773901274, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.13000387726088525, 6.8022120793682105e-06,
         6.802212079368211e-05, 0.0, 3.4011060396841056e-05, 0.00036731945228588334, 0.0, 0.0, 0.003067797647795063,
         0.003067797647795063, 0.001455673384984797, 0.0, 0.0065437280203522186, 0.004707130758922802,
         0.008727238097829415, 0.002006652563413622, 0.003986096278509771, 0.00414254715633524, 0.0032310507376999,
         0.0016869485956833162, 0.002169905653318459, 0.0015917176265721612, 0.0014352667487466924,
         0.0012856180830005917, 0.0012448048105243826, 0.0011155627810163866, 0.004911197121303848,
         0.0010883539326989138, 4.761548455557748e-05, 0.00025168184693662377, 4.081327247620926e-05,
         2.040663623810463e-05, 0.00016325308990483705, 0.005727462570828033, 0.001618926474889634,
         0.0047411418193196424, 0.00524450551319289, 0.004992823666256267, 0.0012856180830005917,
         0.0016529375352864752, 0.0003197039677303059, 0.0035575569175095743, 2.7208848317472842e-05,
         0.0037004033711763064, 0.002530422893524974, 0.001714157444000789, 0.0028229180129378073,
         0.002040663623810463, 0.0035575569175095743, 0.0006053968750637707, 0.0037276122194937794,
         0.0057886824795423475, 0.0055982205413200375, 0.001584915414492793, 0.0002652862710953602,
         0.000775452177047976, 7.482433287305032e-05, 0.0003265061798096741, 4.761548455557748e-05,
         0.001033936236063968, 8.842875703178673e-05, 0.001033936236063968, 0.0, 0.004496262184462387, 0.0,
         0.0439082789723218, 0.004584690941494174, 0.030011359694172544, 0.028752950459489425, 0.09593839916740925,
         0.009870009727163273, 0.005632231601716878, 0.00581589132785982, 0.04966295039146731, 0.000965914115270286,
         0.0029589622545251716, 0.029378753970791302, 0.017318431954071463, 0.04700328546843433, 0.03645305453333424,
         0.021406561413771757, 0.004469053336144915, 0.046003360292767206, 0.054574147512771155, 0.06067573174796444,
         0.035215051934889226, 0.008203467767718062, 0.001265211446762487, 0.0028637312854140166, 0.004339811306636918,
         0.00017005530198420526, 6.8022120793682105e-06, 6.8022120793682105e-06, 6.8022120793682105e-06, 0.0, 0.0,
         0.007121916047098517, 2.7208848317472842e-05, 2.7208848317472842e-05, 1.3604424158736421e-05,
         6.8022120793682105e-06, 0.0, 0.0, 0.0, 0.0, 7.482433287305032e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.000129242029507996, 0.0, 0.0, 0.0, 0.0, 0.0, 0.007081102774622307, 0.0, 0.0, 0.0, 0.0,
         0.00027889069525409665, 0.0, 0.00193863044261994, 0.0, 0.0, 0.0, 6.8022120793682105e-06, 0.0, 0.0,
         8.162654495241853e-05, 0.0017753773527151029, 0.016141649264340762, 0.0010611450843814407,
         9.523096911115495e-05, 0.0, 0.0, 0.00017685751406357347, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0004965614817938794, 0.0,
         0.0, 0.0, 0.0, 8.842875703178673e-05, 0.0, 0.00010883539326989137, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0001904619382223099, 0.02185550741101006, 0.0, 0.000129242029507996, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.007278366924923985, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def extracticypher(msg, i, keylength):
    return msg[i::keylength]


def computeDist(iFreqs):
    dist = sqrt(sum([(x - y) * (x - y) for (x, y) in zip(FREQS, iFreqs)]))
    return dist


def isvalidpermutation(iFreqs):
    myFreqs = iFreqs[:]
    myFreqs[10] = 0
    myFreqs[13] = 0
    if sum(myFreqs[:32]) > 0:
        return False
    return True


def getiposcandidates(cipher):
    candidates = []
    for xor in range(256):
        icipher = charstrxor(chr(xor), cipher)
        iFreqs = computefreqs(icipher)
        if isvalidpermutation(iFreqs):
            dist = computeDist(iFreqs)
            candidates.append((xor, dist))

    candidates.sort(key=lambda x: x[1])
    return candidates


def compute():
    pass


def getciphertext():
    with open("cyphertext2.txt", "r") as f:
        HEXMSG = (f.read())
    MSG = hex2string(HEXMSG)
    return MSG


def keycandidatesbydist(msg, keylength):
    allkeycandidates = []
    for i in range(keylength):
        ipos = extracticypher(msg, i, keylength)
        candid = getiposcandidates(ipos)
        allkeycandidates.append(candid)
    return allkeycandidates


def keycandidatesreconstruct(keycandidateslist):
    return "".join([chr(x[0][0]) for x in keycandidateslist])


if __name__ == "__main__":
    msg = getciphertext()
    """
    ipos1 = extracticypher(msg, 0, 23)
    print(ipos1[:10])
    print(charstrxor(hex2string("f4"), ipos1)[:10])
    candid1 = getiposcandidates(ipos1)
    print(candid1)
    ipos2 = extracticypher(msg, 1, 23)
    candid2 = getiposcandidates(ipos2)
    print(candid2)
        """
    kc = keycandidatesbydist(msg, 7)
    kcrec = keycandidatesreconstruct(kc)
    print(printashex(kcrec))

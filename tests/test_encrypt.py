from unittest import TestCase

from VigenereEncrypt import printashex, encrypt
from hexHelpers.hexhelpers import hex2string, charstrxor


class TestEncrypt(TestCase):
    def test_should_return_known_value_for_simple_key(self):
        KEY = "A0A0"
        MSG = printashex("This is a test message.")
        ExpMSG = "f4c8c9d380c9d380c180d4c5d3d480cdc5d3d3c1c7c58e"
        TestEncrypt.assertEqual(self,ExpMSG,printashex(encrypt(KEY,MSG)))

    def test_should_return_starting_message_for_double_encoding(self):
        KEY = "A0FF0002"
        MSG = printashex("This is a test message.")
        ExpMSG = "f4c8c9d380c9d380c180d4c5d3d480cdc5d3d3c1c7c58e"
        TestEncrypt.assertEqual(self,MSG,printashex(encrypt(KEY,printashex(encrypt(KEY,MSG)))))

    def test_should_encrypt_key_1_equal_xor(self):
        KEY = "B3"
        MSG = printashex("This is a test message.")
        ENCRYPT = encrypt(KEY, MSG)
        XOR = charstrxor(hex2string(KEY), hex2string(MSG))
        TestEncrypt.assertEqual(self, ENCRYPT, XOR)

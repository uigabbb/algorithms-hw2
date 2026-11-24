import unittest

from src.base62 import ALPHABET, decode, encode


class Base62Tests(unittest.TestCase):
    def test_encode_zero_and_alphabet_digits(self):
        self.assertEqual(encode(0), "0")
        for value, character in enumerate(ALPHABET):
            with self.subTest(value=value):
                self.assertEqual(encode(value), character)

    def test_encode_uses_expected_digit_order(self):
        self.assertEqual(encode(61), "Z")
        self.assertEqual(encode(62), "10")
        self.assertEqual(encode(63), "11")

    def test_round_trip(self):
        values = [0, 1, 61, 62, 12345, 2**64, 10**100]
        for value in values:
            with self.subTest(value=value):
                self.assertEqual(decode(encode(value)), value)

    def test_encode_rejects_invalid_values(self):
        for value in (True, 1.5, "12"):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    encode(value)
        with self.assertRaises(ValueError):
            encode(-1)

    def test_decode_rejects_invalid_values(self):
        for value in (None, 12):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    decode(value)
        for value in ("", "abc!", "é"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    decode(value)


if __name__ == "__main__":
    unittest.main()

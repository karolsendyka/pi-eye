import unittest
import pi_eye


class MyTestCase(unittest.TestCase):

    # available classes ['Blekitne suzuki', 'bialy bus', 'chrupek', 'czarne suzuki', 'czerwona mazda', 'srebrny golf']
    CLASS_CHRUPEK = 'chrupek'
    CLASS_GOLF = 'srebrny golf'

    CHRUPEK_PHOTO = "./test-data/chrupek/03-20210109122815-00.jpg"
    GOLF_PHOTO = "./test-data/golf/04-20210108112804-01.jpg"

    target = pi_eye

    def test_example_photos(self):
        self.assertEqual(pi_eye.classify(self.CHRUPEK_PHOTO), self.CLASS_CHRUPEK)
        self.assertEqual(pi_eye.classify(self.GOLF_PHOTO), self.CLASS_GOLF)


if __name__ == '__main__':
    unittest.main()

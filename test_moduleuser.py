from moduleuser import do_something
from unittest import TestCase


class MyTest(TestCase):

    def test_main(self):
        self.assertEqual(do_something(), 1)

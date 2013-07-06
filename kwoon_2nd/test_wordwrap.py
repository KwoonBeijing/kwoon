import unittest
from wordwrap import Wrapper

class TestWordWrap(unittest.TestCase):
    def test_no_need_to_wrap(self):
        wrapper = Wrapper()
        self.assertEqual(wrapper.wrap("something", 34),
                         "something")
    
    def test_need_to_wrap(self):
        wrapper = Wrapper()
        self.assertEqual(wrapper.wrap("some really", 6), "some\nreally")
    
    def test_need_to_wrap_longword(self):
        wrapper = Wrapper()
        self.assertEqual(wrapper.wrap("something", 7), "somethi\nng")
        
    def test_need_to_wrap_another_long_word(self):
        wrapper = Wrapper()
        self.assertEqual(wrapper.wrap("ab", 1), "a\nb")
        
unittest.main()
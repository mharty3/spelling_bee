import unittest

from word_finder import letters_in_word, check_word, word_finder, find_pangrams

class TestLettersInWord(unittest.TestCase):
    
    # test string input letters
    def test_single_letter_is_at_start_of_string(self):
        result = letters_in_word('a', 'apple')
        self.assertTrue(result)


    def test_single_letter_is_in_string(self):
        result = letters_in_word('p', 'apple')
        self.assertTrue(result)


    def test_single_letter_not_in_string(self):
        result = letters_in_word('z', 'apple')
        self.assertFalse(result)

    
    def test_multi_letter_string(self):
        result = letters_in_word('app', 'apple')
        self.assertTrue(result)


    def test_multi_letter_string_not_in_word(self):
        result = letters_in_word('zxc', 'apple')
        self.assertFalse(result)


    # test list input letters
    def test_multi_letter_letter_list(self):
        result = letters_in_word(['a', 'p', 'p'], 'apple')
        self.assertTrue(result)


    def test_multi_letter_letter_list_fail(self):
        result = letters_in_word(['y', 'z', 'x'], 'apple')
        self.assertFalse(result)


class TestCheckWord(unittest.TestCase):

    def test_check_word(self):
        self.assertTrue(check_word('pill', 'liupyubc')) # test a good word
        self.assertTrue(check_word('publicly', 'liuypubc')) # test pangram

        # test failing cases
        self.assertFalse(check_word('ill', 'liupuybc')) # too short
        self.assertFalse(check_word('cubby', 'liupuybc')) # no "key" letter
        self.assertFalse(check_word('prior', 'liupuybc')) # contains bad letters


class TestWordFinder(unittest.TestCase):

    def test_key_letter_in_all_words(self):
        good_words_to_test = word_finder('liupybc')
        
        results = ['l' in w for w in good_words_to_test]
        self.assertTrue(all(results))


    def test_all_words_have_four_or_more_letters(self):
        good_words_to_test = word_finder('liupycb')
        
        results = [len(w) >= 4 for w in good_words_to_test]
        self.assertTrue(all(results))


    def test_only_good_letters_in_words(self):
        good_letters = 'liupycb'
        good_words_to_test = word_finder(good_letters)
        
        results = [set(w).issubset(good_letters) for w in good_words_to_test]
        self.assertTrue(all(results))

class TestPangram(unittest.TestCase):

    def test_pangram(self):
        word_list = ['pill', 'clubby', 'cyclicly', 'publicly']
        self.assertEqual(find_pangrams(word_list), ['publicly'])

        word_list.append('upblicly') # add another "pangram"
        self.assertEqual(len(find_pangrams(word_list)), 2) # Find multiple pangrams

        word_list = word_list[:3]
        self.assertEqual(find_pangrams(word_list), []) # no pangrams

if __name__ == "__main__":
    unittest.main()
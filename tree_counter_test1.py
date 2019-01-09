import unittest
import tree_counter


class TreeCounterTest(unittest.TestCase):

    tree_builder_test = tree_counter.pickleloader("tree_counter_test_pickle").keys()
    known_values1 = ("sweet", len(tree_builder_test))

    def test_tree_counter_launcher(self):
        '''
        given a word tree_counter_launcher should return a counter with a count of all the words in the word's semantic tree
        '''
        word_in, output = self.known_values1
        tree_builder = tree_counter.pickleloader("tree_builder_pickled")

        result_prelim = tree_counter.tree_counter_launcher(tree_builder, word_in).keys()
        result = len(result_prelim)
        self.assertEqual(result, output)


    def test_tree_counter(self):
        '''
        given a pickle file, pickleloader should be able to load it for reading
        '''
        pass

    def test_similarity_score(self):
        '''
        given a pickle file, pickleloader should be able to load it for reading
        '''
        pass

if __name__ == '__main__':
    unittest.main()

from email.policy import default
from typing import Tuple

from tree_builder import TreeBuilder, Node
import sys
import _pickle as pickle
import pprint
from collections import Counter


# function to load pickle file
def pickleloader(filename):
    # # open the file for writing
    fileObject = open(filename,'rb')

    # load the object from the file into var univ_processed_train
    return pickle.load(fileObject,  encoding="latin1")  #latin1 here, to bypass
                                        # python2 to 3 pickle problem

    # here we close the fileObject
    fileObject.close()

# function to create a file and store the data in the file
def picklemaker(filename, objectname):
    # open the file for writing
    fileObject = open(filename,'wb')

    # this writes the object a to the
    # file named 'testfile'
    pickle.dump(objectname,fileObject)

    # here we close the fileObject
    fileObject.close()


def tree_counter_launcher(tree_builder: TreeBuilder, root_word: str, max_depth: int = 5) -> Counter:
    """Produce a counter that counts the different words in the tree starting from root_word and with a maximal depth
    of max_depth, according to the semantic graph stored in tree_builder

    This launcher's main is to find the word object in the wordbase
    """

    try:
        # Find the word in the wordbase
        root_word_node = tree_builder.primitives.get(root_word,  # we search the word among the primitives
                                                     # if we do net find it we search among the processed words
                                                     tree_builder.processed_words.get(root_word))

        return tree_counter(root_word_node, max_depth)

    except KeyError:
        print("Word {} is not present in the wordbase".format(root_word))
        return Counter()


def tree_counter(root_word: Node, max_depth: int) -> Counter:
    """Produce a counter that counts the different words in the tree starting from root_word and with a maximal depth
    of max_depth"""
    counter = Counter()
    counter[root_word] += 1
    if root_word is None:
        print(5454)

    # if we have not reached the maximal depth, we look at the children
    # word counter
    if max_depth > 0:
        # Add the counters of all the children of the node
        for child in root_word.children:
            counter += tree_counter(child, max_depth - 1)

    return counter


def similarity_score(tree_counter_1: Counter, tree_counter_2: Counter) -> Tuple[int, int]:
    # similarity - elements that are in both trees
    similarity = tree_counter_1 & tree_counter_2

    # dissimilarity - elements in 1 but not the other
    # create a copy of the counter and subtract the second counter to it
    difference = Counter(tree_counter_1)
    difference.subtract(tree_counter_2)
    # get the absolute value
    for key in difference: difference[key] = abs(difference[key])

    # total
    total = tree_counter_1 + tree_counter_2

    # produce the ratios
    similarity_ratio = sum(similarity.values()) / sum(total.values())
    difference_ratio = sum(difference.values()) / sum(total.values())

    return similarity_ratio, difference_ratio


if __name__ == "__main__":
    tree_builder = pickleloader("tree_builder_pickled")
    # pprint.pprint([i for i in tree_builder.processed_words])
    print(tree_counter_launcher(tree_builder, "taste"))

    print(tree_builder.processed_words.keys())
    print(similarity_score(tree_counter_launcher(tree_builder, "taste"), tree_counter_launcher(tree_builder, "food")))

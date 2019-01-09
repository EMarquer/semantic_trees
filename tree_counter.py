from tree_builder import TreeBuilder
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


def TreeCounter(tree_builder, root_Word, max_depth=5):
    '''
    A counter that counts the different words in the tree starting from root_word and with a maximal depth of max_depth, according to the semantic graph stored in tree_builder

    input:  tree_builder: instance of a tree_builder class
            root_Word: instancen of a Word class that serves as the root of the tree
    result: a counter with the counts of each instance of a Word or Primitive within a semantic tree.
    '''
    Words_in_tree = []
    root_Word_queue = [[root_Word]]
    current_depth = 0

    while current_depth < max_depth and len(root_Word_queue) != 0:

        current_level = root_Word_queue.pop(0)
        for Word in current_level:

            children_Words = Word.children

            Words_in_tree.append(Word)

            root_Word_queue.append(children_Words)

        current_depth += 1

    word_counter = Counter(Words_in_tree)
    return word_counter




def similarity_score(tree_counter_1, tree_counter_2):
    #similarty - elements that are in both trees
    similar = tree_counter_1.union(tree_counter_2)
    # disimilarity - elements in 1 but not the other
    difference = tree_counter_1.symmetric_difference(tree_counter_2)

    # we can find the weight of the subtree, by

    str(tree_builder.processed_words["sweet"])


    # their child
    # nodes will be inserted into a priority queue in which the
    # subtrees with the largest weights are always compared
    # first.

    # https://sci-hub.tw/https://ieeexplore.ieee.org/document/1260818
    # Whenever XyDiff finds an exact match between two
    # subtrees, it attempts to propagate the match to the
    # respective parents of the two nodes with the weight of
    # each subtree determining how many levels the matching is
    # propagated.

    # Whenever there is more than one potential
    # candidate for matching, XyDiff uses a few simple
    # heuristic rules to pick one in order to avoid having to
    # perform a full evaluation of the alternatives. This
    # algorithm achieves O(nlogn) complexity in execution time
    # and generates fairly good results in many cases. However,
    # XyDiff cannot guarantee any form of optimal or nearoptimal result because of the greedy rules used in the
    # algorithm.

    pass


if __name__ == "__main__":
    tree_builder = pickleloader("tree_builder_pickled")
    # pprint.pprint([i for i in tree_builder.processed_words])
    # pprint.pprint(str(tree_builder.processed_words["sweet"]))
    #
    # pprint.pprint([str(i) for i in tree_builder.processed_words["sweet"].children])
    pprint.pprint(TreeCounter(tree_builder, tree_builder.processed_words["taste"]))

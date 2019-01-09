from tree_builder import TreeBuilder
import sys
import _pickle as pickle
import pprint


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


def root_children(tree_builder, root_word):
    #get the root word
    root = tree_builder.processed_words[root_word]

    # get its children
    children = root.children
    children_names = [i.name for i in children]
    return children_names

def TreeCounter(tree_builder, root_word, max_depth=5):
    depth_counter = 0
    tree_counter = []

    root_queue = []
    root = root_word
    tree_counter.append(root)
    root_queue += root_children(tree_builder, root_word)

    while depth_counter < max_depth and len(root_queue) != 0:
        root = root_queue.pop(0)
        tree_counter.append(root)
        root_queue + root_children(tree_builder, root)
        depth_counter += 1

    return tree_counter

def similarity_score(tree_counter):
        #similarty  by counting number of same words within 2 different tree_counters
        # disimilarity by counting number of differing words within 2 different tree_counters
    pass


if __name__ == "__main__":
    tree_builder = pickleloader("tree_builder_pickled")
    pprint.pprint([i for i in tree_builder.processed_words])
    print(TreeCounter(tree_builder, "ground"))

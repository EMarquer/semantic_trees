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
    # initialise the start of the tree counter with the first layer consisting of the root_word
    tree_counter = {depth_counter: [root_word]}
    depth_counter+=1

    #maintain a queue of childrens at each level, which we will pop the head of at each step
    children = root_children(tree_builder, root_word)
    depth_queue = {depth_counter:children}
    while depth_counter < max_depth and len(depth_queue) != 0:
        for i in depth_queue.keys():
            tree_counter[depth_counter] = []
            for i2 in depth_queue[i]:
                tree_counter[depth_counter].append(i2)
                children = root_children(tree_builder, i2)

                depth_queue[depth_counter]+= children
            del depth_queue[depth_counter]
            depth_counter += 1

    return depth_queue



def similarity_score(tree_counter_1, tree_counter_2):
    #similarty - elements that are in both trees
    similar = tree_counter_1.union(tree_counter_2)
    # disimilarity - elements in 1 but not the other
    difference = tree_counter_1.symmetric_difference(tree_counter_2)
    pass


if __name__ == "__main__":
    tree_builder = pickleloader("tree_builder_pickled")
    # pprint.pprint([i for i in tree_builder.processed_words])
    print(TreeCounter(tree_builder, "taste"))

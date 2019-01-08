from tree_builder import TreeBuilder
import sys

word = (len(sys.argv) > 1 and sys.argv[1]) or "hello"
context = (len(sys.argv) > 2 and sys.argv[2]) or "hello this is a test"


# function to create a file and store the data in the file
def picklemaker(filename, objectname):
    # open the file for writing
    fileObject = open(filename,'wb')

    # this writes the object a to the
    # file named 'testfile'
    pickle.dump(objectname,fileObject)

    # here we close the fileObject
    fileObject.close()

if __name__ == "__main__":
    tree_builder = TreeBuilder()
    tree_builder.build_word_tree(word, context, 10)

    filename = "tree_builder_{}".format(word)
    picklemaker(filename, tree_builder)

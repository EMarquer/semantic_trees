from tree_builder import TreeBuilder
import sys

word = (len(sys.argv) > 1 and sys.argv[1]) or "hello"
context = (len(sys.argv) > 2 and sys.argv[2]) or "hello this is a test"


if __name__ == "__main__":
    tree_builder = TreeBuilder()
    tree_builder.build_word_tree(word, context, 10)

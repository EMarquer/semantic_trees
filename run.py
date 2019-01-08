import tree_builder

word = "hello"
context = "hello this is a test"


if __name__ == "__main__":
    tree = tree_builder.TreeBuilder()
    tree.build_word_tree(word, context, 10)


from typing import Any, Dict, Optional

from word_tree import Word, Primitive, Node
from primitives import get_primitives_dict


class TreeBuilder():
    # All the primitives.py will be built beforehand
    # That way, we can always refer to the same Primitive object when using a primitive
    primitives: Dict[str, Primitive]

    # All the processed words will be storeed here (as objects), so we can reference them later in the tree without
    # processing them again. By processing, I mean affecting all the children Words & Primitives to a word, we could
    # also say "building one level of the tree"
    # TODO this dictionary can be pickled between uses of the script
    processed_words: Dict[str, Word]

    def __init__(self):
        """ Creates a new instance of a TreeBuilder, use only if you want to reset the processed word set.
        Otherwise, unpickle a already built TreeBuilder.
        """
        self.primitives: Dict[str, Primitive] = get_primitives_dict()
        self.processed_words: Dict[str, Word] = dict()

    def build_word_tree(self, root_word: str, max_depth: Optional[int]=0) -> Node:
        """
        Tree building algorithm using breath-first search.

        :param root_word: the string version of a word
        :param max_depth: the maximum depth for the search
        :return: a Word object representing a word, connected to all the necessary words
        """
        # if the word has already been processed or is a primitive, we return the already processed version
        if root_word in self.processed_words.keys():
            return self.processed_words[root_word]
        elif root_word in self.primitives.keys():
            return self.primitives[root_word]

        # Here are stored the words that we have not processed yet
        # We start with the root of the tree, the first word, in this set.
        # To use a depth criteria to stop the search, we can split it in two lists, one for the current level of the
        # tree, one for the next level
        root_word_ = Word[root_word]
        words_to_process: Dict[str, Word] = dict()
        words_to_process_next_level: Dict[str, Word] = {root_word: root_word_}
        depth = -1

        # I we still have words to process in the next level
        while len(words_to_process_next_level) > 0:
            # we break the loop if the maximal depth is reached
            if max_depth > depth or max_depth < 1: break

            words_to_process = words_to_process_next_level
            words_to_process_next_level: Dict[str, Word] = dict()
            depth += 1

            # processing of every word in the current level
            while len(words_to_process) > 0:
                # we get a word to process
                word_to_process_str, word_to_process = words_to_process.popitem()

                for word in word_to_process.get_definition():

                    # [fail safe] we can add here a checking to verify that a word does not contain itself in its
                    # definition
                    if word_to_process_str == word:
                        pass

                    elif word in self.primitives.keys():
                        word_to_process.children.add(self.primitives[word])

                    elif word in self.processed_words.keys():
                        word_to_process.children.add(self.processed_words[word])

                    # if the word is not a primitive or an already processed word, create it and add it to the words to
                    # process (next layer, if relevant)
                    else:
                        # create the word object
                        word_ = Word(word)

                        # as it has just been created, we add the new word to the words to process
                        words_to_process_next_level[word] = word_

                        # finally, we add the word as a children of currently processed word
                        word_to_process.children.add(word_)

                # once the definition is completely treated, the word is processed, we can add it  to the processed
                # words
                self.processed_words[word_to_process_str] = word_to_process

        return root_word_




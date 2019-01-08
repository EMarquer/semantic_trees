# from __future__ import annotations

from typing import Collection, Set, Any
import dictionary_scrapping

class Node:
    # Type hints for internal variables
    name: str
    children: Set

    def __init__(self, name: str):
        self.name = name
        self.children = set()

    def add(self, child) -> None:
        self.children.add(child)

    def add_all(self, children: Collection) -> None:
        for child in children:
            self.children.add(child)

    def __str__(self) -> str:
        len_ = self.children.__len__()
        children_text = ("no child" if len_ < 1 else
                         "1 child" if len_ == 1 else
                         "{} children".format(len_))
        return "Node \"{}\": {}".format(self.name, children_text)


class Word(Node):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self) -> str:
        len_ = self.children.__len__()
        children_text = ("no child" if len_ < 1 else
                         "1 child" if len_ == 1 else
                         "{} children".format(len_))
        return "Word \"{}\": {}".format(self.name, children_text)

    def get_definition(self) -> Set[str]:
        definitions = dictionary_scrapping.extract_definition(self.name)
        first_definition = definitions["definitions"]["def_1"]['relevant_words']

        return first_definition


class Primitive(Node):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self) -> str:
        return "Primitive \"{}\"".format(self.name)


if __name__ == "__main__":
    from pprint import pprint

    words_str = {
        "something",
        "someone",
        "ask",
        "someone",
        "want",
        "information",
        "speak",
        "write",
        "talk",
        "communicate",
        "use",
        "pen",
        "make",
        "words",
        "create",
        "produce",
        "get",
        "facts",
        "particular",
        "subject",
        "know",
        "express",
        "thought",
        "feelings",
        "knowledge",
        "person",
        "another",
        "animal",
        "tell",
        "opinion",
        "aim",
        "do",
        "machine",
        "tool",
        "method",
        "result",
        "job",
        "work",
        "regularly",
        "earn",
        "money",
        "idea",
        "problem",
        "situation",
        "thought",
        "object",
        "draw",
        "ink",
        "discuss",
        "image",
        "mind"
    }
    primitives_class_str = {
        "Substantives": {"I", "YOU", "SOMEONE", "PERSON", "PEOPLE", "SOMETHING", "THING", "BODY"},
        "Relational substantives": {"KIND", "PART"},
        "Determiners": {"THIS", "THE SAME", "OTHER", "ELSE", "ANOTHER"},
        "Quantifiers": {"ONE", "TWO", "SOME", "ALL", "MUCH", "MANY", "LITTLE", "FEW"},
        "Evaluators": {"GOOD", "BAD"},
        "Descriptors": {"BIG", "SMALL"},
        "Mental predicates": {"THINK", "KNOW", "WANT", "FEEL", "SEE", "HEAR"},
        "Speech": {"SAY", "WORDS", "TRUE"},
        "Actions, events, movement, contact": {"DO", "HAPPEN", "MOVE", "TOUCH"},
        "Location, existence, possession, specification": {"BE", "SOMEWHERE", "THERE IS", "HAVE", "BE", "SOMEONE",
                                                           "SOMETHING"},
        "Life and death": {"LIVE", "DIE"},
        "Time": {"WHEN", "TIME", "NOW", "BEFORE", "AFTER", "A LONG TIME", "A SHORT TIME", "FOR SOME TIME", "MOMENT"},
        "Space": {"WHERE", "PLACE", "HERE", "ABOVE", "BELOW", "FAR", "NEAR", "SIDE", "INSIDE"},
        "Logical concepts": {"NOT", "MAYBE", "CAN", "BECAUSE", "IF"},
        "Intensifier, augmentor": {"VERY", "MORE"},
        "Similarity": {"LIKE", "AS", "WAY"},
    }

    # Flatten the dictionary as a set, to make it usable as a filter
    primitives_str = set()
    for primitive_class in primitives_class_str.values():
        primitives_str |= {primitive_str.lower() for primitive_str in primitive_class}

    """ This chunk does two things:
    - it creates variables for each word, their name being the word itself
      Example: for the word "carrot", it will execute something equivalent to:
      >>> carrot = Word("carrot")
    - it create a different representation for standard words (Word) and primitives (Primitive)"""
    _words = set()
    for word_str in words_str:
        word_str = word_str.lower()
        vars()[word_str] = (Primitive if word_str in primitives_str else Word)(word_str)
        _words.add(vars()[word_str])

    pprint({str(_word) for _word in _words if isinstance(_word, Primitive)})
    pprint({str(_word) for _word in _words if isinstance(_word, Word)})

    """ Two words were considered primitives in the original tree but were not correctly detected, because of one thing:
    they are not "truly" primitives, at least according to the list of primitives used
    "feelings" and "animal"
    it is not truly a problem as both words are defined in the dictionary in a simple way"""

    # --------------

    # Here are examples of how to combine the Nodes to create a tree

    a, b, c, d = Primitive('a'), Primitive('b'), Primitive('c'), Primitive('d')
    e = Word('e')
    f = Word('f')
    x = Node("x")
    y = Node("y")
    z = Node("z")

    primitives = {a, b, c, d}
    nodes = {e, f, x, y, z}

    x.add(y)
    x.add(z)
    y.add(z)
    e.add(f)
    f.add(a)
    f.add(d)
    for node in nodes:
        print(node)
        pprint({str(word_) for word_ in node.children})

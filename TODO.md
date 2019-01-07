# Major steps
1. [x] Find information about theory
2. [ ] **[WIP]** Create tools to build the trees
3. [ ] Build the trees for the selected words (= create the toy corpus)
4. [ ] Compare trees to rate sentences

## Step 2 (Create tools to build the trees) main objectives
1. [x] Create a tool to extract the definition from the web
2. [ ] **[WIP]** Create a tool to select and process the necessary information from the definition
5. [ ] Create a tree representation of words (create the data structure, the necessary classes)
4. [ ] Create a tool to build the tree of a word
3. [ ] Create a tool to store the information about a word locally (using XML)

# TODO
1. Semantic tree example, class and unit test (we call similar procedures "test driven programing")
    1. [ ] Manually create a paper version of the semantic tree of one or two words, containing
        * the relevant words of the first definition (those with the UD tag "NOUN", "VERB", "ADJ", "ADV" or "PART";
        you can use [http://lindat.mff.cuni.cz/services/udpipe/](http://lindat.mff.cuni.cz/services/udpipe/) to get the tags)
        * the "modifiers" of those words ("not", for example)
    2. [ ] Create a class able to represent such a tree in python
    3. [ ] Build the tree for the words in python (create a small script that produce the correct object instance), it will
    serve in the test cases as a target output
    4. [ ] Create the tests for a `build_semantic_tree(word)` function (it does not exist yet), it will serve as a target to
    code the function `build_semantic_tree(word)`

2. Extracting the information from the definition in order to build the tree
    1. Create a single level of the tree from the dictionary data (we consider that we already extracted the data)
        1. [ ] create the info/example 
        2. [ ] create the test 
        3. [ ] create the code
    2. Create the recursive algorithm
        1. [ ] prepare the data for each node of the tree
        2. [ ] store the primitives
        3. [ ] create the test 
        4. [ ] create the code of the algorithm, using the single level builder and the primitives
        * We can use a "word pool" to store a list of all seen words, whatever the step
        * We can use pointers to link all the instance of a word to a single object, avoiding the need to build the 
        complete tree each time
    
3. Connecting everything (from the word query to the semantic tree)
    1. [ ] adapt the processing of the raw HTML to obtain the necessary information to create a single level of the tree
    2. [ ] test the queries for the word we have built semantic tree manually
    
4. Implement a tree distance algorithm

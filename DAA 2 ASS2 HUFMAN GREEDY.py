class Node:
    """A Huffman Tree Node"""

    def __init__(self, freq_, symbol_, left_=None, right_=None):
        # frequency of symbol
        self.freq = freq_

        # symbol name (character)
        self.symbol = symbol_

        # node left of the current node
        self.left = left_

        # node right of the current node
        self.right = right_

        # tree direction (0/1)
        self.huff = ""


def print_nodes(node, val=""):
    """Utility function to print Huffman codes for all symbols in the newly created Huffman tree"""
    # Huffman code for the current node
    new_val = val + str(node.huff)

    # if the node is not an edge node, then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    # if the node is an edge node, then display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} > {new_val}")


# Characters for Huffman tree
chars = ["a", "b", "c", "d", "e", "f"]

# Frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# List containing Huffman tree nodes of characters and frequencies
nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
    # Sort all the nodes in ascending order based on their frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # Pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # Assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # Combine the 2 smallest nodes to create a new node as their parent
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # Remove the 2 nodes and add their parent as a new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print("Characters:", chars)
print("Frequency:", freq)
print("\nHuffman Encoding:")
print_nodes(nodes[0])








































#FIRST EXPLAIN MEE THE CODE LINE BY LINE, THEN WHAT WE HAVE IMPLEMENTED WHY WE NEED IT AND THEN PREPARE QUESTION AND ANSWER
# ChatGPT
# Certainly, let's first explain the code line by line:
#
# python
# Copy code
# class Node:
#     """A Huffman Tree Node"""
#
#     def __init__(self, freq_, symbol_, left_=None, right_=None):
#         # frequency of symbol
#         self.freq = freq_
#
#         # symbol name (character)
#         self.symbol = symbol_
#
#         # node left of the current node
#         self.left = left_
#
#         # node right of the current node
#         self.right = right_
#
#         # tree direction (0/1)
#         self.huff = ""
# This section defines a class called Node, which represents nodes in a Huffman tree. Each node has attributes for frequency (freq), the associated symbol (symbol), links to left and right child nodes (left and right), and a huff attribute to indicate the direction in the tree (0 or 1).
# python
# Copy code
# def print_nodes(node, val=""):
#     """Utility function to print Huffman codes for all symbols in the newly created Huffman tree"""
#     # Huffman code for the current node
#     new_val = val + str(node.huff)
#
#     # if the node is not an edge node, then traverse inside it
#     if node.left:
#         print_nodes(node.left, new_val)
#     if node.right:
#         print_nodes(node.right, new_val)
#
#     # if the node is an edge node, then display its Huffman code
#     if not node.left and not node.right:
#         print(f"{node.symbol} > {new_val}")
# The print_nodes function is defined to print Huffman codes for symbols in a Huffman tree. It takes a node as an argument and a val parameter to track the current Huffman code.
# The function recursively traverses the tree, adding 0 or 1 to val based on the huff attribute of each node. When a leaf node (edge node) is encountered, it prints the symbol and its corresponding Huffman code.
# python
# Copy code
# # Characters for Huffman tree
# chars = ["a", "b", "c", "d", "e", "f"]
#
# # Frequency of characters
# freq = [5, 9, 12, 13, 16, 45]
#
# # List containing Huffman tree nodes of characters and frequencies
# nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]
# This section defines the characters and their corresponding frequencies that you want to encode using Huffman coding.
# The chars list contains characters to be encoded.
# The freq list contains the frequencies (number of occurrences) of these characters.
# A list of Node objects (nodes) is created using a list comprehension, where each Node object represents a character and its frequency.
# python
# Copy code
# while len(nodes) > 1:
#     # Sort all the nodes in ascending order based on their frequency
#     nodes = sorted(nodes, key=lambda x: x.freq)
#
#     # Pick 2 smallest nodes
#     left = nodes[0]
#     right = nodes[1]
#
#     # Assign directional value to these nodes
#     left.huff = 0
#     right.huff = 1
#
#     # Combine the 2 smallest nodes to create a new node as their parent
#     newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
#
#     # Remove the 2 nodes and add their parent as a new node among others
#     nodes.remove(left)
#     nodes.remove(right)
#     nodes.append(newNode)
# In this part of the code, a while loop constructs the Huffman tree.
# The loop continues until there is only one node left in the nodes list.
# In each iteration, the nodes list is sorted in ascending order based on the freq attribute.
# The two nodes with the smallest frequencies are selected as left and right.
# These two nodes are assigned directional values (0 and 1) using the huff attribute.
# A new parent node (newNode) is created by combining the two smallest nodes.
# The two smallest nodes are removed from the nodes list, and the new parent node is added to it.
# python
# Copy code
# print("Characters:", chars)
# print("Frequency:", freq)
# print("\nHuffman Encoding:")
# print_nodes(nodes[0])
# Finally, this part of the code prints the characters and their frequencies.
# It then calls the print_nodes function to print the Huffman codes for the characters. The nodes[0] argument represents the root of the Huffman tree.
# Now, let's discuss what we have implemented and why we need it:
#
# What We Have Implemented:
#
# The code implements the Huffman coding algorithm, which is a variable-length prefix coding technique used for lossless data compression.
# It constructs a Huffman tree based on character frequencies and assigns Huffman codes to each character.
# Why We Need It:
#
# Huffman coding is used to efficiently compress data, where frequently occurring characters are assigned shorter codes, and less frequent characters are assigned longer codes.
# Huffman coding is widely used in data compression, including in file compression formats like ZIP and in various data transmission and storage applications.
# Here are 20 questions and answers based on the code:
#
# What is Huffman coding, and how does it work?
#
# Answer: Huffman coding is a variable-length prefix coding technique used for data compression. It assigns shorter codes to frequently occurring characters and longer codes to less frequent characters. It works by constructing a Huffman tree.
# What is the purpose of the Node class in this code?
#
# Answer: The Node class represents nodes in a Huffman tree, storing information about symbol frequency, the symbol itself, and tree structure.
# How are Huffman codes assigned to characters in Huffman coding?
#
# Answer: Huffman codes are assigned based on the structure of a Huffman tree. Characters closer to the root have shorter codes.
# What does the print_nodes function do in this code?
#
# Answer: The print_nodes function prints Huffman codes for all symbols in the Huffman tree by recursively traversing the tree.
# How is the direction (0 or 1) determined for nodes in the Huffman tree?
#
# Answer: The huff attribute is used to determine the direction. A node with huff equal to 0 is on the left, and a node with huff equal to 1 is on the right.
# Why is it necessary to sort the nodes in ascending order based on frequency in each iteration of the loop?
#
# Answer: Sorting nodes ensures that the two smallest frequency nodes are selected to create the parent node, maintaining the property of a Huffman tree.
# What happens to the two smallest nodes (left and right) in each iteration of the loop?
#
# Answer: They are combined to create a new parent node, and directional values (0 and 1) are assigned to them.
# How are the two smallest nodes removed from the nodes list?
#
# Answer: The remove method is used to remove them from the list.
# What is the purpose of the newNode variable in the loop?
#
# Answer: It represents the newly created parent node for the two smallest nodes.
# What is the significance of the nodes list after the loop completes?
#
# Answer: After the loop completes, the nodes list contains only one node, which is the root of the Huffman tree.
# What data structure is used to store character frequencies (freq) and characters (chars)?
#
# Answer: Lists are used to store character frequencies and characters.
# What is the significance of character frequencies in Huffman coding?
#
# Answer: Character frequencies determine the length of Huffman codes, with more frequent characters having shorter codes.
# How are Huffman codes printed for the characters at the end of the code?
#
# Answer: The print_nodes function is called with the root node of the Huffman tree to print the codes.
# How does the code handle the traversal of the Huffman tree to print codes?
#
# Answer: The print_nodes function recursively traverses the tree and keeps track of the current Huffman code.
# What does the val parameter represent in the print_nodes function?
#
# Answer: The val parameter represents the current Huffman code being constructed during tree traversal.
# Why are Huffman codes important in data compression?
#
# Answer: Huffman codes allow for efficient representation of data, reducing storage space and transmission time.
# What is the time complexity of constructing a Huffman tree using this code?
#
# Answer: The time complexity is O(n log n), where n is the number of characters.
# How are Huffman codes used in decoding compressed data?
#
# Answer: Huffman codes are used to map compressed binary data back to the original characters during decoding.
# Can Huffman coding handle non-textual data, such as images or audio?
#
# Answer: Yes, Huffman coding can be applied to any data where symbols and their frequencies can be defined.
# What are some applications of Huffman coding in real life?
#
# Answer: Huffman coding is used in file compression formats (e.g., ZIP), data transmission protocols, image and video compression, and various data storage and compression applications.
# These questions and answers should provide a comprehensive understanding of the code and its implications. If you have more specific questions or need further clarification, please feel free to ask.
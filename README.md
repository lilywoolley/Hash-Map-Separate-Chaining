# Hash-Map-Separate-Chaining

This is an implementation of a hash map data structure that uses separate chaining for collisions. This implementation utilizes a basic dynamic array that contains a linked list object at each index. If a key's hashed index is the same as another key, it will simply add that new key value pair to the list. If the key is exactly the same as one already stored in the list, it will update the value attributed to it.

The hash_map_sc.py file has tests built in, just run the file in a terminal to see the results!

NOTE: File will not run without the a6_include.py file.

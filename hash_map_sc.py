# Name: Lily Woolley
# OSU Email: woolleyw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 3/11/22
# Description: Implementation of a hash map data structure with separate chaining


from a6_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Overrides object's string method
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Empties the hash map of all key value pairs
        """
        #Clears each bucket individually, and reduces the size accordingly
        for i in range(self.buckets.length()):
            self.buckets[i] = LinkedList()
        
        self.size = 0


    def get(self, key: str) -> object:
        """
        Returns the value attributed to a key
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        list = self.buckets.get_at_index(index) 
        node = list.contains(key)
        #If the node doesn't have the key returns false
        if node == None:
            return None
        #If the node does have the key, returns the value
        else:
            return node.value

    def put(self, key: str, value: object) -> None:
        """
        Puts a new value into the list at the appropriate key or overwrites if the key already existed
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        list = self.buckets.get_at_index(index)
        #If list is empty, insert the key value pair and increments the size
        if list.length() == 0:
            list.insert(key, value)
            self.size += 1
        #If the key is already in the list, updates the value attributed to it
        elif list.contains(key) != None:
            list.remove(key)
            list.insert(key, value)
        #Otherwise, inserts the key and increments the size
        else:
            list.insert(key, value)
            self.size += 1
        

    def remove(self, key: str) -> None:
        """
        Takes some key, checks if that key exists in the hash map, removes it if it does
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        list = self.buckets.get_at_index(index)
        node = list.contains(key)
        #If the key does not exist, does nothing
        if node == None:
            return
        #If the key does exist, removes the node with that key
        else:
            list.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns true if there is nothing in the list at the key
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        list = self.buckets.get_at_index(index)
        #If the list has something in it, returns True otherwise False
        if list.contains(key) != None:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        Returns the number of buckets that did not contain a linked list
        """
        i = self.capacity
        j = 0
        #Runs through entire array
        while i > 0:
            i -= 1
            list = self.buckets.get_at_index(i)
            #Checks if the linked list is empty, increments j if true
            if list.length() == 0:
               j += 1 

        return j
            

    def table_load(self) -> float:
        """
        Calculates and returns the current table load
        """
        return self.size / self.capacity
         

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of a pre-existing hash map and rehashes all keys stored within
        """
        if new_capacity < 1:
            return None
        
        i = self.capacity
        resizedArray = HashMap(new_capacity, self.hash_function)
        
        while i > 0:
            i -= 1
            list = self.buckets.get_at_index(i)
            #If the list is empty, checks the next index in the array
            if list.length() != 0:
                #Iterates through the list finding all the key and value pairs and rehashes them with the new capacity
                for node in list:                   
                    key = node.key
                    value = node.value
                    resizedArray.put(key, value)     
        #Once looping is done, changes the capacity, and sets the data
        self.capacity = new_capacity
        self.buckets = resizedArray.buckets
    


    def get_keys(self) -> DynamicArray:
        """
        Returns a dynamic array containing all keys stored within the hash map
        """
        i = self.capacity
        keyArray = DynamicArray()
        
        while i > 0:
            i -= 1
            list = self.buckets.get_at_index(i)
            #If the list is empty, checks the next index in the array
            if list.length() != 0:
                #Add each key to the returning array per node in the list
                for node in list:
                    key = node.key
                    keyArray.append(key)
        
        return keyArray
        


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

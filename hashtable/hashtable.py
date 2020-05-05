class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """

        key_bytes = str(key).encode()
        total = 0

        for x in key_bytes:
            total += x
            total &= 0xffffffffffffffff
        return total

    def djb2(self, key):

        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        key_bytes = str(key).encode()
        total = 0

        for x in key_bytes:
            total += x
            total &= 0xffffffffffffffff
        return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """

        index =  self.hash_index(key)
        new_val = HashTableEntry(key, value)
        cur = self.storage[index]
        if cur is not None:
            #overwriting value
            self.storage[index] = new_val
            self.storage[index].next = cur
        else:
            self.storage[index] = HashTableEntry(key, value)
        return self.storage[index].value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]
        prev = None
        
        while cur.next is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
                prev = cur
            cur = cur.next
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index =  self.hash_index(key)
        cur = self.storage[index]



        while cur != None:
            if cur.key == key:
                return cur.value

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        self.storage = self.storage + [None] * self.capacity
        return self.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

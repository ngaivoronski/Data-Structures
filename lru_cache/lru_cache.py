from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.orderList = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            self.orderList.move_to_end(self.storage[key])
            return self.storage[key].value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key is in storage
        if key in self.storage.keys():
            # get the node from storage
            node_to_update = self.storage[key]
            # move it to the end
            self.orderList.move_to_end(node_to_update)
            # set the tail value to the new value
            self.orderList.tail.value = value
            # set the value of storage to the new tail
            self.storage[key] = self.orderList.tail

        # if the number of nodes are within the limit
        elif self.nodes < self.limit:
            # create a node and add it to the tail
            new_node = self.orderList.add_to_tail(value)
            # set the key to the new node
            self.storage[key] = new_node
            self.nodes += 1
        
        # if the limit of nodes has been reached
        else:
            # get the head node
            value_to_remove = self.orderList.head
            # remove the head from the orderList
            self.orderList.remove_from_head()
            # remove the head value from storage
            self.storage = {k:v for k, v in self.storage.items() if v != value_to_remove}
            # create a node and add it to the tail
            new_node = self.orderList.add_to_tail(value)
            # set the key to the new node
            self.storage[key] = new_node



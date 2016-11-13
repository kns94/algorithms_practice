'''
Implementing LRU cache
'''

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = []
        self.hash_map = {}
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hash_map:
            index = self.cache.index(key)
            del self.cache[index]
            self.cache.append(key)
            return self.hash_map[key]
        else:
            return -1

    """
    def swap_elements(self, index):
        '''
        Swap elements from index to end of list
        '''
        i = index
        while i < len(self.cache) - 1:
            nxt = self.cache[i + 1]
            self.cache[i + 1] = self.cache[i]
            self.cache[i] = nxt
            i += 1
    """

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
           
        '''
        Add element
        '''
        if key not in self.hash_map:
            self.hash_map[key] = value

            if len(self.cache) < self.capacity:
                self.cache.append(key)
            else:
                del self.hash_map[self.cache[0]]
                del self.cache[0]
                self.cache.append(key)
        else:
            '''
            Remove least recent
            '''
            self.hash_map[key] = value
            index = self.cache.index(key)
            del self.cache[index]
            self.cache.append(key)
   
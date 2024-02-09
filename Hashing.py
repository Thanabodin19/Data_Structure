class HashTable:
    def __init__(self):
        self.size = 7
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        strt_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = strt_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == strt_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':

    h = HashTable()
    h[6] = "อรุณ"
    h[21] = "เมฆา"
    h[37] = "อัสนี"
    h[1] = "นภา"
    h[45] = "พิรุณ"
    h[69] = "สายหมอก"
    h[5] = "วายุ"



    print(h.slots)
    print(h.data)
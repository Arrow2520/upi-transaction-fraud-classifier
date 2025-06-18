MAX_HASHTABLE_size = 4096


def get_index(data_list, a_string):
    result = 0
    for a_char in a_string:
        a_num = ord(a_char)
        result += a_num
    list_index = result % len(data_list)
    return list_index


class BasicHashTable:

    def __init__(self, max_size=MAX_HASHTABLE_size):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')


# The next function is to handle collisions using linear probing

def get_valid_index(data_list, key):
    idx = get_index(data_list, key)
    while True:
        kv = data_list[idx]
        if kv is None:
            return idx
        k, v = kv
        if k == key:
            return idx
        idx += 1
        if idx == len(data_list):
            idx = 0


class ProbingHashTable:

    def __init__(self, max_size=MAX_HASHTABLE_size):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


# Create a new hash table
probing_table = ProbingHashTable()
probing_table.insert('listen', 99)
print(probing_table.find('listen') == 99)
probing_table.insert('silent', 200)
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)


MAX_HASH_TABLE_SIZE  = 4096


class HashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data = [None] * max_size
        self.count = 0

    def get_valid_index(self, key):
        idx = hash(key) % len(self.data)
        while True:
            kv = self.data[idx]
            if kv is None:
                return idx
            k, v = kv
            if k == key:
                return idx
            idx += 1
            if idx == len(self.data):
                idx = 0

    def __getitem__(self, key):
        idx = self.get_valid_index(self.data, key)
        kv = self.data[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def __setitem__(self, key, value):
        idx = self.get_valid_index(self.data, key)
        self.data[idx] = key, value

    def __iter__(self):
        return (x for x in self.data if x is not None)

    def __len__(self):
        return self.count

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format('\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)
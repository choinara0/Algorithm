# 기본 hashTable(충돌알고리즘 x)
class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_func(self, key):
        return key%8

    def insert(self, key, value):
        hash_value = self.hash_func(hash(key))
        self.hash_table[hash_value] = value

    def read(self, key):
        hash_value = self.hash_func(hash(key))
        return self.hash_table[hash_value]

    def print(self):
        print(self.hash_table)

ht = HashTable()
ht.insert(1, 'one')
ht.print()
ht.insert(2, 'two')
ht.print()
ht.insert('nara', 'choi')
ht.print()
# Chaining 기법을 활용한 hash table
class hashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_func(self, key):
        return key % 8

    def insert(self, key, value):
        gen_key = hash(key) #내장함수 hash로 해쉬 키 생성
        hash_value = self.hash_func(gen_key) #hash_func를 통해 해쉬 키에 맞는 해쉬 값 생성

        if self.hash_table[hash_value] != 0: #hash value index를 사용하고 있어서 충돌이 발생하는 경우
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key: #이미 같은 키 값이 존재하면 value를 교체한다.
                    self.hash_table[hash_value][i][1] = value
                    return

            self.hash_table[hash_value].append([gen_key, value]) #같은 키 값이 존재하지 않는다면 [key, value] 쌍을 해당 index에 insert

        else:
            self.hash_table[hash_value] = [[gen_key, value]] # hash_value index를 사용하고 있지 않아서 충돌이 발생하지 않을 때

    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)

        if self.hash_table[hash_value] != 0:
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    return self.hash_table[hash_value][i][1]

            return None
        else:
            return None

    def print(self):
        print(self.hash_table)

ht2 = hashTable()
ht2.insert(1, 'one')
ht2.print()
ht2.insert(2, 'two')
ht2.print()
ht2.insert('nara', 'choi')
ht2.print()


#Close Hashing 기법을 활용한 hash table

class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_func(self, key):
        return key%8

    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)

        if self.hash_table[hash_value] != 0: #hash value index를 사용하고 있어서 충돌이 발생하는 경우
            for i in range(hash_value, len(self.hash_table)): # 해당 Index부터 마지막 index까지 for문을 돈다.
                if self.hash_table[i] == 0: #해당 index가 비어있으면 [key, value]를 insert
                    self.hash_table[i] = [gen_key, hash_value]
                    return
                elif self.hash_table[i][0] == gen_key: #해당 index에 이미 같은 키 값이 존재하면 덮어쓴다.
                    self.hash_table[i][1] = value
                    return
        else:
            self.hash_table[hash_value] = [gen_key, value]


    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)

        if self.hash_table[hash_value] != 0:
            for i in range(hash_value, len(self.hash_table)):
                if self.hash_table[i] == 0:
                    return None
                elif self.hash_table[i][0] == gen_key:
                    return self.hash_table[i][1]

        else:
            return None

    def print(self):
        print(self.hash_table)

ht3 = HashTable()
ht3.insert(1, 'one')
ht3.print()
ht3.insert(2, 'two')
ht3.print()
ht3.insert('nara', 'choi')
ht3.print()
ht3.insert(4, 'four')
ht3.insert(5, 'five')
ht3.insert(6, 'six')
ht3.print()

# 공간을 확장하는 방법

class HashTable:
    def __init__(self, n):
        self.n = n
        self.hash_table = list([0 for i in range(8)])

    def hash_func(self, key):
        return key % self.n

    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)

        if self.hash_table[hash_value] != 0: #hash value index를 사용하고 있어서 충돌이 발생하는 경우
            for i in range(hash_value, len(self.hash_table)): # 해당 Index부터 마지막 index까지 for문을 돈다.
                if self.hash_table[i] == 0: #해당 index가 비어있으면 [key, value]를 insert
                    self.hash_table[i] = [gen_key, hash_value]
                    return
                elif self.hash_table[i][0] == gen_key: #해당 index에 이미 같은 키 값이 존재하면 덮어쓴다.
                    self.hash_table[i][1] = value
                    return
        else:
            self.hash_table[hash_value] = [gen_key, value]


    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)

        if self.hash_table[hash_value] != 0:
            for i in range(hash_value, len(self.hash_table)):
                if self.hash_table[i] == 0:
                    return None
                elif self.hash_table[i][0] == gen_key:
                    return self.hash_table[i][1]

        else:
            return None

    def print(self):
        print(self.hash_table)

ht4 =
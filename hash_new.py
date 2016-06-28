class hashmap():
    def __init__(self,size):
        self.size=size
        self.map=[None]*size

    def get_hash(self,key):
        hash=0
        for char in str(key):
            hash+=ord(char)
        return hash%self.size

    def add(self,key,value):
        hash_value=self.get_hash(key)
        l=[key,value]

        if self.map[hash_value]==None:
            self.map[hash_value]=list(l)
            return True
        else:
            for pair in self.map[hash_value]:
                if pair[0]==key:
                    pair[1]=value
                    return True

                self.map[hash_value].append(l)
                return True

    def get(self,key):
        hash_value=self.get_hash(key)

        if self.map[hash_value] is not None:
            for pair in self.map[hash_value]:
                if pair[0]==key:
                    return pair[1]

        return None
    def delete(self,key):
        hash_value=self.get_hash(key)
        if self.map[hash_value] is None:
            return False
        for i in range(0,len(self.map[hash_value])):
            if self.map[hash_value][i][0]==key:
                self.map[hash_value].pop(i)
                return True

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))
            

a=hashmap(5)
a.add('sheetal','5865555')
a.add('shreyu','9999')
a.add('sangeeta','370')

a.print()
a.get('sangeeta')

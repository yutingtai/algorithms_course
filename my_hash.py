class Dictionary:
    def __init__(self):
        self.capacity = 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.count = 1

    def insert(self, key, value):
        if self.count == self.capacity:
            self.capacity *= 2
            old_bucket = self.buckets
            self.buckets = [[] for _ in range(self.capacity)]
            for bucket in old_bucket:
                for item in bucket:
                    h = hash(item[0]) % self.capacity
                    self.buckets[h].append(item)

        h = hash(key) % self.capacity
        self.buckets[h].append((key, value))
        self.count += 1

    def find(self, key):
        h = hash(key) % self.capacity
        for item in self.buckets[h]:
            if hash(key) == hash(item[0]) and key == item[0]:
                return item[1]


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name) + hash(self.age)

    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name and other.age == self.age


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name) + hash(self.age)

    def __eq__(self, other):
        return isinstance(other, Dog) and other.name == self.name and other.age == self.age


def main():
    peter = Person("Peter", 29)
    patrik = Person("Patrik", 28)
    happy = Dog("Happy", 4)
    lucky = Dog("Lucky", 3)
    mydict = Dictionary()
    mydict.insert(peter, happy)
    mydict.insert(patrik, lucky)
    print(mydict.find(patrik).name)


if __name__ == '__main__':
    main()

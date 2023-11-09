class People:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_properties(self):
        return "People(name: %s, age: %d)" % (self._name, self._age)

    def __eq__(self, other):
        if not isinstance(other, People):
            raise Exception("Type error")
        return self._name == other._name and self._age == other._age


if __name__ == '__main__':
    p1 = People("Gavin Jin", 22)
    print(p1)
    p2 = People("Gavin Jin", 22)
    print(p2)
    print(p1 == p2)

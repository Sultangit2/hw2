class Cat:
    tail = True

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def meow(self):
        print(self._name, 'meows')

    def __str__(self):
        return f'name is {self._name}\n' \
               f'age is {self.age}'

    def __len__(self):
        return len(self._name)

    def _x2(self):
        self.age *= 9
        print(self)

    def x(self):
        self._x2()

cat3 = Cat('eric',3)
cat3.name

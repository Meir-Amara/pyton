class Animal :
    def __init__(self,num_of_legs) :
        self.num_of_legs=num_of_legs

    def eat(self):
        print("Animal is eating")



class Zebra (Animal):
    def __init__(self, num_of_strips,num_of_legs):
        self.num_of_strips=num_of_strips

        super().__init__(num_of_legs)

    def print_data(self):   
        data = dict({'num_of_legs':self.num_of_legs,'num_of_strips':self.num_of_strips})
        print(data)

    def eat(self):
        print("Zebra is eating")



class Monkey(Animal):
    def __init__(self,color,num_of_legs):
        self.num_of_legs=num_of_legs
        self.color=color
    def eat(self):
        print("monkey is eating")

    def print_data(self):   
        data = dict({'num_of_legs':self.num_of_legs,'color':self.color})
        print(data)


class Chimpanzee(Monkey):
    def __init__(self, color, num_of_legs):
        self.height="150cm"
        super().__init__(color, num_of_legs)
    def print_data(self):
        data = dict({'num_of_legs':self.num_of_legs,'color':self.color,'height':self.height})
        print(data)

class Zoo (Animal):
    def __init__(self):
        self.animals=list()
    def add_animals(self,animal):
        self.animals.append(animal)

    def count_animals(self):
        print(len(self.animals))

    def feed(self):
        for animal in self.animals:
            animal.eat()

zoo=Zoo()
zebra=Zebra(180,4)
chimpanzee=Chimpanzee("black",2)
# chimpanzee.print_data()

zoo.add_animals(chimpanzee)
zoo.add_animals(zebra)
print(zoo.animals)
zoo.count_animals()
zoo.feed()
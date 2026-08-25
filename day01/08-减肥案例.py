# 需求
# 小明同学体重 100kg
# 每次跑步一次,减少 0.5kg
# 每当大吃大喝一次,增加 2kg
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} 本来的体重是 {self.weight} kg'

    def run(self):
        self.weight -= 0.5
        print(f'{self.name} 跑步后的体重是 {self.weight} kg')

    def eat(self):
        self.weight += 2
        print(f'{self.name} 大吃大喝后的体重是 {self.weight} kg')


if __name__ == '__main__':
    weight = Person('小明', 100)
    print(weight)

    weight.run()
    weight.run()
    weight.eat()
    weight.eat()

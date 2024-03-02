"""Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. 
Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини. Реалізуйте також метод класу say. 
При реалізації методу можна використати оператор pass, поки що головне - це визначення, а не конкретна реалізація.
"""
class Animal:
    def __init__(self, nickname, weight) -> None:
        self.nickname = nickname
        self.weight = weight
    
    def say(self):
        print('myau')
    
animal = Animal(nickname='Bars', weight='3 kg')
print(animal.nickname)
print(animal.weight)
print(animal.say())

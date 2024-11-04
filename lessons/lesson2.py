# import lesson1
# from lesson1 import Person
#
# person_test = Person("Arzybek", "25", "Bishkek")
#
# person_test.introduce()


# Принципы ООП

# Наследование: позволяет одному классу (производному) унаследовать свойства и методы другого класса (базового),
#    расширяя или изменяя их. Наследование способствует повторному использованию кода и созданию иерархии классов.

# Полиморфизм: предоставляет возможность объектам разных классов обрабатывать одно и то же сообщение по-разному.
#   С помощью полиморфизма можно создавать гибкие интерфейсы, работающие с разными типами объектов,
#    что повышает гибкость и масштабируемость кода.

# Инкапсуляция: предполагает объединение данных и методов, работающих с этими данными, в единое целое — объект.
#   Это позволяет скрыть внутреннее устройство объекта и защитить данные от прямого доступа и изменений извне.


# Абстракция: этот принцип позволяет выделить ключевые характеристики объектов, скрывая детали их реализации.
#    Благодаря абстракции, можно сосредоточиться на общих свойствах и поведении объектов, игнорируя излишние детали.

# Базовый\Супер\Родительский\
class Hero:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health


    def introduce(self):
        return f"Я {self.name}, мое здоровье : {self.health} "

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие: делает ход\n"



class Mage(Hero):

    def __init__(self, name, health=100, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание! \n Огненый шар {self.mana}"
        else:
            return f"{self.name} недостаточно маны для заклинания!"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()

        return f"{base_action}, {spell_result}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())

mage = Mage("Гендальф")

hero_action(mage)


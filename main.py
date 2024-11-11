from lessons import lesson1


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"

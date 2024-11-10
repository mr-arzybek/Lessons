from main import Hero


class Warrior(Hero):

    def __init__(self, name, health, shield = 50, sword = 30):
        super().__init__(name, health)
        self.shield = shield
        self.sword = sword

    def defence(self):
        if self.shield >= 2:
            self.shield -= 1
            return f"{self.name} you succesfully defenced \n you have {self.shield} endurance left "
        elif self.shield == 1:
            self.shield -= 1
            return f"{self.name} you succesfully defenced \n however you broke your shield "
        else:
            return f"you broke your shield"

    def atack(self):
        if self.shield >= 1 and self.health >= 100:
            new_damage = self.sword * 0.7
            return f"{self.name} you atacked \n you damaged for {new_damage} points"
        elif self.shield >= 1 and self.health <= 100:
            new_damage = self.sword * 1.3
            return f"{self.name} you atacked , you are getting angry \n you damaged for {new_damage} points"
        else:
            new_damage = self.sword * 2
            return f"{self.name} you are in BERSERK MODE \n you damaged for {new_damage} points"

    def action(self):
        base_action = super().action()
        special_result = self.defence()
        special_result2 = self.atack()
        return f"{base_action}, {special_result} and {special_result2}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


Guts = Warrior("Adil", 99, 1 , 30)

hero_action(Guts)
Guts.action()
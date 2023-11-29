"""
Модуль, який містить класи Fish і Aquarium.
"""

class Fish:
    """
    Клас, що представляє рибу.
    """

    def __init__(self, name, age, species, *args):
        self.name = name
        self.age = age
        self.species = species
        self.size = args[0]
        self.preferred_food = args[1]
        self.is_aggressive = args[2]
        self.needed_space = args[3]

    def __str__(self):
        return f"Рибка {self.name} {self.age} років"

    def __repr__(self) -> str:
        pass

class Aquarium:
    """
    Клас, що представляє акваріум.
    """

    def __init__(self, total_volume):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.aggressive_fish_list = []  # Окремий список для агресивних риб
        self.non_aggressive_fish_list = []  # Окремий список для неагресивних риб

    def add_fish(self, fish):
        """
        Додає рибу до відповідного списку акваріума.
        """
        if fish.is_aggressive:
            # Перевірка, чи є вільне місце для агресивної риби
            if self.free_space >= fish.needed_space:
                self.aggressive_fish_list.append(fish)
                self.free_space -= fish.needed_space
                print(f"{fish.name} (агресивна) додана до акваріума для агресивних риб.")
            else:
                print(f"Недостатньо місця для {fish.name} (агресивна) в акваріумі.")
        else:
            # Перевірка, чи є вільне місце для неагресивної риби
            if self.free_space >= fish.needed_space:
                self.non_aggressive_fish_list.append(fish)
                self.free_space -= fish.needed_space
                print(f"{fish.name} додана до акваріума для неагресивних риб.")
            else:
                print(f"Недостатньо місця для {fish.name} в акваріумі.")

    def get_top_3_fish(self, fish_list):
        """
        Виводить топ-3 риби за розміром.
        """
        sorted_fish = sorted(fish_list, key=lambda x: x.size, reverse=True)
        top_3_fish = sorted_fish[:3]
        print("Топ-3 риби в акваріумі:")
        for fish in top_3_fish:
            print(f"{fish.name} - {fish.size} cm")
        return [f"{fish.name} - {fish.size} cm" for fish in top_3_fish]


# Приклад використання класів:

def main():
    """
    main function
    """
    aquarium1 = Aquarium(10)
    fish1 = Fish("Немо", 2, "Клоун", 5, "Планктон", False, 1)
    fish2 = Fish("Шарки", 5, "Великий білий акула", 200, "Риба", True, 8)
    fish3 = Fish("Голді", 1, "Золота рибка", 3, "Пластівці", False, 0.5)

    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish2)
    aquarium1.add_fish(fish3)

    aquarium1.get_top_3_fish(aquarium1.non_aggressive_fish_list)

    aquarium2 = Aquarium(5)
    fish4 = Fish("Баблз", 3, "Кульчастий риба", 1, "Кільчасті", True, 1.5)
    fish5 = Fish("Фугу", 1.5, "Морська риба", 1.3, "Листя", False, 0.8)
    fish6 = Fish("Піранья", 3, "Косар", 1, "М'ясо", True, 1)
    fish7 = Fish("dfjsdkf", 4, "Морська риба", 1.7, "Листя", False, 1)

    aquarium2.add_fish(fish4)
    aquarium2.add_fish(fish5)
    aquarium2.add_fish(fish6)
    aquarium2.add_fish(fish7)

    aquarium2.get_top_3_fish(aquarium2.aggressive_fish_list)

if __name__ == "__main__":
    main()

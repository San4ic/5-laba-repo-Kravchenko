class Fish:
    def __init__(self, name, age, species, size, preferredFood, isAggressive, neededSpace):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferredFood = preferredFood
        self.isAggressive = isAggressive
        self.neededSpace = neededSpace

class Aquarium:
    def __init__(self, totalVolume):
        self.totalVolume = totalVolume
        self.freeSpace = totalVolume
        self.aggressiveFishList = []  # Окремий список для агресивних риб
        self.nonAggressiveFishList = []  # Окремий список для неагресивних риб

    def addFish(self, fish):
        if fish.isAggressive:
            # Перевірка, чи є вільне місце для агресивної риби
            if self.freeSpace >= fish.neededSpace:
                self.aggressiveFishList.append(fish)
                self.freeSpace -= fish.neededSpace
                print(f"{fish.name} (aggressive) added to the aggressive aquarium.")
            else:
                print(f"Not enough space for {fish.name} (aggressive) in the aquarium.")
        else:
            # Перевірка, чи є вільне місце для неагресивної риби
            if self.freeSpace >= fish.neededSpace:
                self.nonAggressiveFishList.append(fish)
                self.freeSpace -= fish.neededSpace
                print(f"{fish.name} added to the non-aggressive aquarium.")
            else:
                print(f"Not enough space for {fish.name} in the aquarium.")

    def getTop3Fish(self, fishList):
        sortedFish = sorted(fishList, key=lambda x: x.size, reverse=True)
        top3Fish = sortedFish[:3]
        print("Top 3 fish in the aquarium:")
        for fish in top3Fish:
            print(f"{fish.name} - {fish.size} cm")

# Пример використання класів:

def main():
    aquarium1 = Aquarium(10)
    fish1 = Fish("Nemo", 2, "Clownfish", 5, "Plankton", False, 1)
    fish2 = Fish("Sharky", 5, "Great White Shark", 200, "Fish", True, 8)
    fish3 = Fish("Goldie", 1, "Goldfish", 3, "Flakes", False, 0.5)

    aquarium1.addFish(fish1)
    aquarium1.addFish(fish2)
    aquarium1.addFish(fish3)

    aquarium1.getTop3Fish(aquarium1.nonAggressiveFishList)

    aquarium2 = Aquarium(5)
    fish4 = Fish("Bubbles", 3, "Pufferfish", 1, "Crustaceans", True, 1.5)
    fish5 = Fish("Fugu", 1.5, "Seefish", 1.3, "leefs", False, 0.8)
    fish6 = Fish("Piranha", 3, "Kilingfish", 1, "Meat", True, 1)
    fish7 = Fish("dfjsdkf", 4, "Seefish", 1.7, "leefs", False, 1)

    aquarium2.addFish(fish4)
    aquarium2.addFish(fish5)
    aquarium2.addFish(fish6)
    aquarium2.addFish(fish7)

    aquarium2.getTop3Fish(aquarium2.aggressiveFishList)

if __name__ == "__main__":
    main()

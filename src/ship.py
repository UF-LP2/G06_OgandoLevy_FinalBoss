class Ship:
    def __init__(self, draft, crew):
        self.crew = crew
        self.draft = (1.5 * self.crew) + draft

    def is_worth_it(self):
        """try:"""
        peso = self.draft - (self.crew * 1.5)
        if peso <= 20:
            raise ValueError("No merece ser saqueado")
        else:
            print("Merece ser saqueado")
            return True
        """except ValueError as error:
                  print(error)"""


class Cruise (Ship):
    def __init__(self, passengers, draft, crew):
        Ship.__init__(self,draft,crew)
        self.passengers = passengers
        self.draft = (2.25 * passengers) + draft

    def is_worth_it(self):
        """try:"""
        peso = self.draft - (self.crew * 1.5) - (self.passengers * 2.25)
        if peso <= 20:
            raise ValueError("No merece ser  saqueado")
        else:
            print("Merece ser saqueado")
            return True
        """except ValueError as error:
           print(error)"""

class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        Ship.__init__(self, draft, crew)
        self.cargo = cargo
        self.quality = quality
        if self.quality == 1:
            self.draft = 3.5 + draft
        elif self.quality == 0.5:
            self.draft = 2 + draft
        elif self.quality == 0.25:
            self.draft = 0.5 + draft
        else:
            raise ValueError("Something else went wrong")

    def is_worth_it(self):
        """try:"""
        peso = self.draft - (self.crew * 1.5)
        if peso <= 20:
            raise ValueError("No merece ser  saqueado")
        else:
            print("Merece ser saqueado")
            return True
        """except ValueError as error:
            print(error)"""

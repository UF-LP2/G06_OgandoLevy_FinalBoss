class Ship:
    def __init__(self, draft, crew):
        self.crew = crew
        self.draft = (1.5 * self.crew) + draft

    def Convertidor(valor) -> float:
        try:
            aux = float(valor)
        except ValueError as e:
            print(e.args)
        else:
            if aux >= 0:
                return aux
        raise ValueError("El valor ingresado no es valido")
    def is_worth_it(self):
        """try:"""
        peso = Ship.Convertidor(self.draft) - (Ship.Convertidor(self.crew) * 1.5)
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
        peso = Ship.Convertidor(self.draft) - (Ship.Convertidor(self.crew) * 1.5) - (Ship.Convertidor(self.passengers) * 2.25)
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
    def is_worth_it(self):
        cargo_aux_val = 0
        if Ship.Convertidor(self.quality) == 1:
            cargo_aux_val = 3.5
        elif Ship.Convertidor(self.quality) == 0.5:
            cargo_aux_val = 2
        elif Ship.Convertidor(self.quality) == 0.25:
            cargo_aux_val = 0.5
        else:
            raise ValueError("Something else went wrong")

        peso = Ship.Convertidor(self.draft) - Ship.Convertidor(self.crew * 1.5) - Ship.Convertidor(self.crew * cargo_aux_val)
        if peso <= 20:
            raise ValueError("No merece ser  saqueado")
        else:
            print("Merece ser saqueado")
            return True
        """except ValueError as error:
            print(error)"""

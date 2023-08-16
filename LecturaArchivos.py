"""import pandas as pd

def lectura_Cargos():
    Barcos = pd.read_csv("ships.csv")

    Segmentacion de los datos en los 3 diferentes tipos de datos
                 Ship:
                    - Cargo == null
                    - extra == null
                 Cargo:
                    - extra == null
                 Pasangers:
                    - Cargo == null

    Cargos = Barcos[Barcos["quality"].notna()]
    return Cargos
def lectura_Cruise():
    Barcos = pd.read_csv("ships.csv")
    ""
    Segmentacion de los datos en los 3 diferentes tipos de datos
                 Ship:
                    - Cargo == null
                    - extra == null
                 Cargo:
                    - extra == null
                 Pasangers:
                    - Cargo == null
    ""

    Pasageros = Barcos[Barcos["quality"].isna() & Barcos["extra"].notna()]
    return Pasageros
    ""
    print("Barcos:\n "+str(Barcos)+"\n")
    print("Cargos: \n"+str(Cargos)+"\n")
    print("Pasajeros: \n"+str(Pasageros)+"\n")
    print("Ships: \n"+str(Ships)+"\n")
    ""

def lectura_Ships():
    Barcos = pd.read_csv("ships.csv")
    Ships = Barcos[Barcos["quality"].isna() & Barcos["extra"].isna()]
    return Ships
    ""
    Segmentacion de los datos en los 3 diferentes tipos de datos
                     Ship:
                        - Cargo == null
                        - extra == null
                     Cargo:
                        - extra == null
                     Pasangers:
                        - Cargo == null
    ""


if __name__ == "__main__":
  #lectura()
"""
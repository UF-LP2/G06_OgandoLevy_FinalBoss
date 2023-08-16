from src.ships import Ship
from src.ships import Cruise
from src.ships import Cargo

import pandas as pd
def main() -> None:

  Barcos = pd.read_csv("ships.csv")
  """
  Segmentacion de los datos en los 3 diferentes tipos de datos 
               Ship:
                  - Cargo == null 
                  - extra == null
               Cargo: 
                  - extra == null
               Pasangers: 
                  - Cargo == null    
  """
  Cargos = Barcos[Barcos["quality"].notna()]
  Pasageros = Barcos[Barcos["quality"].isna() & Barcos["extra"].notna()]
  Ships = Barcos[Barcos["quality"].isna() & Barcos["extra"].isna()]

  print("Barcos:\n "+str(Barcos)+"\n")
  print("Cargos: \n"+str(Cargos)+"\n")
  print("Pasajeros: \n"+str(Pasageros)+"\n")
  print("Ships: \n"+str(Ships)+"\n")
  """ CARGEROS """
  Lista_barcos_total=[]
  Lista_cargeros_crew_Bruto = Cargos["crew"].tolist()
  Lista_cargeros_draft_Bruto = Cargos["draft"].tolist()
  Lista_cargeros_quality_Bruto = Cargos["quality"].tolist()
  Lista_cargeros_extra_Bruto = Cargos["extra"].tolist()

  for i in range(0,len(Lista_cargeros_crew_Bruto)):
    try:
      # agrego el tipo de barco con los datos del elemento
      if(str(Lista_cargeros_extra_Bruto[i]) == "nan"):
        Lista_barcos_total.append(
          Cargo(0,Lista_cargeros_quality_Bruto[i], Lista_cargeros_draft_Bruto[i],
                Lista_cargeros_crew_Bruto[i]))
      else:
        Lista_barcos_total.append(
          Cargo(Lista_cargeros_extra_Bruto[i], Lista_cargeros_quality_Bruto[i], Lista_cargeros_draft_Bruto[i],
                Lista_cargeros_crew_Bruto[i]))
    except ValueError as error:
      print(error)

  """    PASAjEROS    """

  Lista_pasajeros_crew_Bruto = Cargos["crew"].tolist()
  Lista_pasajeros_draft_Bruto = Cargos["draft"].tolist()
  Lista_pasajeros_extra_Bruto = Cargos["extra"].tolist()
  for i in range(0,len(Lista_cargeros_crew_Bruto)):
    try:
        #agrego el tipo de barco con los datos del elemento
        Lista_barcos_total.append(
        Cruise(Lista_pasajeros_extra_Bruto[i], Lista_pasajeros_draft_Bruto[i],Lista_pasajeros_crew_Bruto[i]))
    except ValueError as error:
      print(error)



  """    Ship    """

  Lista_ship_crew_Bruto = Cargos["crew"].tolist()
  Lista_ship_draft_Bruto = Cargos["draft"].tolist()
  for i in range(0, len(Lista_cargeros_crew_Bruto)):
    try:
      #agrego el tipo de barco con los datos del elemento
      Lista_barcos_total.append(Ship(Lista_ship_draft_Bruto[i], Lista_ship_crew_Bruto[i]))
    except ValueError as error:
      print(error)
if __name__ == "__main__":
  main()

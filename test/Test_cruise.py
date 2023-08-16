import pytest
from src.ship import Cruise
def test_cruise_negativo_1() -> None:
    #Creo objetos que se que van a fallar
    crucero1 = Cruise(1, 20, 15)
    with pytest.raises(ValueError):
        crucero1.is_worth_it()

def test_cruise_negativo_2() -> None:
    #Creo objetos que se que van a fallar
    crucero2 = Cruise(-1, 5, 20)
    with pytest.raises(ValueError):
        crucero2.is_worth_it()

def test_cruise_negativo_3() -> None:
    #Creo objetos que se que van a fallar
    crucero3 = Cruise(0, 0, 0)
    with pytest.raises(ValueError):
        crucero3.is_worth_it()


def test_positivo_cruise():
  crucero4=Cruise(10,100,50)
  assert crucero4.is_worth_it() == True
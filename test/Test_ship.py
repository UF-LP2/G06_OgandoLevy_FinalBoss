import pytest
from src.ships import Ship
def test_negativo_ship():
  barquito=Ship(20,15)
  barquito2=Ship(-20, 15)
  barquito3=Ship(0,0)
  with pytest.raises(ValueError):
    barquito.is_worth_it()
    barquito2.is_worth_it()
    barquito3.is_worth_it()

def test_positivo_ship():
  barquito1 = Ship(30, 20)
  assert barquito1.is_worth_it() == True
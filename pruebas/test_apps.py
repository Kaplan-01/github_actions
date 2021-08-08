import pytest 
import aplicacion as apl

personas = [
    {'nombre': 'Maria', 'edad': 19},
    {'nombre': 'Carmen', 'edad': 20},
    {'nombre': 'Melanie', 'edad': 15}, 
    {'nombre': 'Victoria', 'edad': 10},
]

def testing():
    assert apl.Ordenar() == 1
    assert apl.Mayores(personas) == 2
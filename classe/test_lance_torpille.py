
from lance_torpille import *




def test_lance_torpilles_sous_marine():
    lance_torpilles = LanceTorpillesSousMarine()

    # Test avec munitions
    lance_torpilles.fire_at(10, 20, -5)  # Devrait réussir
    assert lance_torpilles.get_ammunition() == 23

    # Test sans munitions
    lance_torpilles.set_ammunition(0)
    lance_torpilles.fire_at(5, 10, -2)  # Devrait échouer avec NoAmmunitionError

    # Test hors de portée
    lance_torpilles.set_ammunition(1)
    lance_torpilles.fire_at(5, 10, 5)  # Devrait échouer avec OutOfRangeError

    # Test coordonnées valides
    lance_torpilles.set_ammunition(1)
    lance_torpilles.fire_at(-5, 15, -2)  # Devrait réussir
    



# Exécution des tests
test_lance_torpilles_sous_marine()
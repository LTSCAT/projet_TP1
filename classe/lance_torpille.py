from exception import *
from arme_mere import Weapon






class LanceTorpillesSousMarine(Weapon):
    def __init__(self):
        # Initialiser avec des valeurs spécifiques pour les torpilles
        super().__init__(ammunition=24, portee=40)

    def fire_at(self, x: int, y: int, z: int):
        try:
            super().fire_at(x, y, z)

            if z > 0:
                raise OutOfRangeError("Missile antisurface out of range.")
            elif z < 0:
                # Torpille
                if x <= 0 or y <= 0 or z <= 0:
                    raise OutOfRangeError("Invalid coordinates for torpille.")
            else:
                raise OutOfRangeError("Missile anti-air out of range.")

        except OutOfRangeError as e:
            print(f"Error: {e}")





from exception import *

class Weapon:
    def __init__(self, ammunition: int, portee: int):
        self.__ammunition = ammunition
        self.__portee = portee

    def get_ammunition(self):
        return self.__ammunition

    def set_ammunition(self):
        self.__ammunition = max(0, self.__ammunition - 1)

    def fire_at(self, x: int, y: int, z: int):
        try:
            if self.get_ammunition() == 0:
                raise NoAmmunitionError("No ammunition left.")
            else:
                print("Tir effectué.")
                self.set_ammunition()

        except NoAmmunitionError as e:
            print(f"Erreur : {e}")


class AntiAirMissile(Weapon):
    def __init__(self):
        # Appeler le constructeur de la classe mère avec les valeurs spécifiques
        super().__init__(ammunition=40, portee=20)

    def fire_at(self, x: int, y: int, z: int):
        try:
            # Valider les coordonnées de la cible
            if z <= 0:
                raise OutOfRangeError("Invalid target altitude (z should be greater than 0)")

            # Appeler la méthode de la classe mère pour vérifier les munitions
            super().fire_at(x, y, z)

        except OutOfRangeError as e:
            print(f"Erreur : {e}")
            # Retirer 1 des munitions en cas d'erreur
            self.set_ammunition()
        except NoAmmunitionError as e:
            print(f"Erreur : {e}")
            # Gérer l'épuisement des munitions spécifiquement pour la classe AntiAirMissile
            # Peut-être déclencher une alerte ou effectuer d'autres actions spécifiques.
        except Exception as e:
            # Gérer d'autres exceptions
            print(f"Erreur : {e}")



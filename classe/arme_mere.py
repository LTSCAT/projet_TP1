

class Weapon:
    def __init__(self,ammunition:int, portee:int):
        self.__ammunition=ammunition 
        self.__portee=portee


    def get_ammunition(self):
        return self.__ammunition 


    def set_ammunition(self):
        self.__ammunition = self.__ammunition - 1


    

    def fire_at(self, x:int, y:int, z:int):
        try:
    
            if     self.get_ammunition() == 0 :
                raise Exception ("NoAmmunitionError ")
            else:
                print("Tir effectué.")

        except Exception as e:
            print(f"Erreur : {e}")        

       




    
            




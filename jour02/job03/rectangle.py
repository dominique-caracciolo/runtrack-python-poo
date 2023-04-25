class Rectangle:
    def __init__(self, longueur, largeur) :
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        print((self.__longueur + self.__largeur) *2)

    def surface(self):
        print(self.__longueur * self.__largeur)

#------Get------#

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

 #------Set------#
    def set_longueur(self,new_longueur):
        self.__longueur = new_longueur

    def set_largeur(self,new_largeur):
        self.__largeur = self,new_largeur




class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur,largeur)
        self.hauteur= hauteur

    def get_hauteur(self):
        return self.hauteur
    
    def volume(self):
        print(self.get_longueur() * self.get_largeur() * self.get_hauteur())

rectangle = Rectangle(10,4)
para = Parallelepipede(10,4,4)

para.perimetre()
para.volume()
para.surface()




        



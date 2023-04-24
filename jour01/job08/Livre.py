class Livre:

    def __init__(self):
        self.__titre = "Le livre du siecle"
        self.__auteur = "Jean-michmich dupont"
        self.__pages = 42
        self.__disponible = True

    def get_titre(self):
        print("Le nom du livre est :", self.__titre)
        return self.__titre 
    def get_auteur(self):
        print("L'auteur du livre est :", self.__auteur)
        return self.__auteur 
    def get_pages(self):
        print("Le nombre de pages est de", self.__pages)
        return self.__pages
    
    def set_values(self, set_titre,set_auteur, set_pages):
        self.__titre = set_titre
        self.__auteur = set_auteur
        if set_pages >= 0 and set_pages is int(set_pages):
            self.__pages = set_pages       
        else:
            self.__pages = self.__pages
            print("Le nombre de pages doit etre positif, sans decimales,la valeur du nombre de pages n'est pas changer")
        
    def verification(self, verif):
        if self.__disponible is True:
            verif == True
        else: 
            verif == False

    def get_disponible(self):
        #print(self.__disponible)
        return self.__disponible
        

    def set_disponible(self,dispo):
        self.__disponible = dispo

    def emprunter(self,borrow):
        if borrow == True :
            self.__disponible = False
            print("Le livre est emprunté")
            return True
        else:
            return False
            
    def rendre(self, giveback):
        if self.__disponible == False:
            self.__disponible = True
            print("Le livre est rendu")
        else:
            print("Le livre n'est pas emprunté, il ne peut pas être rendu")


livre = Livre()

print(livre.get_disponible())
livre.emprunter(True) 
print(livre.get_disponible())
livre.rendre(True)
print(livre.get_disponible())




# livre.get_titre()
# livre.get_auteur()
# livre.get_pages()
# print("---------------------------------")
# livre.set_values("Le nouveau nom du livre", "Le nouvel auteur du livre", 25)

# livre.get_titre()
# livre.get_auteur()
# livre.get_pages()   
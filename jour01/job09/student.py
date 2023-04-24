class Student:
    def __init__(self):
        self.__nom = "John"
        self.__prenom = "Doe"
        self.__numero_etudiant = 145
        self.__credits = 0
        self.__level = self.__studentEval()

#--------Get--------#
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level

#---------Set---------#
    def set_nom(self,new_nom):
        self.__nom = new_nom

    def set_prenom(self,new_prenom):
        self.__prenom = new_prenom

    def set_numero_etudiant(self, new_nemero_etudiant):
        self.__numero_etudiant = new_nemero_etudiant

    def set_credits(self,new_credits):
        self.__credits = new_credits

    def add_credits(self,addcred):
        if addcred > 0:
            self.__credits += addcred
            self.__level = self.__studentEval()
        else:
            print("La valeur ajouter doit etre superieur a 0")
            

    def __studentEval(self):
        if self.get_credits() >= 90:
            return "Excelent"
        elif self.get_credits() >= 80:
            return "Tres bien"
        elif self.get_credits() >= 70:
            return "Bien"
        elif self.get_credits() >= 60:
            return "Passable"
        elif self.get_credits() < 60:
            return "Insuffisant"

    def StudentInfo(self):
        print("nom =", self.get_nom())
        print("prenom =",self.get_prenom())
        print("id =",self.get_numero_etudiant())
        print("Niveau =" ,self.get_level())
    


student = Student()
student.add_credits(25)
student.add_credits(25)
student.add_credits(25)
print(student.get_credits())
print("Le nombre de credits de", student.get_nom(), student.get_prenom(), "est de", student.get_credits())
student.StudentInfo()

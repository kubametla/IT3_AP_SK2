class Vozidlo:
   def __init__(self, znacka, rok_vyroby, stav_nadrze=100):
       self.znacka = znacka
       self.rok_vyroby = rok_vyroby
       self.stav_nadrze = stav_nadrze

   def info(self):
       return f"Vozidlo {self.znacka}, rok {self.rok_vyroby}"
   
   def zvuk_motoru(self):
       return "Vrrrum!"
   
   def startuj(self):
       if self.stav_nadrze > 0:
           print(self.info(), "startuje.")
           print(self.zvuk_motoru())
       else:
           print(self.info(), "nenastartuje, prázdná nádrž.")

class Auto(Vozidlo):
   def __init__(self, znacka, rok_vyroby, typ_prevodovky, stav_nadrze=100):
       super().__init__(znacka, rok_vyroby, stav_nadrze)
       self.typ_prevodovky = typ_prevodovky
   def zatroub(self):
       print("Túú")

class Moped(Vozidlo):
   def __init__(self, znacka, rok_vyroby, ma_slapadla, stav_nadrze=100):
       super().__init__(znacka, rok_vyroby, stav_nadrze)
       self.ma_slapadla = ma_slapadla
   def zvuk_motoru(self):
       return "Trtrtr"
   def slapni(self):
       print("Šlápni do toho")

auto = Auto("Škoda", 2016, "manuální")
moped = Moped("Jawa", 2020, True)

garaz = [auto, moped]

for vozidlo in garaz:
   print("--------------------")
   print(vozidlo.info())
   vozidlo.startuj()

print("--------------------")
auto.zatroub()
print("--------------------")
moped.slapni()
class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

def zvuk(self):
    return "???"

def predstav_se(self):
    return f"Jmenuji se {self.jmeno} a je mi {self.vek}"

def kde_jsi(self):
    return f"jsem v {self.misto}"

def jdi_na(self, nMisto:str):
    self.misto = nMisto
    return f"Přesunul jsem se na {nMisto}"

zvire = Zvire("Šoral",50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)
print(zvire.zvuk("???"))
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("Kadeřnictví"))

zvire2 = Zvire("Wolfram", 32, "PentHouse")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.predstav_se())
print(zvire2.zvuk())
print(zvire2.jdi_na("Klokánek"))
class Robot:
    def __init__(self, oznaceni: str, baterie: int, ukol: str):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return "Tudum"
    
    def diagnositka(self):
        return f"{self.baterie}, {self.oznaceni}"

    
    def aktualniUkol(self):
        return self.ukol
    
    def zadejUkol(self,NovyUkol:str):
        self.ukol = NovyUkol
        return f"Tvuj nový úkol je {self.ukol}"
    
robot = Robot("Tudum", 90, "umýt nádobí")
print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)
print(robot.zvuk())
print(robot.diagnositka())
print(robot.aktualniUkol())
print(robot.zadejUkol("uklidit nádobí"))
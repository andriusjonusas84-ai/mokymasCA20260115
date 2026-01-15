from dataclasses import dataclass


@dataclass
class Kursas:
    destytojas: str
    trukme: int

    def destyti(self):
        print("Vyksta mokymas")
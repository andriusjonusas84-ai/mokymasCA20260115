from dataclasses import dataclass


@dataclass
class Kursas:
    pavadinimas: strs
    destytojas: str
    trukme: int

    def destyti(self):
        print("Vyksta mokymas")
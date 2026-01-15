from dataclasses import dataclass
from models.kursas import Kursas


@dataclass
class PythonKursas(Kursas):
    def destyti(self):
        print("Vyksta programavimas")

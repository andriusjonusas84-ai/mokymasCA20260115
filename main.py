from models.python_kursas import Kursas,PythonKursas
import datetime
import numpy
import django
import pandas


kursas = Kursas("Algis Stankevicius",40)
python_kursas = PythonKursas("Donatas Noreikia",30)

if __name__ == "__main__":
    print("Ar mokymas vyksta")
    kursas.destyti()
    python_kursas.destyti()
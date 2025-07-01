import json

class ModelAI:
    # Atrybut klasowy do śledzenia liczby utworzonych modeli
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.liczba_modeli += 1  # Zwiększamy licznik przy każdym nowym obiekcie

    @classmethod
    def nowy_model(cls):
        cls.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        # Tworzenie obiektu na podstawie pliku JSON
        with open(nazwa_pliku, 'r') as f:
            dane = json.load(f)
        return cls(dane['name'], dane['version'])

# Przykład użycia
# model = ModelAI.z_pliku("model.json")
# print(model.nazwa_modelu, model.wersja)
# print(ModelAI.ile_modeli())

from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur

class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)

class ColorMixin:
    def __init__(self, *args, couleur="blanc", **kwargs):
        super().__init__(*args, **kwargs)
        self.couleur = couleur

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} – couleur : {self.couleur}"

class CercleColore(ColorMixin, Cercle):
    pass

class RectangleColore(ColorMixin, Rectangle):
    pass

class TriangleColore(ColorMixin, Triangle):
    pass

class CarreColore(ColorMixin, Carre):
    pass

if __name__ == "__main__":
    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2),
        Carre(4),
        CercleColore(2, couleur="rouge"),
        RectangleColore(3, 7, couleur="bleu"),
        TriangleColore(5, 4, couleur="vert"),
        CarreColore(5, couleur="jaune")
    ]

    for f in formes:
        print(f)
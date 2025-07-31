import csv

biblio = open("livre_bibliotheque", "r")

class Biblioteque:
    def __init__(self, section):
        pass

class Livre(Biblioteque):
    def __init__(self, code, titre, auteur, pages, date_edition, date_arrive, genre, editeur):
        self._code = code
        self.titre = titre
        self._auteur = auteur
        self.pages = pages
        self._date_edition = date_edition
        self._date_arrive = date_arrive
        self._genre = genre
        self.editeur = editeur
    


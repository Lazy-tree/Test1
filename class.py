import csv
import matplotlib.pyplot as plt
from datetime import date, datetime
from collections import Counter
import uuid

class Livre:
    def __init__(self, titre, auteur, pages, date_edition, date_arrivee, genre, editeur):
        self.code = self.generer_code()  # ID unique (12 caractères)
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.date_edition = date_edition  # type date
        self.date_arrivee = date_arrivee  # type date
        self.genre = genre
        self.editeur = editeur
    
    @staticmethod
    def generer_code():
        return uuid.uuid4().hex[:12].upper()
    
    def __str__(self):
        return f"{self.code} - {self.titre} ({self.auteur})"

class Bibliotheque:
    def __init__(self):
        self.livres = {}  # {code: Livre}
        self.historique = []  # [("ajout"|"suppression", code, date)]

    def charger_depuis_csv(self, chemin_fichier):
        with open(chemin_fichier, newline='', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            for ligne in lecteur:
                livre = Livre(
                    titre=ligne["titre"],
                    auteur=ligne["auteur"],
                    pages=int(ligne["pages"]),
                    date_edition=datetime.strptime(ligne["date_edition"], "%Y-%m-%d").date(),
                    date_arrivee=datetime.strptime(ligne["date_arrivee"], "%Y-%m-%d").date(),
                    genre=ligne["genre"],
                    editeur=ligne["editeur"]
                )
                # self.ajouter(livre) ou
                self[livre.code] = livre

    def afficher_histogramme_arrivees(self):
        donnees = [livre.date_arrivee.strftime("%Y-%m") for livre in self.livres.values()]
        if not donnees:
            print("Aucune donnée pour générer l'histogramme.")
            return
        frequence = Counter(donnees)
        mois = sorted(frequence)
        valeurs = [frequence[m] for m in mois]
        
        plt.figure(figsize=(10, 5))
        plt.bar(mois, valeurs)
        plt.title("Nombre de livres arrivés par mois")
        plt.xlabel("Mois")
        plt.ylabel("Nombre de livres")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    def ajouter(self, livre):
        self.livres[livre.code] = livre
        self.historique.append(('ajout', livre.code, livre.date_arrivee))
        print(livre)
# ou
    def __setitem__(self, code, livre):
        self.ajouter(livre)

    def supprimer(self, code):
        if code in self.livres:
            del self.livres[code]
            self.historique.append(('suppression', code, date.today()))

    def modifier(self, code, **kwargs):
        livre = self.livres.get(code)
        if livre:
            for clé, valeur in kwargs.items():
                if hasattr(livre, clé):
                    setattr(livre, clé, valeur)

    def lister(self, filtre=None):
        if filtre is None:
            return list(self.livres.values())
        return [livre for livre in self.livres.values() if filtre(livre)]

    def compter(self):
        return len(self.livres)

    def stats_par_mois(self, type_action="ajout"):
        stats = Counter()
        for action, code, d in self.historique:
            if action == type_action:
                stats[(d.year, d.month)] += 1
        return dict(stats)

    def evolution_stock(self):
        count = 0
        historique_trie = sorted(self.historique, key=lambda x: x[2])
        evolution = []
        for action, code, d in historique_trie:
            count += 1 if action == 'ajout' else -1
            evolution.append((d, count))
        return evolution

biblio = Bibliotheque()
biblio.charger_depuis_csv("livres_bibliotheque.csv")

print("Nombre total de livres:", biblio.compter())
print("Statistiques mensuelles (ajouts):", biblio.stats_par_mois())

biblio.afficher_histogramme_arrivees()


class Dictionnaire:
    
    def __init__(self, base={}, **donnes):
        self._cle = []
        self._valeurs = []

        if type(base) not in (dict, Dictionnaire):
            raise TypeError("Le type attendu est un dictionnaire (usuel ou ordonné)")
        
        for cle in base:
            self[cle] = base[cle]
        for cle in donnes:
            self[cle] = donnes[cle]
        

    def __repr__(self):
        return self

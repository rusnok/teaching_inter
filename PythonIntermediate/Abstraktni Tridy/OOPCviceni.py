class JakkolivNazvana:
    def __init__(self, nejaky_integer):
        self.cislo = nejaky_integer

    def mocnina(self):
        print(self.cislo**2)

a = JakkolivNazvana(5)
a.mocnina() # 25

a = JakkolivNazvana(2)
a.mocnina() # 4
print(a.cislo)
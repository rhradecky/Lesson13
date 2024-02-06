'''
class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("tato trieda je singlet")
        else:
            self.meno = "Patrick"
            Singleton._instance = self

    @staticmethod
    def getIstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

s1 = Singleton.getIstance()
print(s1.meno)
s2 = Singleton.getIstance()
s1.meno = "Milan"
print(s2.meno)

s3 = Singleton._Istance()
s3.meno = "Milan"
print(s3.meno)



************************************************************************************************


class Document:
    def create(self):
        raise NotImplementedError("Metoda create() musi byt prepisana")


class PDFDocument(Document):
    def create(self):
        return "Vytvaram PDF"

class WordDocument(Document):
    def create(self):
        return "Vytvaram Word"

class TxtDocument(Document):
    def create(self):
        return "Vytvaram txt"


class Factory:
    def create_document(self, type):
        if type == 'pdf':
            return PDFDocument()
        elif type == 'word':
            return  WordDocument()
        elif type == 'txt':
            return  TxtDocument()

        else:
            raise ValueError("Neznamy typ dokumentu")
factory = Factory()
pdf = factory.create_document('pdf')
print(pdf.create())

word =  factory.create_document('word')
print(word.create())

txt =  factory.create_document('txt')
print(txt.create())





class Form:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def __str__(self):
        return "\n".join(self.fields)

class FormBuilder:
    def __init__(self):
        self.form = Form()

    def add_name_field(self):
        self.form.add_field("Name: [________________]")
        return self

    def add_address_field(self):
        self.form.add_field("Adress: [________________]")
        return self

    def add_email_field(self):
        self.form.add_field("Email: [________________]")
        return self

    def add_ecountry_field(self):
        self.form.add_field("Country: [________________]")
        return self


    def build(self):
        return self.form

builder = FormBuilder()
form = builder.add_name_field().add_address_field().add_email_field().add_ecountry_field().build()
print(form)




class Napoj:
    def cena(self):
        raise NotImplementalError

class Kava(Napoj):
    def cena(self):
        return 2

class Caj(Napoj):
    def cena(self):
        return 3

class PrisadaDecorator(Napoj):
    def __init__(self, napoj):
        self._napoj = napoj

    def cena(self):
        return self._napoj.cena()

class Mlieko(PrisadaDecorator):
    def cena(self):
        return self._napoj.cena() + 5

class Cukor(PrisadaDecorator):
    def cena(self):
        return self._napoj.cena() + 2


moja_kava = Kava()
print(moja_kava.cena())
moja_kava = Mlieko(moja_kava)
print(moja_kava.cena())
moja_kava = Cukor(moja_kava)
print(moja_kava.cena())

moj_caj = Caj()
moj_caj = Cukor(moja_kava)
print(moj_caj.cena())

****************************************************************************************************
'''


class AkciovaBurza:
    def __init__(self):
        self._investori = []
        self._cena_akcie = None

    def pridaj_investora(self, investor):
        self._investori.append(investor)

    def odstran_investora(self, investor):
        self._investori.remove(investor)

    def notifikuj_investov(self):
        for investor in self._investori:
            investor.update(self._cena_akcie)

    def set_cena_akcie(self, cena):
        self._cena_akcie = cena
        self.notifikuj_investov()




class Investor:
    def update(self, cena):
        print(f"Aktualizovana cena akcie: {cena}")

burza = AkciovaBurza()
investor1 = Investor()
investor2 = Investor()

burza.pridaj_investora(investor1)
burza.pridaj_investora(investor2)

burza.set_cena_akcie(100)

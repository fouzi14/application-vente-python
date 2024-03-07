from peewee import *
import datetime


db = MySQLDatabase('hassan',user='root',password='root',
                   host='localhost',port=3306)

class produit(Model):
    reference=CharField()
    designiation=CharField()
    marque=CharField()
    famille=CharField()
    unite=CharField()
    cond=IntegerField()
    prixachat=IntegerField()
    prixdetail=IntegerField()
    prixgros=IntegerField()
    prixrevendeur=IntegerField()
    localisation=CharField()
    stock=IntegerField()
    observation=CharField()

    class Meta :
        database=db

class client(Model):
    code=CharField()
    nom=CharField()
    tarif=CharField()
    adresse=CharField()
    telephon=IntegerField()
    region=CharField()
    wilaya=CharField()
    mail=CharField()
    soldeinitail=IntegerField()
    soldemax = IntegerField()
    reglement = CharField()
    soldeactuel = IntegerField()
    detenow=datetime.datetime.now()
    regcom=CharField()
    matfis=CharField()
    Artimp=CharField()
    nis=CharField()
    mobil=IntegerField()

    class Meta:
        database=db


class fournisseur(Model):
    code = CharField()
    nom = CharField()
    adresse = CharField()
    telephon = IntegerField()
    mobil=IntegerField()
    region = CharField()
    wilaya = CharField()
    mail = CharField()
    solde = IntegerField()
    detenow = datetime.datetime.now()

    class Meta:
        database = db





class factur(Model):
    N_de_facture=CharField()
    date=datetime.date
    nom=CharField()
    HT=DecimalField()
    TVA=FloatField()
    timbre=DecimalField()
    TTC=DecimalField()
    modepaiement=CharField()
    date= CharField()
    class Meta:
        database=db

class caisse(Model):
    date=CharField()
    description=CharField()
    tiers=CharField()
    entree=DecimalField()
    sortee=DecimalField()
    modepaiement=CharField()
    class Meta:
        database=db





db.connect()

db.create_tables([produit,client,fournisseur,factur,caisse])
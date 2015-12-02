# -*- coding: utf-8 -*-


def services():
    rowLesServices = db().select(db.services.libelle,db.services.description)
    return locals()

@auth.requires_membership('Administration')
def servicesModif():
    grid = SQLFORM.grid(db.services)
    return locals()

def contact():
    return locals()

def locaux():
    return locals()

def personel():
    rowPersonel = db().select(db.personel.nom,db.personel.prenom,db.personel.adresse,db.personel.tel)
    return locals()

@auth.requires_membership('Administration')
def personelModif():
    grid = SQLFORM.grid(db.personel)
    return locals()



def listeFormation():
    rowLesFormations = db().select(db.formation.libelle,db.formation.description,db.formation.nbrPlaces)
    return locals()

@auth.requires_membership('Administration')
def formationModif():
    grid = SQLFORM.grid(db.formation)
    return locals()

@auth.requires_login()
def inscriptionFormation(idUser,idFormation):
    db.inscriptionFormation.insert(idUser,idFormation)
    return locals()

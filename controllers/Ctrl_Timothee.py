# -*- coding: utf-8 -*-
# essayez quelque chose comme
def index(): return dict(message="hello from Ctrl_Timothee.py")
def olympique():
    rowsAthlete=db(db.ligue.id==db.athlete.idLigue).select(db.athlete.nom,db.athlete.prenom,db.ligue.discipline,db.ligue.nom)
    rowsDateOlympique=db(db.athlete.id==db.dateOlympique.idAthlete).select(db.athlete.nom,db.dateOlympique.dateOlympique)
    return locals()

# -*- coding: utf-8 -*-
# essayez quelque chose comme
def olympique():
    rowsAthlete=db(db.ligue.id==db.athlete.idLigue).select(db.athlete.nom,db.athlete.prenom,db.ligue.discipline,db.ligue.nom)
    rowsDateOlympique=db(db.athlete.id==db.dateOlympique.idAthlete).select(db.athlete.nom,db.dateOlympique.dateOlympique)
    return locals()
def ajouterDateOlympique():
    listeAthlete=[]
    for row in db().select(db.athlete.nom):
        listeAthlete.append(row.nom)
    formDate=SQLFORM.factory( Field('Nom','string',requires=IS_IN_SET(listeAthlete)),
                             Field('Date','date',requires=IS_NOT_EMPTY())).process()
    if formDate.accepted:
        response.flash= 'Date Ajouté'
        idAthlete=db(db.athlete.nom==request.vars.Nom).select(db.athlete.id)
        idAthlete=idAthlete[0]
        db.dateOlympique.update_or_insert(dateOlympique=request.vars.Date,
                                          idAthlete=idAthlete)
    return locals()
def adminOlympique():
    listeLigue=[]
    for row in db().select(db.ligue.nom):
        listeLigue.append(row.nom)
    form=SQLFORM.factory( Field('nom','string'),
                         Field('prenom','string'),
                         Field('Date','date'),
                         Field('Ligue','text',requires=IS_IN_SET(listeLigue))).process()
    if form.accepted:
        response.flash= 'Athlete Ajouté'
        idLigue=db(db.ligue.nom==request.vars.Ligue).select(db.ligue.id)
        idLigue=idLigue[0]
        db.athlete.update_or_insert(nom=request.vars.nom,
                                    prenom=request.vars.prenom,
                                    idLigue=idLigue
                                     )
        idA=db(db.athlete.nom==request.vars.nom).select(db.athlete.id)
        idA=idA[0]
        db.dateOlympique.update_or_insert(dateOlympique=request.vars.Date,
                                          idAthlete=idA
                                         )
    return locals()

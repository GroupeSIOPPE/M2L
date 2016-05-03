# -*- coding: utf-8 -*-

def aggregator():
    import gluon.contrib.feedparser as feedparser
    d = feedparser.parse(
        "http://www.republicain-lorrain.fr/sports/rss")
    return dict(title=d.channel.title,
                link = d.channel.link,
                description = d.channel.description,
                created_on = request.now,
                entries = [
                  dict(title = entry.title,
                  link = entry.link,
                  description = entry.description,
                  created_on = request.now) for entry in d.entries])

def actu():
    import gluon.contrib.feedparser as feedparser
    rssLorrain = aggregator()
    return locals()

def ligues():
    rowsLigues=db().select(db.ligue.ALL)
    NbLicencies=[]
    for uneLigue in rowsLigues:
        NbLicencies.append(db(uneLigue.id==db.athlete.idLigue).count())

    return locals()

def ajoutLigue():
    form = SQLFORM(db.ligue)
    if form.process().accepted:
        response.flash = 'Ligue ajouté'
    elif form.errors:
        response.flash = 'Problème dans le formulaire'
    else:
        response.flash = 'Veuillez remplir le formulaire'
    return dict(form=form)

def supprLigue():
    rowsLigues=[]
    for row in db(db.ligue.nom).select(db.ligue.nom, distinct=True):
        rowsLigues.append(row.nom)

    ligueChoisi=request.vars['nom']
    db(db.ligue.nom==ligueChoisi).delete()
    return locals()

def infosLigues():
    Ligue=db(db.ligue.id==request.vars['ligue']).select(db.ligue.ALL)
    Athlete=db(db.athlete.idLigue==request.vars['ligue']).select(db.athlete.ALL)
    return locals()

def demandesFormations():
    rowInscriPerso=db((db.personel.id==db.inscriptionCROSL.idPersonnel)&(db.formation.id==db.inscriptionCROSL.idFormation)).select(db.personel.nom, db.personel.prenom, db.formation.libelle)

    return locals()

def export_xml():
    rowsLigues=db().select(db.ligue.ALL)
    rowsClubs=db().select(db.club.ALL)
    rowsEquipes=db().select(db.equipe.ALL)
    rowsCategories=db().select(db.categorie.ALL)
    rowsLicencies=db().select(db.licencie.ALL)
    return locals()

# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
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

def xml_writer():
    rows=[]
    rowsLigues=db().select(db.ligue.ALL)
    rows.append(rowsLigues)
    rowsClubs=db().select(db.club.ALL)
    rows.append(rowsClubs)
    rowsEquipes=db().select(db.equipe.ALL)
    rows.append(rowsEquipes)
    rowsCategories=db().select(db.categorie.ALL)
    rows.append(rowsCategories)
    rowsLicencies=db().select(db.licencie.ALL)
    rows.append(rowsLicencies)

    root= ET.Element("root")
    for row in rows :
        nomTable=unicode(str(row), 'utf-8')
        nomTable=nomTable[0:4]
        if nomTable=="ligu":
            fields=db.ligue.fields
        if nomTable=="club":
            fields=db.club.fields
        if nomTable=="equi":
            fields=db.equipe.fields
        if nomTable=="lice":
            fields=db.licencie.fields
        if nomTable=="cate":
            fields=db.categorie.fields
        for element in row:
            table= ET.SubElement(root, "table", name=nomTable)
            for f in fields:
                valeur=unicode(str(element[f]), 'utf-8')
                ET.SubElement(table, "column", name=f).text=valeur
    tree=ET.ElementTree(root)
    tree.write("applications/M2L/static/bdd.xml")


def get_xml():
    xml_writer()
    url = URL('static','bdd.xml')
    redirect(url)

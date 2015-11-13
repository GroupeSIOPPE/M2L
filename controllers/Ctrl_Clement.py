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

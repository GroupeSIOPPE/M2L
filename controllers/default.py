# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    Page d'accueil
    """
    message = "Bienvenue sur le portail de la Maison des Ligues !"
    return locals()

def evenement():
    evenements=db(db.ligue.id==db.evenement.idLigue).select(db.evenement.nom, db.evenement.adresse, db.evenement.remarques, db.evenement.site, db.evenement.dateDebut, db.evenement.dateFin, db.ligue.nom,  orderby=db.evenement.dateDebut)
    return locals()

def evtadmin():
    evenements=db(db.ligue.id==db.evenement.idLigue).select(db.evenement.nom, db.evenement.adresse, db.evenement.remarques, db.evenement.site, db.evenement.dateDebut, db.evenement.dateFin, db.ligue.nom,  orderby=db.evenement.dateDebut)

    listeLigue=[]

    for row in db().select(db.ligue.nom, orderby=db.ligue.nom):
        listeLigue.append(row.nom)

    form=SQLFORM.factory(
            Field('nom','text',requires=IS_NOT_EMPTY()),
            Field('adresse','text',requires=IS_NOT_EMPTY()),
            Field('remarques','text',requires=IS_NOT_EMPTY()),
            Field('site','text',requires=IS_NOT_EMPTY()),
            Field('dateDebut','date',requires=IS_NOT_EMPTY()),
            Field('dateFin','date',requires=IS_NOT_EMPTY()),
            Field('idLigue','text',requires=IS_IN_SET(listeLigue))).process()

    if form.accepted:
        rows=db(db.ligue.nom==request.vars.idLigue).select(db.ligue.id)
        for row in rows:
            idLigue=row.id
            db.evenement.update_or_insert(nom=request.vars.nom,
                                          adresse=request.vars.adresse,
                                          remarques=request.vars.remarques,
                                          site=request.vars.site,
                                          dateDebut=request.vars.dateDebut,
                                          dateFin=request.vars.dateFin,
                                          idLigue=idLigue
                                          )
        redirect(URL('evtadmin'))

    supp=SQLFORM.factory(
        suppression=db(db.evenement.nom==unEvenement.evenement.nom).delete())


    return locals()

def statutJuridique():
    """
    Page statut juridique
    """
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

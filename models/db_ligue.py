# -*- coding: utf-8 -*-
db.define_table('ligue',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('URLSiteWeb','string'),
             Field('emailContact','string'), 
             Field('discipline','string')
             ,migrate=False)


db.define_table('evenement',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresse','string',requires=IS_NOT_EMPTY()),
             Field('remarques','string',requires=IS_NOT_EMPTY()),
             Field('site','string',requires=IS_NOT_EMPTY()),
             Field('dateDebut','date'),
             Field('dateFin','date'),
             Field('idLigue','reference ligue',requires=IS_IN_DB(db,db.ligue.id,'%(nom)s'))
             ,migrate=False)

db.define_table('athlete',
                Field('nom','string',requires=IS_NOT_EMPTY()),
                Field('prenom','string',requires=IS_NOT_EMPTY()),
                Field('idLigue','reference ligue',requires=IS_IN_DB(db,db.ligue.id,'%(discipline)s')),
                migrate=False)

db.define_table('dateOlympique',
                Field('dateOlympique','date',requires=IS_NOT_EMPTY()),
                Field('idAthlete','reference athlete',requires=IS_IN_DB(db,db.athlete.id,'%(nom)s')),
                migrate=False)

db.define_table('formationJBFD',
                Field('theme','string',requires=IS_NOT_EMPTY()),
                Field('lieu','string'),
                Field('dateDebut','date'),
                Field('dateFin','date'),
                Field('heureDebut','integer'),
                Field('heureFin','integer'),
                Field('intervenant','string'),
                Field('contenu','string'),
                migrate=False)

db.define_table('JBFD',
                Field('promotion','string'),
                migrate=False)

db.define_table('contenir',
                Field('idJBFD','reference JBFD',requires=IS_IN_DB(db,db.athlete.id,'%(promotion)s')),
                Field('idFormationJBFD','reference formationJBFD',requires=IS_IN_DB(db,db.athlete.id,'%(theme)s')),
                migrate=False)

db.define_table('inscriptionJBFD',
                Field('idPersonnel','reference personel',requires=IS_IN_DB(db,db.athlete.id,'%(nom)s')),
                Field('idJBFD','reference JBFD',requires=IS_IN_DB(db,db.athlete.id,'%(promotion)s')),
                migrate=False)

db.define_table('formation',
                Field('libelle','string'),
                Field('lieu','string'),
                Field('intervenant','string'),
                Field('audience','string'),
                Field('objectif','string'),
                Field('prerequis','string'),
                Field('contenus','string'),
                Field('cout','integer'),
                Field('repas','string'),
                Field('dateLimite','date'),
                Field('dateDebut','date'),
                Field('dateFin','date'),
                Field('heureDebut','integer'),
                Field('heureFin','integer'),
                migrate=False)

db.define_table('participer',
                Field('idPersonnel','reference personel',requires=IS_IN_DB(db,db.athlete.id,'%(nom)s')),
                Field('idFormation','reference formation',requires=IS_IN_DB(db,db.athlete.id,'%(libelle)s')),
                migrate=False)

db.define_table('inscriptionCROSL',
                Field('idPersonnel','reference personel',requires=IS_IN_DB(db,db.athlete.id,'%(nom)s')),
                Field('idFormation','reference formation',requires=IS_IN_DB(db,db.athlete.id,'%(libelle)s')),
                Field('dateInscription','date'),
                migrate=False)

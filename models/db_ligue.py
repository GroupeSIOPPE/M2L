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

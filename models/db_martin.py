# -*- coding: utf-8 -*-


db.define_table('services',
          Field('libelle','string',requires=IS_NOT_EMPTY()),
          Field('description','string',requires=IS_NOT_EMPTY()),
          migrate=False)

db.define_table('personel',
          Field('nom','string',requires=IS_NOT_EMPTY()),
          Field('prenom','string',requires=IS_NOT_EMPTY()),
          Field('adresse','string',requires=IS_NOT_EMPTY()),
          Field('tel','string',requires=IS_NOT_EMPTY()),
          migrate=False)

db.define_table('formation',
          Field('libelle','string',requires=IS_NOT_EMPTY()),
          Field('description','string',requires=IS_NOT_EMPTY()),
          Field('nbrPlaces','integer',requires=IS_NOT_EMPTY()),
          migrate=False)

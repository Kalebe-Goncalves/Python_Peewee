import os
from peewee import *

arq = "plantas.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db
        
class Planta(BaseModel):
    nome = CharField()
    nome_cientifico = CharField()
    tamanho_folha = CharField()

class Jardim(BaseModel):
    nome_jardineiro = CharField()
    localizacao = CharField()

class PlantadoJardim(BaseModel):
    jardim = ForeignKeyField(Jardim)
    planta = ForeignKeyField(Planta)    

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([
    Planta,
    Jardim,
    PlantadoJardim
])

planta1 = Planta.create(nome = "Rosa", nome_cientifico = "FelipiumTestumdum", tamanho_folha = "Médio", especie = "Cannabis", periodo_poda = "120 dias")
planta2 = Planta.create(nome = "Lirio", nome_cientifico = "AmendoimRosiumPequinium", tamanho_folha = "Pequeno", especie = "folhinha", periodo_poda = "2 meses")
jardim_prefeitura = Jardim.create(nome_jardineiro = "Everton", localizacao = "Timbocity")

PlantaPrefeitura = PlantadoJardim.create(jardim = jardim_prefeitura, planta = planta1)
PlantaPrefeitura = PlantadoJardim.create(jardim = jardim_prefeitura, planta = planta2) 


q1 = PlantadoJardim.select()
for planta in q1:
    print(planta.planta.nome, planta.planta.periodo_poda)

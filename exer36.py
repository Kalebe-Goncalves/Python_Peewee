import os
from peewee import *

arq = "marcenaria.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    cpf = CharField()
    nome = CharField()
    telefone = CharField()

class Mobilia(BaseModel):
    nome_mobilia = CharField()
    material = CharField()
    cor = CharField()

class Pedidos(BaseModel):
    cliente = ForeignKeyField(Cliente)
    mobilia_pedida = ForeignKeyField(Mobilia)  

class Estoque(BaseModel):
    mobilia_em_estoque = ForeignKeyField(Mobilia)
    quantidade = CharField()

db.connect()
db.create_tables([
    Cliente,
    Mobilia,
    Estoque,
    Pedidos,
])

joao = Cliente.create(cpf = "94217842-12", nome = "Joao", telefone = "(47)95424-3123")
mesa = Mobilia.create(nome_mobilia = "Mesa", material = "Madeira Reflorestada", cor = "Branca")
estoque = Estoque.create(mobilia_em_estoque = mesa, quantidade = "4")
pedido1 = Pedidos.create(cliente = joao, mobilia_pedida = mesa)


info = Pedidos.select()
for pedido in info:
    print(pedido.cliente.nome)



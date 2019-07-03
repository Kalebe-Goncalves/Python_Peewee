from peewee import *
import datetime

arq = "eventosaude.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Registro(BaseModel):
    data = DateField()
    ocorrencia = CharField()
    intensidade = IntegerField()
    observacoes = CharField()


db.connect()
db.create_tables([Registro])

reg = Registro.create(data = datetime.date(2019, 6, 26), ocorrencia = "Dor de cabeça", intensidade = 0, observacoes = "Jantei muito na noite anterior (resto de marmita do almoço)")

print(reg.data, reg.ocorrencia, reg.intensidade, reg.observacoes)
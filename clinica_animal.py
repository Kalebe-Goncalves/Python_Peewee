import peewee, os

db = peewee.SqliteDatabase('animalia.db')

class Animal(peewee.Model):
    nomedono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    class Meta:
        database = db
    def __str__(self):
        return self.tipo_animal+","+self.raca+" de "+self.nomedono

class Cliente(peewee.Model):
    nome = peewee.CharField()
    email = peewee.CharField()
    telefone = peewee.CharField()
    myID = peewee.IntegerField()
    nomeLogin = peewee.CharField()
    senha = peewee.CharField()
    class Meta:
        database = db
        def __str__(self):
            return self.nome + "," + self.email + "," + self.telefone + "," + str(self.myID) + "," + self.nomeLogin + "," + self.senha



class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    cliente = peewee.ForeignKeyField(Cliente)
    confirma = peewee.CharField()
    myID = peewee.CharField()
    class Meta:
        database = db
    def __str__(self):
        return self.servico+" em "+self.data+":"+self.horario+", confirmado: "+\
        self.confirma+", ID da consulta: "+self.myID+" | animal: "+str(self.animal) + "cliente: " + str(self.cliente)

if __name__ == '__main__':
    arq = 'animalia.db'
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Animal,Consulta]) 
    except peewee.OperationalError as e:
        print("erro ao criar tabelas: "+str(e))

    print("TESTE DO ANIMAL")
    a1 = Animal(nomedono="José", email="gustavoschlei27@gmail.com")
    print(a1)

    print("TESTE DO CLIENTE")
    a1 = Animal(nome="Schlei", tipo_animal="C", raca="Chiuaua")
    print(a1)  

    print("TESTE DA CONSULTA")
    c1 = Consulta(data="19/09/2018", servico="Consulta de rotina", 
    horario="14:00", animal=a1, confirma="N", myID="c9d8f7gu4h3hnwsik3e")
    print(c1)



    print("TESTE DA PERSISTÊNCIA")
    a1.save()
    c1.save()
    c2 = Consulta(data="21/09/2018", servico="Aplicação de vacina", 
    horario="10:00", animal=a1, confirma="S", myID="d9firtu3434uit")
    c2.save()
    todos = Consulta.select()
    for con in todos:
        print(con)
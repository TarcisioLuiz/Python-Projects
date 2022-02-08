class Funcionario:
    def init(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Gerente(Funcionario):
    pass


class Recepcionista(Funcionario):
    pass

a = []
f1 = Funcionario("Igor", 20)
f2 = Gerente("Raphael", 18)
f3 = Recepcionista("Lucas", 22)
a.append(f1.nome)
a.insert(1, f1.idade)
a.insert(2, f2.nome)
a.insert(3, f2.idade)
a.insert(4, f3.nome)
a.insert(5, f3.idade)
print(f1.nome, f1.idade, f2.nome, f2.idade, f3.nome, f3.idade)
print(a)
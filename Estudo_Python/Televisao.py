class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()
print(f'Televisão está ligada: {televisao.ligada}')
televisao.power()
print(f'Televisão está ligada: {televisao.ligada}')
televisao.power()
print(f'Televisão está ligada: {televisao.ligada}')
print(f'Canal: {televisao.canal}')
televisao.power()
print(f'Televisão está ligada: {televisao.ligada}')
televisao.aumentar_canal()
televisao.aumentar_canal()
print(f'Canal: {televisao.canal}')
televisao.diminui_canal()
print(f'Canal: {televisao.canal}')

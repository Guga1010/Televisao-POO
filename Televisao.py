import os
os.system("cls")

televisoes = []
class Televisao:
    def __init__(self,nome):
        self.nome = nome
        self.ligado = False
        self.canal = 0
        self.volume = 0

    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False

    def aument_canal(self):
        if self.ligado:
            self.canal+=1
        else:
            print("Ligue a TV primeiro")
    def diminui_canal(self):
        if self.ligado:
            if self.canal:
                self.canal-=1
        else:
            print("Ligue a TV primeiro")
    
    def aument_vol(self):
        if self.ligado:
            self.volume+=1
        else:
            print("Ligue a TV primeiro")
    def diminui_vol(self):
        if self.ligado:
            if self.volume:
                self.volume-=1
        else:
            print("Ligue a TV primeiro")

    def info(self):
        print("Nome TV: "+self.nome)
        print("Ligado.: "+("Sim" if self.ligado else "Não"))
        print("Canal..: "+str(self.canal))
        print("Volume.: "+str(self.volume))

def Menu():
    os.system("cls") or None
    print("1 - Criar uma TV")
    print("2 - Excluir uma TV")
    print("3 - Mostrar informação da TV")
    print("4 - Ligar TV")
    print("5 - Desligar TV")
    print("6 - Aumentar canal da TV")
    print("7 - Diminuir canal da TV")
    print("8 - Aumentar volume da TV")
    print("9 - Diminuir volume da TV")
    print("10 - Listar todas as televisões")
    print("11 - Sair")
    print("Televisões existentes: "+str(len(televisoes)))
    opc = int(input("Escolha uma opção: "))
    return opc

def criarTV():
    os.system("cls") or None
    n = input("Digite um nome para TV: ")
    tv = Televisao(n)
    televisoes.append(tv)
    print("Televisão criada")
    os.system("pause")

def excluirTV():
    os.system("cls") or None
    p = input("Digite a posição da TV a ser excluida: ")
    try:
        del televisoes[int(p)]
        print("TV excluida")
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja visualizar informação: ")
    try:
        televisoes[int(p)].info()
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def ligarTV():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja ligar: ")
    try:
        televisoes[int(p)].ligar()
        print("TV ligada")
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def desligarTV():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja desligar: ")
    try:
        televisoes[int(p)].desligar()
        print("TV desligada")
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def aum_canal():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja aumentar o canal: ")
    try:
        televisoes[int(p)].aument_canal()
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def dim_canal():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja diminuir o canal: ")
    try:
        televisoes[int(p)].diminui_canal()
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def aum_vol():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja aumentar o volume: ")
    try:
        televisoes[int(p)].aument_vol()
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def dim_vol():
    os.system("cls") or None
    p = input("Digite a posição da TV que deseja diminuir o volume: ")
    try:
        televisoes[int(p)].diminui_vol()
    except:
        print("Não existe televisão nesta posição")
    os.system("pause")

def listarTV():
    os.system("cls") or None
    i=0
    for t in televisoes:
        print(str(i)+" - "+t.nome)
        i+=1
    os.system("pause")

ret = Menu()

while ret != 11:
    if ret == 1:
        criarTV()
    elif ret == 2:
        excluirTV()
    elif ret == 3:
        informacoes()
    elif ret == 4:
        ligarTV()
    elif ret == 5:
        desligarTV()
    elif ret == 6:
        aum_canal()
    elif ret == 7:
        dim_canal()
    elif ret == 8:
        aum_vol()
    elif ret == 9:
        dim_vol()
    elif ret == 10:
        listarTV()

    ret = Menu()

os.system("cls") or None
print("Fim do programa")
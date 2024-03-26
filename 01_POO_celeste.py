import random 
class Personaje:

    def __init__(self,vida,ataque,nombre) :
        self.vida= vida
        self.ataque=ataque
        self.nombre=nombre

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño (self,daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
            
    def atacar_enemigo(self, enemigo):
        daño=random.randint(0,self.ataque)
        enemigo.recibir_daño(daño)
        print(f"{self.nombre} ataca a {enemigo.nombre} y le inflinge { daño} de daño ")

        if not enemigo.esta_vivo():
            print(f"{enemigo.nombre} fue vencido")


def main():
    Red=Personaje (100,20,"Red")
    Blue=Personaje (100,20,"Blue")

    while Red.esta_vivo() and Blue.esta_vivo():

        Red.atacar_enemigo(Blue) 
    
        if Blue.esta_vivo() :
            Blue.atacar_enemigo(Red)

    if Red.esta_vivo():

        print(f"{Red.nombre} GANA¡")
    else :
        print(f"{Blue.nombre} GANA ¡")

            
main()





    




    
    


    
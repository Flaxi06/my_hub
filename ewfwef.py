class Tank:
    def __init__(self , name , armor , damage):
        self.name = name 
        self.armor = armor
        self.damage = damage


    def __str__(self) :
        return self.name


    def shoot(self , enemy):
        print(f"по пали по {enemy}")
        enemy.health_down(enemy.damage)


    def health_down(self , damage):
        print(f"ЕСТЬ ПРОБИТИЕ , ПО НАМ ПОПАЛИ НА {damage} урона.")


class T34(Tank):
    pass

class Mouse(Tank):
    pass


t34 = T34("t34" , 100 , 50)
mouse = Mouse("МАУС" , 50 ,25) 

t34.shoot(mouse)
mouse.shoot(t34)



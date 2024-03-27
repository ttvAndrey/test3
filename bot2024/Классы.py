class Person():
    def __init__(self,name,hp,armor,attack,reaction) -> None:
        self.name=name
        self.hp=hp
        self.armor=armor
        self.attack=attack
        self.reaction=reaction
    def damage(self,enemy):
        if self.hp>0:
            print(f"{self.name} Атакует {enemy.name}")
            if self.attack>enemy.armor:
                Yron=self.attack-enemy.armor
                enemy.hp-=Yron
                print(f"У {enemy.name} Осталось {enemy.hp} hp")
            else:
                print(f"{self.name} не может пробить броню")
        else:
            print(f"{self.name} больше не может атаковать")
p1=Person("Naruto",hp=1000,armor=300,attack=100,reaction=100)
p2=Person("Jorno",hp=100,armor=900,attack=500,reaction=110)
while p1.hp>0 and p2.hp>0:
    if p1.reaction>p2.reaction:
        p1.damage(p2)
        p2.damage(p1)
    else:
        p2.damage(p1)
        p1.damage(p2)
        print(p2.hp)
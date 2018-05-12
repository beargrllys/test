import random

class Player:

    def __init__(self,name, attack, depense,Hp,life=True):
        self.name = name
        self.Hp = Hp
        self.attack = attack
        self.life = life
        self.depense = depense

    def depen(self, attacker):
        self.Hp -= (attacker-self.depense)
        print("플레이어가" + str(attacker) + "의 피해를 입었습니다.")
        if(self.Hp <= 0):
            self.life = False
            print("플레이어가 사망하였습니다.")
            exit(1)
        print("남은 HP: "+ str(self.Hp))

    def attackes(self, whos):
        print("플레이어가 "+ whos.name+ "에게 공격을 했습니다.")
        if(whos.depen(self.attack)):
            return 1
        return 0


class Character:  # B.O

    def __init__(self,name, Hp, attack, depense,life=True):
        self.name = name
        self.Hp = Hp
        self.attack = attack
        self.life = life
        self.depense = depense

    def depen(self, attacker):
        self.Hp -= (attacker-self.depense)
        print(self.name+ "이" + str(attacker)+"의 피해를 입었습니다.")
        print(self.name+"의 남은 HP: " + str(self.Hp))
        if(self.Hp <= 0):
            self.life = False
            print(self.name+ "이 죽었습니다.")
            return 1
        return 0

    def attacks(self, who):
        print(self.name+"이 "+ who.name+ "에게 공격을 했습니다.")
        who.depen(self.attack)


class GameController:

    def __init__(self):
        self.Player = Player(input("당신의 이름은?"),int(input("당신의 방어력은?")),int(input("당신의 공격력은?")),int(input("당신의 HP는?")))
        self.Creeper = Character("크리퍼", random.randint(100,300),random.randint(100,200),random.randint(10,50) )
        self.Zombie = Character("좀비", random.randint(200,500),random.randint(50,100),random.randint(20,80))
        self.Endermen = Character("앤더맨", random.randint(50,150),random.randint(100,150),random.randint(10,30))
        self.Spider = Character("거미", random.randint(100,200),random.randint(30,180),random.randint(60,100))
        self.Skeleton = Character("스켈레톤", random.randint(50,200),random.randint(90,180),random.randint(10,50))
        self.emelist = [self.Creeper, self.Zombie, self.Endermen, self.Spider, self.Skeleton]

    def playGame(self):
        print("게임을 시작합니다.")
        #플레이어 초기 설정
        i=0
        while(self.emelist != []):
            self.emelist[i % 5].attacks(self.Player)
            if(self.emelist[i % 5].Hp<=0):
                self.emelist.remove(self.emelist[i % 5])
            if(i%5==0):
                self.Player.attackes(self.Creeper)
            elif(i%5==1):
                self.Player.attackes(self.Zombie)
            elif (i % 5 == 2):
                self.Player.attackes(self.Endermen)
            elif (i % 5 == 3):
                self.Player.attackes(self.Spider)
            elif (i % 5 == 4):
                self.Player.attackes(self.Skeleton)
            i+=1

        print("플레이어의 남은 Hp:"+ str(Player.Hp))
        if(Player.Hp < 200):
            print("성공!")
        else:
            print("실패!")


# main
Minecraft_War = GameController()
Minecraft_War.playGame()
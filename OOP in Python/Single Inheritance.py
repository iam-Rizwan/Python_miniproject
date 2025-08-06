class father:
    def __init__(self):
        self.mother=input("Hey Dad type your mom name :") #mother= grandmother(gm)
        self.myfather=input("Hey Dad type your father name :") #father= grandfather(gf)
        self.he=input("Finally now! : Give me your name dad :")
class son(father):  
    def display(self):
        print("\n\nNow Here it is .")
        print(f"My grandmom is   Mrs.{self.mother}")
        print(f"My grandfather is Mr.{self.myfather}")
        print("AAAAAnnnnnnnnddddd")
        print(f"My dear father is Mr.{self.he}")

ans=son()
ans.display()
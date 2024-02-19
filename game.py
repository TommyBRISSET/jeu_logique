from tkinter import *      #Import du module tkinter
from tkinter import ttk
from tkinter import messagebox
from math import *         #Import du module math et random 
from random import * 
from player import *       #Import de nos classes
from case import *
from playsound import playsound #Import du module playsound et threading pour gérer le son de notre jeu
from threading import Thread

class Jeu:
    """Class Jeu ayant pour attribut main, présence d'une page tkinter ; caseConfig, permettant de dessiner les pions ;  
    j et i, le nombre de lignes et colonnes ; players, la liste des joueurs ; save_players,
    la sauvegarde du nombre de joueurs ; currentPlayer, le joueur du tour actuel et turn pour le joueur 
    a qui c'est le tour."""
    def __init__(self,main):
        self.__main = main
        self.__caseConfig = [
            [{
                "x": 25,
                "y": 25
            }],
            [{
                "x": 16,
                "y": 25
            },{
                "x": 34,    
                "y": 25
            }],
            [{
                "x": 25,
                "y": 16
            },{
                "x": 34,
                "y": 34
            },{
                "x": 16,
                "y": 34
            }]
        ]
        self.__j = 8
        self.__i = 5
        self.__players = []
        self.__save_players = []
        self.__currentPlayer = None
        self.__turn = 1
        
    def sound(self):
        """Fonction qui lance un son (pose de pion)"""
        playsound("./sons/son.mp3")
    def sound1(self):
        """Fonction qui lance un son (son de victoire)"""
        playsound("./sons/victory.wav")
        
    def start(self):
        """Fonction qui cree la fenetre du jeu """
        if self.__main != None:
            self.__main.destroy()
        if len(self.__players) < 2:
            messagebox.showerror(title="Erreur", message="Il n'y a pas assez de joueur enregistré")
            return
        self.__save_players = self.__players.copy()
        #print("la liste est",self.__save_players )
        self.__root = Tk()
        self.__root.title("Mini projet - 2")
        self.__root.configure(background='black')
        self.__root.resizable(False,False)
        self.__canvas_frame = Frame(self.__root, bg="black")
        self.__canvas_frame.grid(row=0,column=0)
        if self.__players[1].getId() == "ordinateur":
            self.__txtlabel3 = StringVar()
            self.__labelInfo3 = Label(self.__canvas_frame, textvariable= self.__txtlabel3,font=("Times", "20", "bold italic"))
            self.__labelInfo3.config(fg="white",bg="black")
            self.__labelInfo3.pack()
            self.updateLabels3()
        self.__canvas = Canvas(self.__canvas_frame)
        self.__canvas.config(width = self.__i*50, height = self.__j*50, highlightthickness=0, bd=0, bg="black")
        self.__canvas.bind('<Button-1>',self.onClick)
        self.__canvas.pack(pady=20, padx=20)
        
        self.__frame1 = Frame(self.__root, bg="black")
        self.__frame1.grid(row=1,column=0)
        self.__txtlabel2 = StringVar()
        self.__labelInfo2 = Label(self.__frame1, textvariable= self.__txtlabel2,font=("roboto",10))
        self.__labelInfo2.config(fg="white",bg="black")
        self.__labelInfo2.pack()
        self.__buttonReprendre = Button(self.__frame1, text='Sauvergarder la partie',width=20)
        self.__buttonReprendre.pack(pady=10)
        self.__buttonStart = Button(self.__frame1, text='Couleur des joueurs', width=20,command=self.info)
        self.__buttonStart.pack(pady=10)
        self.__buttonStart = Button(self.__frame1, text='règle du jeu', width=10,command=self.info1)
        self.__buttonStart.pack(pady=10)
        self.__txtlabel1 = StringVar()
        self.__labelInfo1 = Label(self.__frame1, textvariable= self.__txtlabel1,font=("roboto",10))
        self.__labelInfo1.config(fg="white",bg="black")
        self.__labelInfo1.pack()
        
        self.updateLabels()
        self.checkCurrentPlayer()
        self.createGrid(self.__i,self.__j)
        self.showGrid()
        self.__root.mainloop()
        
        
    def setRow(self, row):           # Getters and Setters
        self.__i = row
        
    def setColumn(self, column):
        self.__j = column
    
    def getCanvas(self):
        return self.__canvas
    
    def getCaseConfig(self):
        return self.__caseConfig
    
    def getPlayers(self):
        return self.__players
    
    def resetPlayers(self):
        self.__players=[]
    
    def setPlayers(self, players):
        self.__players = players
        self.__save_players = players
    
    def createGrid(self,i,j):
        """Fonction qui creer la grille de jeu."""
        self.__grid = []
        for x in range(i):
            self.__grid.append([])
            for y in range(j):
                self.__grid[x].append(Case(self,x,y))
                
    def showGrid(self):
        """Fonction qui dessine la grille de jeu."""
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                rec = self.__canvas.create_rectangle(50*i,j*50,50*(i+1),50*(j+1), width=2,outline=self.__currentPlayer.getColor())
                self.__grid[i][j].setRec(rec)
    
    def resetGrid(self):
        """Fonction qui remet la grille a zero."""
        self.createGrid(self.__i,self.__j)
        self.__canvas.delete("all")
        self.showGrid()
    
    def updateGrid(self):
        """Fonction qui met a jour la grille."""
        for line in self.__grid:
            for case in line:
                self.__canvas.delete(case.getRec())
        self.showGrid()
    
    def updateLabels(self):
        """Fonction qui montre la couleur associé aux joueurs"""
        self.__text=""
        a=len(self.__players)
        for i in range(a):
            if self.__players[i].getColor() == "white" or self.__players[i].getColor() == "red":
                self.__text1=("Le joueur "+str(self.__players[i].getId())+" a la couleur "+str(self.__players[i].getColor())+"\n")
                self.__text +=self.__text1
            else:
                self.__labelInfo1.config(bg="black")
        self.__txtlabel1.set(str(self.__text))
    
    def updateLabels2(self,x,y):
        self.__txt1=str("Le pion vient d'être posé dans\nla case de coordonnées : ["+str(y)+"] ["+str(x)+"].")
        self.__txtlabel2.set(self.__txt1)
    
    def updateLabels3(self):
        self.__txtlabel3.set("Vous affrontez l'ordinateur !!!")
    
    def info(self):
        """Fonction associe au boutton couleur des joueur et done des informations"""
        messagebox.showinfo("Couleur des joueurs", "Lors de la configuration du jeu, chaque joueur peut choisir sa couleur. Le joueur joue lorsque la grille de jeu est afficher avec sa couleur.")
        
    def info1(self):
        """Fonction associe au boutton regle de jeu et qui donne les regles du jeu."""
        messagebox.showinfo("règle du jeu","Entre 2 et 8 joueurs s’affrontent sur un plateau rectangulaire initialement vide comportant par défaut 8 lignes et 5 colonnes. Chaque joueur possède des pions d’une certaine couleur. \n Alternativement, chacun des joueurs va poser l’un de ses pions soit sur une case vide, soit sur une case contenant déjà un ou plusieurs de ses pions. \n Les cases situées dans les coins du plateau ont une capacité maximale de 2 pions, celles situées sur les bords mais pas dans les coins ont une capacité maximale de 3 pions, et enfin celles situées à l’intérieur du plateau ont une capacité maximale de 4 pions. \n Quand le nombre de pions sur une case est égal à la capacité maximale que celle-ci peut contenir, ces pions sont envoyés vers les cases adjacentes et la case se libère. Si sur l’une des cases adjacentes se trouvaient des pions du joueur le nouveau pion se rajoute à ceux-ci. Si sur l’une des cases adjacentes se trouvaient des pions adverses, ceux-ci sont capturés, ils changent de couleur et le nouveau pion se rajoute ensuite. \n Après un tel déplacement de pions, les cases adjacentes contiennent donc plus de pions qu’elles n’en avaient auparavant et peuvent donc à leur tour atteindre leur capacité maximale. Si c’est le cas, le phénomène se reproduit et ainsi de suite. On peut donc assister à une réaction en chaîne.")
                
    def onClick(self,e):
            """Fonction de jeu principale qui met a jour le plateau a chaque tour (clic de souris de chaque joueurs)"""
            x = floor(e.x/50) #i
            y = floor(e.y/50) #j
            case = self.__grid[x][y]
            if case.getOwner() != self.__currentPlayer and case.getOwner() is not None:
                if case.getValue() == 0:
                    case.setOwner(self.__currentPlayer)
                else:
                    return
            case.setOwner(self.__currentPlayer, False)
            case.addValue()
            last = self.checkCurrentPlayer()
            self.updateGrid()
            self.updateLabels2(x,y)
            self.__threadsound = Thread(target=self.sound)
            self.__threadsound.start()
            if self.__currentPlayer.getId()=="ordinateur":
                self.ordi()
            
    def ordi(self):
        """Fonction qui se declenche si partie avec joueur ordi selectionner et fait jouer celui ci en mode random"""
        x = randint(0,self.__i-1) #i
        y = randint(0,self.__j-1)#j
        #print("je suis",x,y)
        case = self.__grid[x][y]
        while case.getOwner() ==self.__players[0]:
            x = randint(0,self.__i-1) #i
            y = randint(0,self.__j-1)#j
            #print("je suis a nouveau",x,y)
            case = self.__grid[x][y]
        if case.getOwner() != self.__currentPlayer and case.getOwner() is not None:
            if case.getValue() == 0:
                case.setOwner(self.__currentPlayer)
            else:
                return
        case.setOwner(self.__currentPlayer, False)
        case.addValue()
        last = self.checkCurrentPlayer()
        self.updateGrid()
        self.updateLabels2(x,y)
        self.__threadsound = Thread(target=self.sound)
        self.__threadsound.start()
  
    def checkCurrentPlayer(self):
        """Fonction qui verifie le joueur actuel et renvoie celui ci"""
        if self.__currentPlayer == None:
            last = 0
            self.__currentPlayer = self.__players[0]
        elif self.__currentPlayer == self.__players[-1]:
            last = self.__players.index(self.__currentPlayer)
            self.__currentPlayer = self.__players[0]
            self.__turn+=1
        else:
            last = self.__players.index(self.__currentPlayer)
            self.__currentPlayer = self.__players[self.__players.index(self.__currentPlayer)+1]
        return last
    
    def addPlayer(self, player):
        """Fonction qui permet d'ajouter des joueurs et renvoie une erreur si le nombre de joueurs autorise est depasse."""
        if len(self.__players) >= 8:
            messagebox.showerror(title="Erreur", message="Il ne peut y avoir plus de 8 joueurs dans une partie")
            self.start()
            return
        self.__players.append(player)
        
    def adjacents(self,case):
        """Fonction qui verifie emplacement des pions et effectue le deplacement de ceci en fonction des regles du jeu"""
        cases = []
        for a in range(1,3):
            if a == (1):
                pos = -1
            else:
                pos = +1
            if (case.getI()+pos == -1 or case.getI()+pos == len(self.__grid)) and (case.getJ()+pos == -1 or case.getJ()+pos == len(self.__grid[0])):
                continue
            if case.getI()+pos == -1 or case.getI()+pos == len(self.__grid):
                #print("PosI", case.getJ()+pos)
                cases.append(self.__grid[case.getI()][case.getJ()+pos])
                continue
            if case.getJ()+pos == -1 or case.getJ()+pos == len(self.__grid[0]):
                cases.append(self.__grid[case.getI()+pos][case.getJ()])
                continue
            #print("PosJ", case.getJ()+pos)
            #print("PosI", case.getI()+pos)
            cases.append(self.__grid[case.getI()][case.getJ()+pos])
            cases.append(self.__grid[case.getI()+pos][case.getJ()])
        return cases
    
    def checkWin(self,player):
        """Fonction qui vérifie si un joueur a gagne"""
        if self.__turn < 2:
            return False
        win = True
        for line in self.__grid:
            for case in line:
                if case.getOwner() == player or case.getOwner() == None:
                    continue
                else:
                    win = False
        return win
    
    def verif(self,case):
        """Fonction qui verifie situation de la partie """
        player = case.getOwner()
        adjacents = self.adjacents(case)
        if self.checkWin(player):
            case.clear()
            self.end(player)
        if (len(adjacents) > case.getValue()):
            return
        case.clear()
        for c in adjacents:
            if c.getOwner() != player:
                c.setOwner(player)
            c.addValue()
    
    def end(self, player):
        """Fonction qui se declenche si la partie est termine"""
        self.__threadsound = Thread(target=self.sound1)
        self.__threadsound.start()
        a=randint(1,3)
        if a ==1:
            if not messagebox.askyesno("enquete satisfaction","Ce jeu vous a t-il plu?"):
                messagebox.showinfo("Aidez nous à l'améliorer","Veuillez nous préciser les différents bugs ou problèmes que vous rencontrez, à l'une des adresses mail suivantes : tommy.brisset@supinfo.com ou orlann.ferreira-dias-almeida@supinfo.com")
        if player.getId()=="ordinateur":
            if messagebox.askyesno("Fin de partie", "Le joueur " + str(player.getId()) + " a gagné \nVoulez-vous rejouer une partie ?"):
                self.__players = self.__save_players
                self.__root.destroy()
                game = Jeu(None)
                game.setRow(self.__i)
                game.setColumn(self.__j)
                game.setPlayers(self.__players )
                game.start()
            else:
                self.__root.destroy()
        if messagebox.askyesno("Fin de partie", "Le joueur " + str(player.getId()+1) + " a gagné \nVoulez-vous rejouer une partie ?"):
            self.__players = self.__save_players
            self.__root.destroy()
            game = Jeu(None)
            game.setRow(self.__i)
            game.setColumn(self.__j)
            game.setPlayers(self.__players )
            game.start()
        else:
            self.__root.destroy()
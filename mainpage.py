from tkinter import *                     #Import du module tkinter 
from tkinter import ttk
import tkinter as tk
from tkinter.colorchooser import askcolor
from game import *                        #Import de nos classes
from player import *

class MainPage:
    """Class Mainpage qui permet d'accéder à une page de configuration du jeu, elle a pour attribut game
    qui créer un objet de la class game et elle permet d'activer la fonction init """
    def __init__(self):
        self.__game = Jeu(self)
        self.__labelplayer=0
        self.init()
        
    def init(self):
        """fonction init qui initialise une fenêtre tkinter et qui a pour attribut row et colum que sont respectivement les lignes et colonnes 
        de notre tableau de jeu et nb_players qui contient le nombre de joueurs d'une partie"""
        self.__root = Tk()
        self.__root.title("Initialisation")
        self.__row=8
        self.__column= 5
        self.__root.geometry("250x375")
        self.__root.configure(background='#ffffff')
        self.__root.resizable(False,False)
        self.__frame1 = Frame(self.__root) 
        self.__labelChoix = Label(self.__root, text = "Page de configuration",font=("roboto",15),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__labelChoix.pack(pady=10)
        #choix du nombre de joueurs par ajout de ceux ci un par un, en choisissant une couleur. 
        self.__nb_players = 0
        self.__image1=tk.PhotoImage(file="./images/ajout.png")
        self.__add_player = Button(self.__root, text="Ajouter un joueur",image=self.__image1,font=("roboto",10),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__add_player.bind('<Button-1>',self.addPlayer)
        self.__add_player.pack()
        self.__txtlabel = StringVar()
        self.__labelInfo = Label(self.__root, textvariable= self.__txtlabel,font=("roboto",8),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__labelInfo.pack()
        #choix d'une partie contre l'ordinateur
        self.__image2=tk.PhotoImage(file="./images/ordi.png")
        self.__ordi = Button(self.__root, text="Jouer contre l'ordi",font=("roboto",10),image=self.__image2,command=self.ordi,bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__ordi.pack(pady=10)
        #choix de reprendre une parti arreter précédemment 
        self.__image3=tk.PhotoImage(file="./images/reprendre.png")
        self.__partie = Button(self.__root, text="Reprendre la partie",font=("roboto",10),image=self.__image3,bd=0,bg='#ffffff',activebackground='#ffffff')#ajouter command
        self.__partie.pack(pady=10)
        # choix du nombre de colonnes
        self.__frame1 = Frame(self.__root)
        self.__labelChoix1 = Label(self.__root, text = "Choisissez le nombre de colonnes ?",font=("roboto",10),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__labelChoix1.pack(pady=5)
        self.__listeProduits1=[3,4,5,6,7,8,9,10,11,12]
        self.__listeCombo1 = ttk.Combobox(self.__root, values=self.__listeProduits1)
        self.__listeCombo1.bind("<<ComboboxSelected>>",self.action1)
        self.__listeCombo1.current(2)
        self.__listeCombo1.pack()
        # choix du nombre de lignes
        self.__frame1 = Frame(self.__root) 
        self.__labelChoix2 = Label(self.__root, text = "Choisissez le nombre de lignes ?",font=("roboto",10),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.__labelChoix2.pack(pady=5)
        self.__listeProduits2=[3,4,5,6,7,8,9,10]
        self.__listeCombo2 = ttk.Combobox(self.__root, values=self.__listeProduits2)
        self.__listeCombo2.bind("<<ComboboxSelected>>",self.action2)
        self.__listeCombo2.current(5)
        self.__listeCombo2.pack()
        #button qui permet de de lancer une partie
        self.__image=tk.PhotoImage(file="./images/b12.png")
        self.bouton = Button(self.__root, text="Start",image=self.__image, command=self.start,font=("roboto",10),bd=0,bg='#ffffff',activebackground='#ffffff')
        self.bouton.pack(pady = 20)
        
        self.__root.mainloop()
    
    def updateLabels(self):
        """Fonction qui montre le nombre de joueurs que l'on cree pour notre partie de jeu"""
        if self.__labelplayer>1:
            self.__txtlabel.set("Le nombre de joueurs actuels est " + str(self.__labelplayer)+".")
        else:
            self.__txtlabel.set("Le nombre de joueur actuel est " + str(self.__labelplayer)+".")

    def start(self):
        "fonction associé au button start et qui lance une partie"
        self.__game.start()
        
    def ordi(self):
        """Fonction qui permet de lancer une partie contre l'ordinateur. (celui ci joue de manière random)"""
        self.__game.resetPlayers()
        self.__game.addPlayer(Player("white", self.__game,1))
        self.__game.addPlayer(Player("red", self.__game,"ordinateur"))#joueur ordi 
        self.__game.start()
        
    def addPlayer(self, event):
        """fonction associé au button 'ajouter joueur' qui laisse le choix de
        la couleur au joueurs et qui incrémente le nombre de joueurs"""
        color = askcolor(title="Choix de la couleur du joueur")[1]
        self.__game.addPlayer(Player(color, self.__game, self.__nb_players))
        self.__nb_players+=1
        self.__labelplayer+=1
        self.updateLabels()
        #print(self.__game.getPlayers())
          
    def action1(self,event):
        """fonction qui récupère la valeur choisi dans la combobox pour choisir le nombre de colonnes """
        self.__game.setRow(int(event.widget.get()))
        return self.__row
       
    def action2(self,event):
        """fonction qui récupère la valeur choisi dans la combobox pour choisir le nombre de lignes """
        self.__game.setColumn(int(event.widget.get()))
        return self.__column
    
    def destroy(self):
        """fonction qui détruit la fenetre tkinter correspondant a la page de configuration """
        self.__root.destroy()
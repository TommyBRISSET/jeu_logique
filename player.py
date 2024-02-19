class Player:
    """Class player qui permet de creer un joueur pour le jeu.
    Ses attributs sont color , pour la couleur associe a un joueur ; game pour la partie en cours du joueur 
    et id qui permet d'identifier le joueur."""
    def __init__(self,color,game,id):
        self.__color = color
        self.__game = game
        self.__id = id
        self.__point = 0
        
    #Getters et setters
    def getPoint(self):
        return self.__point
    
    def getColor(self):
        return self.__color
    
    def getId(self):
        return self.__id
    
    def addPoint(self):
        """fonction qui ajoute 1 point a une case"""
        self.__point += 1
        
    def removePoint(self):
        """fonction qui enleve un point a un joueur et supprime le joueur
        sur une case si il n'y a plus de point sur celle-ci. """
        self.__point -= 1
        if self.__point == 0:
            #print("Remove Point")
            self.__game.getPlayers().remove(self)
        #print(self.__game.getPlayers())
    
    
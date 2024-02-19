class Case:
    """Class Case qui permet de créer les cases de notre plateau de jeu , elle a pour attribut value, la valeur de cette case ;
    owner, le détenteur des pions sur cette case ; game, pour la partie de jeu ; pions, qui permet de dessiner le nombre de pions
    sur cette case ; j et i, le nombre de lignes et colonnes et rec la case"""
    def __init__(self,game,i,j):
        self.__value = 0
        self.__owner = None
        self.__game = game
        self.__pions = []
        self.__i = i
        self.__j = j
        self.__rec = None
    
    def getOwner(self):     #Getters and Setters 
        return self.__owner
        
    def getI(self):
        return self.__i
    
    def getJ(self):
        return self.__j
    
    def getValue(self):
        return self.__value
    
    def setRec(self, rec):
        self.__rec = rec
        
    def getRec(self):
        return self.__rec
        
    def addValue(self):
        """Fonction qui ajoute 1 à la valeur de la case."""
        self.__value += 1
        self.verif()
        self.drawPions()
        
    def verif(self):
        """Fonction qui lance une fonction vérif dans la class game."""
        self.__game.verif(self)
        
    def drawPions(self):
        """Fonction qui dessine les points dans les cases."""
        self.clearPions()
        for i in range(self.__value):
            pos = self.__game.getCaseConfig()[self.__value-1][i]
            circle = self.__game.getCanvas().create_oval(self.__i*50+pos["x"]-5, self.__j*50+pos["y"]-5, self.__i*50+pos["x"]+5,self.__j*50+pos["y"]+5, fill=self.__owner.getColor())
            self.__pions.append(circle)
    
    def clear(self):
        """Fonction qui met la valeur d'une case a 0."""
        self.__value = 0
        self.drawPions()
    
    def clearPions(self):
        '''Fonction qui enlève les pions présent dans une case.'''
        for e in self.__pions:
            self.__game.getCanvas().delete(e)
        self.__pions = []
            
    def setOwner(self, owner, remove=True):
        """Fonction qui associe à une case un player qui détiendra les pions sur cette case."""
        if self.__owner is not None and remove == True:
            self.__owner.removePoint() 
        if owner != self.__owner:
            owner.addPoint()
        self.__owner = owner
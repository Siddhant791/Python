class Player:
    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playerName=playerName
        self.playerCountry=playerCountry
        self.playerAge=playerAge
        self.noOfMatches = noOfMatches
        self.noOfRuns=noOfRuns
        self.noOfWickets=noOfWickets
        
class Team:
        
    def getMinRuns(self,listOfPlayers):
        runsList=[]
        lowestRuns = 0
        for i in listOfPlayers:
            runsList.append(i.noOfRuns)
        lowestRuns = min(runsList)
        for i in listOfPlayers:
            if i.noOfRuns == lowestRuns:
                return i
            
    def getMaxWickets(self,listOfPlayers):
        runsList=[]
        maxWickets = 0
        for i in listOfPlayers:
            runsList.append(i.noOfWickets)
        maxWickets = max(runsList)
        for i in listOfPlayers:
            if i.noOfWickets == maxWickets:
                return i
    
if __name__=='__main__':
    n = int(input())
    listOfPlayers=[]
    for i in range(n):
        playerName=str(input())
        playerCountry=str(input())
        playerAge=int(input())
        noOfMatches=int(input())
        noOfRuns=int(input())
        noOfWickets=int(input())
        listOfPlayers.append(Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets))
    team = Team()
    outputPlayer1 = team.getMinRuns(listOfPlayers)
    outputplayer2=team.getMaxWickets(listOfPlayers)
    
    print(outputPlayer1.playerName)
    print(outputPlayer1.noOfRuns)
    print(outputPlayer1.playerCountry)
    print(outputplayer2.playerName)
    print(outputplayer2.noOfWickets)
    print(outputplayer2.playerCountry)
        
        
# 5
# Sachin
# India
# 40
# 350
# 15000
# 120
# Klusnar
# SouthAfrica
# 37
# 270
# 3000
# 250
# Dhoni
# India
# 38
# 345
# 12000
# 0
# RickyPonting
# Australia
# 42
# 290
# 11000
# 3
# Dravid
# India
# 39
# 320
# 11200
# 12
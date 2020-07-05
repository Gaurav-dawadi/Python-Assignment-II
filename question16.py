"""Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player."""


class fifaPlayer():

    def __init__(self, name, age, position, nationality, overallRating):
        self.name = name
        self.age = age
        self.position = position
        self.nationality = nationality
        self.overallRating = overallRating

    def playerInfo(self):

        print("-------PLAYER INFO-------")
        print('\n')
        print("Name of Player: ", self.name)
        print("Age of Player: ", self.age)
        print("Position of Player: ", self.position)
        print("Nationality of Player: ", self.nationality)
        print("OverallRatings of Player: ", self.overallRating)
        print("-------------------------------------")
        print('\n')

    def awardsWon(self):
        print('\n')
        print("Bundesliga Young Player of the Hinrunde: 2010")
        print("Korean Footballer of the Year: 2013, 2014, 2017, 2019")
        print("Tottenham Hotspur Player of the Season: 2018–19")
        print("Tottenham Hotspur Goal of the Season: 2017–18, 2018–19")
        print("Premier League Goal of the Month: November 2018, December 2019")
        print("AIPS ASIA Best Asian Male Athlete: 2018")
        print("FIFA FIFPro World11 nominee: 2019")
        print("London Player of the Year: 2018–19 Premier League")
    
playerOne = fifaPlayer('Son Heung Min', 27, 'Left Wing', 'South Korea', 90)
playerOne.playerInfo()
print("--------Individuals Award One--------")
playerOne.awardsWon()
print("------------------------------------------")           

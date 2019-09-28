import discord

class FightClub:
    def __init__(self):
        # Global Flags
        self.tournamentName = ""
        self.tournamentStatus = False
        self.registrationStatus = False

    # Discord Listeners

    # Discord Handlers
    def createTournament(self, name):
        if not self.tournamenStatus:
            self.tournamentStatus = True
            self.tournamentName = name
            print("Tournament Created: {0}".format(name))
            return True
        return False

    def closeTournament(self):
        self.tournamentStatus = False

    def openRegistration(self):
        # If the tournament is not open open a default tournament
        if not self.tournamentStatus:
            print("A Tournament has not been opened.")
            return False
        self.registrationStatus = True
        return True

    def closeRegistration(self):
        self.registrationStatus = False

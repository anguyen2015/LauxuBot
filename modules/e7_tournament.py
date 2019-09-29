class FightClub:
    def __init__(self):
        # Global Flags
        self.tournamentName = ""
        self.tournamentStatus = False
        self.registrationStatus = False

    # Discord Handler
    def handleCreateTournament(self, name):
        if not self.tournamentStatus:
            self.createTournament(name)
            return True
        return False
        
    # Discord Method
    def createTournament(self, name):
        self.tournamentStatus = True
        self.tournamentName = name
        print("Tournament Created: {0}".format(name))

    def closeTournament(self):
        self.tournamentStatus = False
        self.tournamentName = ""

    def openRegistration(self):
        # If the tournament is not open open a default tournament
        if not self.tournamentStatus:
            print("A Tournament has not been opened.")
            return False
        self.registrationStatus = True
        return True

    def closeRegistration(self):
        self.registrationStatus = False

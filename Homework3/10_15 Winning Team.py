# Kaitlyn Sourignosack
# 1824497

class Team:
    def __init__(self, name= 'none', teamwins = 0, team_losses = 0):
        self.teamname = name
        self.teamwins =  teamwins
        self.team_losses =  team_losses

    def get_win_percentage(self):
        team_wins =  float (self.teamwins)
        team_losses =  float (self.team_losses)
        win_percentage = float (team_wins / (team_wins + team_losses))
        return win_percentage


if __name__ == '__main__':
    c = 0
    attributes = []
    while c < 3:
        attributes.append(input())
        c += 1

    # Variables storing attributes from inputs
    name1 = str (attributes[0])
    teamwins1 =  int (attributes[1])
    team_losses1 = int (attributes[2])
    # print (attributes)

    team1 = Team (name1, teamwins1, team_losses1)

    if team1.get_win_percentage() > 0.5:
        print('Congratulations, Team', team1.teamname, 'has a winning average!')
    else:
        print('Team', team1.teamname, 'has a losing average.')


    # winpercent = team1.get_win_percentage()


    #
    # print ('win percent:', winpercent)



    # team1.get_win_percentage()
    # print (team1.winpercent)

    # print (team1.get_win_percentage())
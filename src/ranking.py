import csv
import re
# Empate 1 ponto
# Vitoria 3 pontos
# Derrota 0 pontos


class Ranking:
    def __init__(self, input, output):
        # Pegando os argumentos passados pela task.py
        self.input = input
        self.output = output
        with open(self.input, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            games = getGames(spamreader)
            results = getTeams(games)
            sort = sorted(results.items(), key=lambda x: x[1], reverse=1)
            lastScore = 0
            lastPosition = 0
            classification = []
            classification.append(["Place","Team","Score"])
            with open(self.output, 'w+', newline="") as file:
                writer = csv.writer(file)
                for index, tup in enumerate(sort):
                    name, score = tup
                    team = ""
                    if(index == 0):
                        lastPosition = 1
                        lastScore = score
                        classification.append([name, lastPosition, str(score) + " pts"])
                    elif(score == lastScore):
                        classification.append([name, lastPosition, str(score) + " pts"])
                    else:
                        lastScore = score
                        lastPosition = len(classification)
                        lastPosition = lastPosition + 1
                        classification.append([name, lastPosition, str(score) + " pts"])
                for team in classification:
                    writer.writerow(team)                
    pass

def getTeams(games):
    results = {}
    for game in games:
        # {'team-one': 'Bulls', 'score-one': '4', 'team-two': 'Otters', 'score-two': '1'}
        teamOne = game['team-one']
        teamTwo = game['team-two']
        scoreOne = 0
        scoreTwo = 0

        if(game['score-one'] > game['score-two']):
            scoreOne = 3
        elif(game['score-one'] < game['score-two']):
            scoreTwo = 3
        else:
            scoreOne = 1
            scoreTwo = 1

        if(teamOne in results):
            results[teamOne] = results[teamOne] + scoreOne
        else:
            results[teamOne] = scoreOne

        if(teamTwo in results):
            results[teamTwo] = results[teamTwo] + scoreTwo
        else:
            results[teamTwo] = scoreTwo
    return results

def getGames(spamreader):
    games = []
    for index, [team1, team2] in enumerate(spamreader):
        if (index):
            teamOneScore = re.findall(r'\d+', team1)
            teamOneName = re.findall(r'[a-zA-Z]+', team1)
            teamTwoScore = re.findall(r'\d+', team2)
            teamTwoName = re.findall(r'[a-zA-Z]+', team2)
            game = {}
            game['team-one'] = ' '.join(teamOneName)
            game['score-one'] = int(teamOneScore[0])
            game['team-two'] = ' '.join(teamTwoName)
            game['score-two'] = int(teamTwoScore[0])
            games.append(game)
    return games
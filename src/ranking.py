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
                
                print(classification)
                
                
                # classification.append(' '.join(tup))
                # converted.append(dict(tup))

            # ignore for now
            # header = ['Place', 'Team', 'Score']
            # data = {'Bulls': 7, 'Otters': 0, 'Dragons': 4, 'The Kraken': 1, 'Sluggers': 4}

            # with open(output, 'w', encoding='UTF8') as f:
            #     writer = csv.writer(f)

            #     # write the header
            #     writer.writerow(header)

            #     # write the data
            #     writer.writerow(data)
    pass


'''

Teams:

Bulls
Dragons
Otters
Sluggers
The Kraken

[
    {
        team1: Bulls,
        score1: 4,
        team2: Otters,
        score2: 1,
    },
    {
        team1: Dragons,
        score1: 2,
        team2: The Kraken,
        score2: 2,
    },
    {
        team1: Otters,
        score1: 1,
        team2: Dragons,
        score2: 2,
    },
    .....
]
-------------
[
    {
        name: Bulls,
        score: 0
    },
]

'''

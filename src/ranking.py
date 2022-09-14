import csv
import re

class Ranking:

    """ Getting arguments passed by the task.py"""

    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.classification = []
        self.main()

    def main(self):

        ''' Get a csv of games and returns a csv with the classification '''

        results = self.get_teams()
        sort = sorted(results.items(), key=lambda x: x[1], reverse=1)
        last_score = 0
        last_position = 0
        self.classification.append(['Place', 'Team', 'Score'])
        with open(self.output, 'w+', newline='', encoding='utf8') as file:
            writer = csv.writer(file)
            for index, team in enumerate(sort):
                (name, score) = team
                team = ''
                if index == 0:
                    last_position = 1
                    last_score = score
                    self.classification.append([last_position, name, 
                            str(score) + ' pts'])
                elif score == last_score:
                    self.classification.append([last_position, name,
                            str(score) + ' pts'])
                else:
                    last_score = score
                    last_position = len(self.classification)
                    self.classification.append([last_position, name,
                            str(score) + ' pts'])
            for team in self.classification:
                writer.writerow(team)

    def get_teams(self):

        '''
            Get all the matches into the file and returns an
            object with the teams and the total points of each one
        '''

        results = {}
        games = self.get_matches()
        for game in games:
            team_one = game['team-one']
            team_two = game['team-two']
            score_one = 0
            score_two = 0

            if game['score-one'] > game['score-two']:
                score_one = 3
            elif game['score-one'] < game['score-two']:
                score_two = 3
            else:
                score_one = 1
                score_two = 1

            if team_one in results:
                results[team_one] = results[team_one] + score_one
            else:
                results[team_one] = score_one

            if team_two in results:
                results[team_two] = results[team_two] + score_two
            else:
                results[team_two] = score_two
        return results


    def get_matches(self):
        ''' Read the file input and convert it to a list of Matches '''
        games = []
        with open(self.input, newline='', encoding='utf8') as csvfile:
            file = csv.reader(csvfile, delimiter=',',
                    quotechar='|')
            for (index, [team1, team2]) in enumerate(file):
                if index:
                    score_one = re.findall(r'\d+', team1)
                    name_one = re.findall(r'[a-zA-Z]+', team1)
                    score_two = re.findall(r'\d+', team2)
                    name_two = re.findall(r'[a-zA-Z]+', team2)
                    game = {}
                    game['team-one'] = ' '.join(name_one)
                    game['score-one'] = int(score_one[0])
                    game['team-two'] = ' '.join(name_two)
                    game['score-two'] = int(score_two[0])
                    games.append(game)
            return games

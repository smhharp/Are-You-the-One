import random
'''
Are You the One? Simulator
'''

'Define contestant class'
class Contestant:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return(self.name)

def truthBooth(self):
    pass

if __name__ == '__main__':
    # initialize contestants
    contestants = [Contestant('Olivia', 'M'), Contestant('Dom', 'M'), Contestant('Kem', 'M'), Contestant('Jess', 'F'), 
                   Contestant('Sam', 'M'), Contestant('Amber', 'F'), Contestant('Camilla', 'F'), Contestant('Montana', 'F'), 
                   Contestant('Chris', 'M'), Contestant('Marcel', 'M'), Contestant('Chloe', 'F'), Contestant('Harley', 'M'), 
                   Contestant('Jonny', 'M'), Contestant('Amelia', 'F'), Contestant('Gabby', 'F'), Contestant('Simon', 'M')]

    # create perfect matches randomly
    perfect_matches = []
    random.shuffle(contestants)
    for i in range(0, len(contestants)-1, 2):
        perfect_matches.append((contestants[i], contestants[i+1]))
        
    # introduce player to game, to the contestants
    print('Welcome to Are You the One!')
    'GIVE INSTRUCTIONS ON HOW TO PLAY'

    # list contestants
    random.shuffle(contestants)
    print('Meet the contestants:', end=' ')
    for i in range(len(contestants)-1):
        print(contestants[i], end = ', ')
    print('and ' + str(contestants[len(contestants)-1]) + '.')

    'Main gameplay'
    all_pairs_correct = False
    while all_pairs_correct == False:
        # count number of loops it takes to complete
        week_count = 1
        print('Welcome to Week ' + str(week_count) +'!')

        # ask player to pair new matches
        matches = []
        print('It is time to couple up the pairs you think are perfect matches!')
        for i in range(1, 9):
            #matches.append(input('Please enter couple ' + str(i) + ' in the form of (Contestant name, Contestant name)'))
            pass

        # check number of correct pairs
        print(matches)
        correct_pairs = 0
        '''
        # algorithm 1
        for x in perfect_matches:
            if (x in matches):
                correct_pairs += 1
        
        # algorithm 2
        for x in matches:
            if (x in perfect_matches):
                correct_pairs += 1
        '''
        # algorithm 3
        def recr_correct_pairs(n):
            #base case
            if n == -1:
                if perfect_matches[0] in matches:
                    return 1
                else:
                    return 0
            if perfect_matches[n] in matches:
                return 1 + recr_correct_pairs(n-1)
            return recr_correct_pairs(n-1)
        recr_correct_pairs(7)
        if (correct_pairs == 8):
            print('You win!')
            all_pairs_correct = True
        else:
            print('You picked', correct_pairs, 'pairs correct!')

        # truth booth - return one pair and whether it is correct or not
        if all_pairs_correct == True:
            pass
        else:   
            print('Pick a couple to go to the truth booth!')

        all_pairs_correct = True

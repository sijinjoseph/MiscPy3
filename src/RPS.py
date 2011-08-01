'''
Created on Jun 10, 2011

@author: sjoseph
'''
from collections import defaultdict
import random
from pprint import pprint

def beat(move):
    if move == 'R':
        return 'P'
    elif move == 'S':
        return 'R'
    elif move == 'P':
        return 'S'
    
def random_move():
    return random.choice(['R', 'P', 'S'])

def get_best_predictor(tallies, current_run_number):
    best_tally = 0
    best_predictor = None
    
    for predictor, tally in tallies.items():
        avg_tally = tally / ( (current_run_number * (current_run_number + 1)) / 2)
        if avg_tally >= best_tally:
            best_tally = avg_tally
            best_predictor = predictor
    
    #print("best = {}".format(best_predictor))
    return best_predictor, best_tally

class PredictN:
    lookback = 1
    history = ""
    frequency = {}
    
    def __init__(self, lookback = 1):
        self.lookback = lookback
        
    def __str__(self):
        return "Predict{0}".format(self.lookback)
    
    def add_history(self, move):
        self.history += move
        
        if len(self.history) > self.lookback:
            key = self.history[(self.lookback + 1) * -1:-1]
            if key not in self.frequency:
                self.frequency[key] = defaultdict(int)
            
            self.frequency[key][move] += 1
    
    def predict(self):
        if self.lookback == 0:
            return (random_move(), 0.5)
        
        key = self.history[(self.lookback) * -1:]
        if key not in self.frequency:
            return (random_move(), 0.5)
        else:
            distribution = self.frequency[key]
            all_sum = sum(distribution.values())
            max_count = max(distribution.values())
            max_key = list(filter(lambda k: distribution[k] == max_count, distribution.keys()))[0]
            
            return (max_key, max_count / all_sum)
                    
    def print_frequency(self):
        pprint(self.frequency)
 
#if input == "":
#    current_run_number = 1
#    predictors = [PredictN(0), PredictN(1), PredictN(2), PredictN(3), PredictN(4), PredictN(5), PredictN(6)]
#    tallies = {}
#    for p in predictors:
#        tallies[p] = 0
#
#    predictions = []
#    output = random_move()
#else:
#    if len(predictions) > 0:
#        for k in range(len(predictions)):
#            if predictions[k] == input:
#                tallies[predictors[k]] += current_run_number
#                
#        for p in predictors:
#            p.add_history(input)
#      
#    predictions = [p.predict()[0] for p in predictors]
#    output = beat(predictions[predictors.index(get_best_predictor(tallies, current_run_number))])
#    current_run_number += 1
            
if __name__ == '__main__':
    predictors = [PredictN(0), PredictN(1), PredictN(2), PredictN(3), PredictN(4), PredictN(5), PredictN(6)]
    tallies = { p:0 for p in predictors }
    runs = 10000
    output_success = 0
    predictions = []
    input = ""
    output = ""
    for current_run_number in range(1, runs + 1):
        if len(predictions) > 0: 
            for k in range(len(predictions)):
                    if predictions[k] == input:
                        tallies[predictors[k]] += current_run_number
                    
            for p in predictors:
                p.add_history(input)
            
            if input == output:
                output_success += 1
        
        input = random.choice(['R', 'P', 'S'])      
            
        predictions = [p.predict()[0] for p in predictors]
        best_predictor, best_tally = get_best_predictor(tallies, current_run_number)
        if best_tally > 0.5:
            output = predictions[predictors.index(best_predictor)]
        else:
            output = random_move()        
        
    for p in predictors:
        print("{} : {}".format(p, tallies[p] / ((runs * (runs + 1))/2) ))
        
    print("Output success rate : {0}".format(output_success / runs))
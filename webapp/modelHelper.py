import numpy as np
import pandas as pd

class ModelHelper():
    def __init__(self):
        self.squad_predictions = pd.read_csv('static/data/squad_strength_final.csv', encoding='latin-1')
        
    def matchup_simulator(self, team1, team2, num_sims = 10000):
        print(team1,team2)
        
        
        # Get Squad Percentages
        S1_percent = self.squad_predictions.loc[self.squad_predictions.Squad==team1]['% of Points Taken'].values[0]
        S2_percent = self.squad_predictions.loc[self.squad_predictions.Squad==team2]['% of Points Taken'].values[0]
        
        # Calculating Probability that S1 wins given the two squad percentages S2_prob = 1 - S1_prob
        
        S1_prob = ((S1_percent - (S1_percent*S2_percent)) / (S1_percent + S2_percent - (2 * S1_percent * S2_percent)))
        
        # Simulating match num_sims times, returns an array of 0 and 1, 1 = squad one wins
        
        match_results = np.random.binomial(n=1, p = S1_prob, size = num_sims)
        
        # Wins per num_sims
        
        S1_win_percent = np.mean(match_results)
        
        results = (f"{team1} Wins{S1_win_percent: .2%} of the time against {team2} across {num_sims} simulations.")
        
        return(results)
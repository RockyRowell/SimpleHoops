# create players' offensive skills

# libraries
import pandas as pd
import numpy as np
import random
import json



class OffenseGeneration:
    def __init__(self, player, physicals):
        self.player = player
        
        self.height = physicals[0]
        self.weight = physicals[1]
        self.wingspan = physicals[2]
        self.strength = physicals[3]
        self.vertical = physicals[4]
        self.footwork = physicals[5]
        self.speed = physicals[6]
        self.stamina = physicals[7]
        
        self.wingspan_difference = self.wingspan - self.height
        
        self.min = 0
        self.max = 100
        
    
    def offense_generation(self):
        three_point = self.three_gen()
        mid_range = self.mid_gen()
        free_throw = self.freethrow_gen()
        post_scoring = self.postscoring_gen()
        
        offense_data = {
            'Player': [self.player],
            'Three Point': [three_point],
            'Mid Range': [mid_range],
            'Free Throw': [free_throw],
            'Post Scoring': [post_scoring]
        }
        
        return pd.DataFrame(offense_data)
        
    
    
    def three_gen(self):
        # establish range
        threeRange = {
            (68, 72, -3, -1): {"mean": 85, "sd": 5},
            (68, 72, 0, 3): {"mean": 80, "sd": 5},
            (68, 72, 4, 6): {"mean": 75, "sd": 5},
            
            (73, 78, -3, -1): {"mean": 80, "sd": 5},
            (73, 78, 0, 3): {"mean": 75, "sd": 5},
            (73, 78, 4, 6): {"mean": 70, "sd": 5},

            (79, 84, -3, -1): {"mean": 75, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 65, "sd": 5},

            (85, 90, -3, -1): {"mean": 70, "sd": 5},
            (85, 90, 0, 3): {"mean": 65, "sd": 5},
            (85, 90, 4, 6): {"mean": 60, "sd": 5},
        }
        
        # gather parameters
        for range_key, params in threeRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate three
        three = np.random.normal(mean, sd)
       
        # round height
        three = round(three)
        
        # correct outliers
        if three < self.min: three = self.min
        elif three > self.max: three = self.max
        
        # return height
        return three
        
        
        
    def mid_gen(self):
        # establish range
        midRange = {
            (68, 72, -3, -1): {"mean": 70, "sd": 5},
            (68, 72, 0, 3): {"mean": 75, "sd": 5},
            (68, 72, 4, 6): {"mean": 80, "sd": 5},
            
            (73, 78, -3, -1): {"mean": 70, "sd": 5},
            (73, 78, 0, 3): {"mean": 80, "sd": 5},
            (73, 78, 4, 6): {"mean": 85, "sd": 5},

            (79, 84, -3, -1): {"mean": 70, "sd": 5},
            (79, 84, 0, 3): {"mean": 80, "sd": 5},
            (79, 84, 4, 6): {"mean": 85, "sd": 5},

            (85, 90, -3, -1): {"mean": 75, "sd": 5},
            (85, 90, 0, 3): {"mean": 80, "sd": 5},
            (85, 90, 4, 6): {"mean": 70, "sd": 5},
        }
        
        # gatheter parameters
        for range_key, params in midRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate three
        mid = np.random.normal(mean, sd)
       
        # round height
        mid = round(mid)
        
        # correct outliers
        if mid < self.min: mid = self.min
        elif mid > self.max: mid = self.max
        
        # return height
        return mid
    
    
    
    def freethrow_gen(self):
        # establish range
        freeRange = {
            (68, 72, -3, -1): {"mean": 90, "sd": 5},
            (68, 72, 0, 3): {"mean": 85, "sd": 5},
            (68, 72, 4, 6): {"mean": 80, "sd": 5},
            
            (73, 78, -3, -1): {"mean": 85, "sd": 5},
            (73, 78, 0, 3): {"mean": 80, "sd": 5},
            (73, 78, 4, 6): {"mean": 75, "sd": 5},

            (79, 84, -3, -1): {"mean": 75, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 65, "sd": 5},

            (85, 90, -3, -1): {"mean": 65, "sd": 5},
            (85, 90, 0, 3): {"mean": 60, "sd": 5},
            (85, 90, 4, 6): {"mean": 55, "sd": 5},
        }
        
        # gatheter parameters
        for range_key, params in freeRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate three
        free = np.random.normal(mean, sd)
       
        # round height
        free = round(free)
        
        # correct outliers
        if free < self.min: free = self.min
        elif free > self.max: free = self.max
        
        # return height
        return free
    
    
    
    def postscoring_gen(self):
        # establish range
        postRange = {
            (68, 72, -3, -1): {"mean": 50, "sd": 5},
            (68, 72, 0, 3): {"mean": 60, "sd": 5},
            (68, 72, 4, 6): {"mean": 70, "sd": 5},
            
            (73, 78, -3, -1): {"mean": 60, "sd": 5},
            (73, 78, 0, 3): {"mean": 70, "sd": 5},
            (73, 78, 4, 6): {"mean": 75, "sd": 5},

            (79, 84, -3, -1): {"mean": 65, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 80, "sd": 5},

            (85, 90, -3, -1): {"mean": 70, "sd": 5},
            (85, 90, 0, 3): {"mean": 75, "sd": 5},
            (85, 90, 4, 6): {"mean": 85, "sd": 5},
        }
        
        # gather parameters
        for range_key, params in postRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate post scoring
        post = np.random.normal(mean, sd)
       
        # round height
        post = round(post)
        
        # correct outliers
        if post < self.min: post = self.min
        elif post > self.max: post = self.max
        
        # return height
        return post
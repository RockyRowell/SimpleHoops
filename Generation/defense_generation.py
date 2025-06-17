# create players' defensive skills

# libraries
import pandas as pd
import numpy as np
import random



class DefenseGeneration:
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
        
    def defense_generation(self):
        perimeter_defense = self.perimeter_gen()
        post_defense = self.post_gen()
        defensive_rebounding = self.defrebounding_gen()
        offensive_rebounding = self.offrebounding_gen()
        steal = self.steal_gen()
        block = self.block_gen()
        
        defense_data = {
            'Player': [self.player],
            'Perimeter Defense': [perimeter_defense],
            'Post Defense': [post_defense],
            'Defensive Rebounding': [defensive_rebounding],
            'Offensive Rebounding': [offensive_rebounding],
            'Steal': [steal],
            'Block': [block]
        }
        
        return pd.DataFrame(defense_data)
    
    
    def perimeter_gen(self):
        # establish range
        perimeterRange = {
            (68, 72, -3, -1): {"mean": 60, "sd": 5},
            (68, 72, 0, 3): {"mean": 70, "sd": 5},
            (68, 72, 4, 6): {"mean": 80, "sd": 5},

            (73, 78, -3, -1): {"mean": 65, "sd": 5},
            (73, 78, 0, 3): {"mean": 75, "sd": 5},
            (73, 78, 4, 6): {"mean": 85, "sd": 5},

            (79, 84, -3, -1): {"mean": 55, "sd": 5},
            (79, 84, 0, 3): {"mean": 65, "sd": 5},
            (79, 84, 4, 6): {"mean": 75, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 45, "sd": 5},
            (85, 90, 0, 3): {"mean": 55, "sd": 5},
            (85, 90, 4, 6): {"mean": 65, "sd": 5},
        }

        # determine range
        for range_key, params in perimeterRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)
        
        # round value
        value = round(value)
        
        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
    
    
    def post_gen(self):
        # establish range
        post_range = {
            (68, 72, -3, -1): {"mean": 40, "sd": 5},
            (68, 72, 0, 3): {"mean": 50, "sd": 5},
            (68, 72, 4, 6): {"mean": 60, "sd": 5},

            (73, 78, -3, -1): {"mean": 50, "sd": 5},
            (73, 78, 0, 3): {"mean": 60, "sd": 5},
            (73, 78, 4, 6): {"mean": 70, "sd": 5},

            (79, 84, -3, -1): {"mean": 60, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 80, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 70, "sd": 5},
            (85, 90, 0, 3): {"mean": 80, "sd": 5},
            (85, 90, 4, 6): {"mean": 85, "sd": 5},
        }

        # determine range
        for range_key, params in post_range.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)

        # round value
        value = round(value)

        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
    
    def defrebounding_gen(self):
        # establish range
        defreb_range = {
            (68, 72, -3, -1): {"mean": 40, "sd": 5},
            (68, 72, 0, 3): {"mean": 50, "sd": 5},
            (68, 72, 4, 6): {"mean": 60, "sd": 5},

            (73, 78, -3, -1): {"mean": 50, "sd": 5},
            (73, 78, 0, 3): {"mean": 65, "sd": 5},
            (73, 78, 4, 6): {"mean": 80, "sd": 5},

            (79, 84, -3, -1): {"mean": 60, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 80, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 70, "sd": 5},
            (85, 90, 0, 3): {"mean": 80, "sd": 5},
            (85, 90, 4, 6): {"mean": 85, "sd": 5},
        }

        # determine range
        for range_key, params in defreb_range.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)

        # round value
        value = round(value)

        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
    
    def offrebounding_gen(self):
        # establish range
        offreb_range = {
            (68, 72, -3, -1): {"mean": 40, "sd": 5},
            (68, 72, 0, 3): {"mean": 50, "sd": 5},
            (68, 72, 4, 6): {"mean": 60, "sd": 5},

            (73, 78, -3, -1): {"mean": 50, "sd": 5},
            (73, 78, 0, 3): {"mean": 65, "sd": 5},
            (73, 78, 4, 6): {"mean": 80, "sd": 5},

            (79, 84, -3, -1): {"mean": 60, "sd": 5},
            (79, 84, 0, 3): {"mean": 70, "sd": 5},
            (79, 84, 4, 6): {"mean": 80, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 70, "sd": 5},
            (85, 90, 0, 3): {"mean": 80, "sd": 5},
            (85, 90, 4, 6): {"mean": 85, "sd": 5},
        }

        # determine range
        for range_key, params in offreb_range.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)

        # round value
        value = round(value)

        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
    
    def steal_gen(self):
        # establish range
        steal_range = {
            (68, 72, -3, -1): {"mean": 60, "sd": 5},
            (68, 72, 0, 3): {"mean": 70, "sd": 5},
            (68, 72, 4, 6): {"mean": 80, "sd": 5},

            (73, 78, -3, -1): {"mean": 55, "sd": 5},
            (73, 78, 0, 3): {"mean": 65, "sd": 5},
            (73, 78, 4, 6): {"mean": 75, "sd": 5},

            (79, 84, -3, -1): {"mean": 50, "sd": 5},
            (79, 84, 0, 3): {"mean": 60, "sd": 5},
            (79, 84, 4, 6): {"mean": 70, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 40, "sd": 5},
            (85, 90, 0, 3): {"mean": 50, "sd": 5},
            (85, 90, 4, 6): {"mean": 60, "sd": 5},
        }

        # determine range
        for range_key, params in steal_range.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)

        # round value
        value = round(value)

        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
    
    def block_gen(self):
        # establish range
        block_range = {
            (68, 72, -3, -1): {"mean": 30, "sd": 5},
            (68, 72, 0, 3): {"mean": 40, "sd": 5},
            (68, 72, 4, 6): {"mean": 50, "sd": 5},

            (73, 78, -3, -1): {"mean": 50, "sd": 5},
            (73, 78, 0, 3): {"mean": 60, "sd": 5},
            (73, 78, 4, 6): {"mean": 70, "sd": 5},

            (79, 84, -3, -1): {"mean": 55, "sd": 5},
            (79, 84, 0, 3): {"mean": 65, "sd": 5},
            (79, 84, 4, 6): {"mean": 75, "sd": 5},
            
            (85, 90, -3, -1): {"mean": 65, "sd": 5},
            (85, 90, 0, 3): {"mean": 75, "sd": 5},
            (85, 90, 4, 6): {"mean": 85, "sd": 5},
        }

        # determine range
        for range_key, params in block_range.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.wingspan_difference <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break

        # generate value
        value = np.random.normal(mean, sd)

        # round value
        value = round(value)

        # correct outliers
        if value < self.min: value = self.min
        elif value > self.max: value = self.max

        return value
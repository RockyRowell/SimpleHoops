# create players' physicals

# libraries
import pandas as pd
import numpy as np
import random
import json



class PhysicalsGeneration:
    def __init__(self, player):
        self.player = player
        
        self.height = self.height_gen()
        self.weight = self.weight_gen()
        self.wingspan = self.wingspan_gen()
        self.strength = self.strength_gen()
        self.vertical = self.vertical_gen()
        self.footwork = self.footwork_gen()
        self.speed = self.speed_gen()
        self.stamina = self.stamina_gen()
        
        
    def get_attributes(self):
        return [self.height, self.weight, self.wingspan, self.strength, self.vertical,
                self.footwork, self.speed, self.stamina]
    
    def physical_generation(self):
        # convert height
        feet = self.height // 12
        inches = self.height % 12
        
        height_fixed = f"{feet}'{inches}"
        
        # add values into df
        physicals = pd.DataFrame([{'Player': self.player, 'Height': height_fixed, 
                                  'Weight': self.weight, 'Wingspan': self.wingspan , 
                                  'Strength': self.strength, 'Vertical': self.vertical, 
                                  'Footwork': self.footwork, 'Speed': self.speed,
                                  'Stamina': self.stamina}])
        
        # return df
        return physicals
       
        
    
    def height_gen(self):
        # establish min, max, mean, sd height
        minHeight = 68; maxHeight = 90; meanHeight = 79; sdHeight = 3
        
        # generate height
        height = np.random.normal(meanHeight, sdHeight)
       
        # round height
        height = round(height)
        
        # correct outliers
        if height < minHeight: height = minHeight
        elif height > maxHeight: height = maxHeight
        
        # return height
        return height
    
    
    
    def weight_gen(self):
        # establish weight ranges
        weightRange = {
            (68, 72): {'min': 170, 'max': 210, 'mean': 165, 'sd': 5},
            (73, 78): {'min': 185, 'max': 235, 'mean': 200, 'sd': 10},
            (79, 84): {'min': 215, 'max': 275, 'mean': 240, 'sd': 10},
            (85, 90): {'min': 250, 'max': 330, 'mean': 280, 'sd': 10}
        }
        
        # gather weight parameters
        for range_key, params in weightRange.items():
            if range_key[0] <= self.height <= range_key[1]:
                min = params['min']
                max = params['max']
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate weight
        weight = np.random.normal(mean, sd)
        
        # round weight
        weight = round(weight)
        
        # correct outliers
        if weight < min: weight = min
        elif weight > max: weight = max
        
        # return weight
        return weight
    
    
    
    def wingspan_gen(self):
        # establish min and max
        min = self.height - 3; max = self.height + 6
        
        # generate wingspan
        wingspan = np.random.randint(min, max)
        
        # return value
        return wingspan
    
    
    
    def strength_gen(self):
        # establish min and max
        min = 0; max = 100

        # establish strength range
        strengthRange = {
            (68, 72, 170, 190): {'mean': 45, 'sd': 10},
            (68, 72, 191, 210): {'mean': 75, 'sd': 10},
            (73, 78, 185, 200): {'mean': 50, 'sd': 10},
            (73, 78, 201, 215): {'mean': 70, 'sd': 10},
            (73, 78, 216, 235): {'mean': 80, 'sd': 10},
            (79, 84, 215, 235): {'mean': 60, 'sd': 10},
            (79, 84, 236, 255): {'mean': 75, 'sd': 10},
            (79, 84, 256, 275): {'mean': 85, 'sd': 8},
            (85, 90, 250, 275): {'mean': 70, 'sd': 10},
            (85, 90, 276, 295): {'mean': 80, 'sd': 10},
            (85, 90, 296, 330): {'mean': 90, 'sd': 5}
        }
        
        # gather rest of strength parameters
        for range_key, params in strengthRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.weight <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
            
        # generate strength
        strength = np.random.normal(mean, sd)
        
        # round value
        strength = round(strength)
        
        # correct outliers
        if strength < min: strength = min
        elif strength > max: strength = max
        
        # return value
        return strength
            
    
    
    def vertical_gen(self):
        # establish min and max
        min = 0; max = 100

        # establish range
        verticalRange = {
            (68, 72, 170, 190): {'mean': 85, 'sd': 5},
            (68, 72, 191, 210): {'mean': 75, 'sd': 5},
            (73, 78, 185, 200): {'mean': 80, 'sd': 5},
            (73, 78, 201, 215): {'mean': 70, 'sd': 5},
            (73, 78, 216, 235): {'mean': 60, 'sd': 5},
            (79, 84, 215, 235): {'mean': 75, 'sd': 5},
            (79, 84, 236, 255): {'mean': 65, 'sd': 5},
            (79, 84, 256, 275): {'mean': 55, 'sd': 5},
            (85, 90, 250, 275): {'mean': 70, 'sd': 5},
            (85, 90, 276, 295): {'mean': 60, 'sd': 5},
            (85, 90, 296, 330): {'mean': 50, 'sd': 5},
        }

        # gather rest of vertical parameters
        for range_key, params in verticalRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.weight <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate vertical
        vertical = np.random.normal(mean, sd)
        
        # round value
        vertical = round(vertical)
        
        # correct outliers
        if vertical < min: vertical = min
        elif vertical > max: vertical = max
        
        # return value
        return vertical
    
    
    
    def footwork_gen(self):
        # establish min and max
        min = 0; max = 100
        
        # establish range
        footworkRange = {
            (68, 72, 170, 190): {'mean': 85, 'sd': 5},
            (68, 72, 191, 210): {'mean': 75, 'sd': 5},
            (73, 78, 185, 200): {'mean': 80, 'sd': 5},
            (73, 78, 201, 215): {'mean': 70, 'sd': 5},
            (73, 78, 216, 235): {'mean': 60, 'sd': 5},
            (79, 84, 215, 235): {'mean': 85, 'sd': 5},
            (79, 84, 236, 255): {'mean': 75, 'sd': 5},
            (79, 84, 256, 275): {'mean': 65, 'sd': 5},
            (85, 90, 250, 275): {'mean': 80, 'sd': 5},
            (85, 90, 276, 295): {'mean': 70, 'sd': 5},
            (85, 90, 296, 330): {'mean': 60, 'sd': 5},
        }
        
        # gather rest of vertical parameters
        for range_key, params in footworkRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.weight <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate vertical
        footwork = np.random.normal(mean, sd)
        
        # round value
        footwork = round(footwork)
        
        # correct outliers
        if footwork < min: footwork = min
        elif footwork > max: footwork = max
        
        # return value
        return footwork
    
    
    
    def speed_gen(self):
        # establish min and max
        min = 0; max = 100
        
        # establish range
        speedRange = {
            (68, 72, 170, 190): {'mean': 90, 'sd': 5},
            (68, 72, 191, 210): {'mean': 80, 'sd': 5},
            (73, 78, 185, 200): {'mean': 85, 'sd': 5},
            (73, 78, 201, 215): {'mean': 75, 'sd': 5},
            (73, 78, 216, 235): {'mean': 65, 'sd': 5},
            (79, 84, 215, 235): {'mean': 80, 'sd': 5},
            (79, 84, 236, 255): {'mean': 70, 'sd': 5},
            (79, 84, 256, 275): {'mean': 60, 'sd': 5},
            (85, 90, 250, 275): {'mean': 75, 'sd': 5},
            (85, 90, 276, 295): {'mean': 65, 'sd': 5},
            (85, 90, 296, 330): {'mean': 55, 'sd': 5},
        }
        
        # gather rest of vertical parameters
        for range_key, params in speedRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.weight <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate vertical
        speed = np.random.normal(mean, sd)
        
        # round value
        speed = round(speed)
        
        # correct outliers
        if speed < min: speed = min
        elif speed > max: speed = max
        
        # return value
        return speed
    
    
    
    def stamina_gen(self):
        # establish min and max
        min = 0; max = 100
        
        # establish range
        staminaRange = {
            (68, 72, 170, 190): {'mean': 90, 'sd': 5},
            (68, 72, 191, 210): {'mean': 85, 'sd': 5},
            (73, 78, 185, 200): {'mean': 90, 'sd': 5},
            (73, 78, 201, 215): {'mean': 85, 'sd': 5},
            (73, 78, 216, 235): {'mean': 80, 'sd': 5},
            (79, 84, 215, 235): {'mean': 85, 'sd': 5},
            (79, 84, 236, 255): {'mean': 80, 'sd': 5},
            (79, 84, 256, 275): {'mean': 75, 'sd': 5},
            (85, 90, 250, 275): {'mean': 80, 'sd': 5},
            (85, 90, 276, 295): {'mean': 75, 'sd': 5},
            (85, 90, 296, 330): {'mean': 70, 'sd': 5},
        }
        
        # gather rest of vertical parameters
        for range_key, params in staminaRange.items():
            if range_key[0] <= self.height <= range_key[1] and range_key[2] <= self.weight <= range_key[3]:
                mean = params['mean']
                sd = params['sd']
                break
        
        # generate vertical
        stamina = np.random.normal(mean, sd)
        
        # round value
        stamina = round(stamina)
        
        # correct outliers
        if stamina < min: stamina = min
        elif stamina > max: stamina = max
        
        # return value
        return stamina
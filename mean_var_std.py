import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain 9 numbers")
    
    matrix = np.array(list).reshape(3,3)
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()],
        
    }
    
    return calculations

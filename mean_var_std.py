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
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()],
    }
    
    return calculations

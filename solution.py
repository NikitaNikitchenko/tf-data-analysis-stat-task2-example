import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 784664358 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.008
    y = x - a
    
    return a+y.max(), a+ y.max()/(1-p)**(1/len(y))

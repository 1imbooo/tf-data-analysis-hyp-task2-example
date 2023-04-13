import pandas as pd
import numpy as np
from scipy.stats import ks_2samp, cramervonmises_2samp


chat_id = 661128504 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.03
    cramer = cramervonmises_2samp(x, y)
    
    if cramer.pvalue < alpha:
        return True
    else:
        return False

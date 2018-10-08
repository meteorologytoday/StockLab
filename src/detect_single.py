import numpy as np
from scipy import stats
from scipy import signal
import pprint
import StockAnalysis as SA

def analysis(data):

    # remove NaN, inf
    data_clean = data[np.isfinite(data)] 
    
    # Detect
    ana = SA.getAnalysis(data)

    long_term  = data[-20:]
    short_term = data[-5:]

    avg_price = np.mean(long_term)

    long_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(long_term)), long_term)
    short_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(short_term)), short_term)
  
    variability = np.mean(np.abs((data_clean[1:] - data_clean[:-1]) / avg_price))
  
    detrend = signal.detrend(data_clean) 
    power = np.abs(np.fft.fft(detrend)) ** 2.0
    tot_power = np.sum(power)
    n = int(np.floor(len(detrend) / 30.0))
    sw_rel_pow = np.sum(power[n:]) / tot_power

    return {
        'long_slope'  : long_slope, 
        'short_slope' : short_slope,
        'avg_price'   : avg_price,
        'variability' : variability,
        'sw_rel_pow'  : sw_rel_pow,
    }


import numpy as np 

'''
> Repetitive behaviour anaysis
Mahdi Zarei : 06-21-2019

parameters
> data; 
    X and Y
> win size; 
    Tie window size for clculation of the statistical parameters values in that interval
> thigmo_thr;
    Thigmotaxis margin value        

Return:
> 1. repitition index and their durations
> 2. thigmotaxix index and the rekated durations
'''        

class trajectory:
    def   __init__(self, X , Y , 
                   win = 500, 
                   cutting_threshold = 400,
                   thigmo_thr = 0.1, 
                   thigmo_lower_thr = 0.3, 
                   thigmo_upper_thr = 0.7,                   
                   immobility_tolerance_val = 0.01):        

        y_min = np.min(Y)
        y_max = np.max(Y)
        x_min = np.min(X)
        x_max = np.max(X)

        dta_X_std = [np.std(X [i:i + win]) for i in range(len(X) -win)]
        dta_Y_std = [np.std(Y [i:i + win]) for i in range(len(Y) -win)]       

        x_interval = np.max(X ) - np.min(X )
        y_interval = np.max(Y ) - np.min(Y )

        '''
        Detecting the Thigmotaxis areas; setting the "sliding_win_stat_DEV" to "0".
        One of the coordinates (e.g. X) std used in the calculations
        '''
        sliding_win_stat_DEV = []
        thigmotaxis_count = 0
        for i in range(len( X) - win):
            if  (np.average( Y [i:i + win]) < y_min + (thigmo_thr * y_interval )or
                 np.average( Y [i:i + win]) > y_max - (thigmo_thr * y_interval )or
                 np.average( X [i:i + win]) < x_min + (thigmo_thr * x_interval) or
                 np.average( X [i:i + win]) > x_max - (thigmo_thr * x_interval)):
                sliding_win_stat_DEV.append(0)
                thigmotaxis_count = thigmotaxis_count + 1
            else:
                sliding_win_stat_DEV.append ( dta_X_std [i] )

        '''
        Repetitive movement detection;
        Deviation of std_X a std_Y in the non_thigmtaxis (tank's central part) 
        are used to detect the STATIONARY behaviour.
        '''
        randomness = 0
        for i in range(len(Y) - win -1):
            if  (np.abs (dta_X_std [i] - dta_X_std [i+1] )< 1e-2 and
                 np.abs (dta_Y_std [i] - dta_Y_std [i+1] )< 1e-2 and
                 sliding_win_stat_DEV [i] != 0 ):
                sliding_win_stat_DEV [i] = 1            
            if ((np.abs (dta_X_std [i] - dta_X_std [i+1] ) > 1e-2 or
                 np.abs (dta_Y_std [i] - dta_Y_std [i+1] ) > 1e-2) and
                sliding_win_stat_DEV [i] != 0 ):
                randomness = randomness + 1           
        '''
        Repetition INTERVALS calculation;
        '''                
        cycle_set= {}
        start_flg = 1
        i = 0    
        cycle_idx = 0
        while (i < len(sliding_win_stat_DEV)):
            if sliding_win_stat_DEV[i] == 1 and start_flg == 1:
                start = i 
                start_flg = 0
                while (sliding_win_stat_DEV[i] == 1 ) :
                    i = i + 1
                end = i 
                cycle_set[cycle_idx] = [start, end] 
                cycle_idx = cycle_idx + 1
                start_flg = 1

            else:
                i = i + 1       

        '''
        Repetition INDEX calculation;
        '''
        Rep_idx_temp = 0
        for m in range(len(cycle_set)):    
            if cycle_set[m][1] - cycle_set[m][0] > cutting_threshold:
                Rep_idx_temp = Rep_idx_temp + (cycle_set[m][1] - cycle_set[m][0])
        Rep_idx = Rep_idx_temp 

        print (' Repetition index = {}, \n Thigmotaxis index = {}, \n Randomness index = {}'
               .format(Rep_idx/len(X), thigmotaxis_count/len(X) , randomness/len(X) ))
        
        self.repetition_idx = Rep_idx/len(X) 
        self.cycling_set = cycle_set  
        self.thigmotaxis_idx = thigmotaxis_count/len(X)

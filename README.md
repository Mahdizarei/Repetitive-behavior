

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


```python

>> import numpy as np
>> from trajectory import *
>> trajectory(X, Y)
 Repetition index = 0.9443333333333334

'''

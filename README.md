

# Repetitive behaviour anaysis
## Mahdi Zarei : 06-21-2019


parameters:
* data: 
    X and Y
* win size:
    - Tie window size for clculation of the statistical parameters values in that interval
* thigmo_thr:
    - Thigmotaxis margin value        
Return:
* 1. Repitition index (result.repetition_idx)
* 2. Repetitive movements duration (result.cycling_set)


```python

>> import numpy as np
>> from trajectory import *
>> result = trajectory(X , Y , win = 500, cutting_threshold = 700)
>> result.repetition_idx 
     0.443333333333334
>> result.cycling_set
    {[2,2004]: [4520, 8499]}
'''

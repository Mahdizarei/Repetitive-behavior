

# Repetitive behaviour anaysis
* Mahdi Zarei : 06-21-2019

parameters:
* Input data: X and Y
    - X: animal movement along x axis across time (X= X(t)).     
    - Y: animal movement along Y axis across time (Y= Y(t)). 
* win size:
    - Time window size for clculation of the statistical parameters values in that interval.
   
Return:
* 1. Repitition index ( result.repetition_idx )
* 2. Repetitive movements duration ( result.cycling_set )


## Testing the library on an example data:

```python
>> from trajectory import *
>> result = trajectory(X , Y , win = 500, cutting_threshold = 700)
>> result.repetition_idx 
     0.4433335
>> result.cycling_set
    {[2,2004]: [4520, 8499]}
'''

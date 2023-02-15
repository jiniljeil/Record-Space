## 새 열 추가하기
```python
import numpy as np 

arr = np.array([[1,2,3], 
                [4,5,6], 
                [7,8,9]])
col = [1, 0, 1] 

added_col = np.c_[arr, col] 

"""
[[1,2,3,1],
 [4,5,6,0],
 [7,8,9,1]]
"""
```
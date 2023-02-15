## DataFrame 생성

```python
import pandas as pd
df = pd.DataFrame({'gender': arr[:,0],
                   'age': arr[:,1], 
                   'income': arr[:,2],
                   'score': arr[:,3],
                   'cluster':arr[:,4]})
```

## CSV 파일 읽기

```python
df = pd.read_csv('FILE PATH') 
print(df)
```

## 컬럼 이름 추가

```python 
df.columns = ['num', 'text']
```

## 컬럼 삭제 

```python
df.drop(['컬럼 이름1', '컬럼 이름2', ...], inplace=True, axis=1)
```
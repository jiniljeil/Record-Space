# next_permutation 

STL에서 ```#include <algorithm> ```을 추가하면 순열을 구할 수 있다. 

함수에 배열의 주소 또는 iterator를 넣으면 사용 가능하다. 
- next_permutation : 다음 순열을 구하고 true를 반환, 다음 순열이 없다면 false를 반환
- prev_permutation : 이전 순열을 구하고 true를 반환, 이전 순열이 없다면 false를 반환

```C++ 
// 첫번째 인자가 구하고자 하는 순열의 시작, 두번째 인자가 순열의 끝
bool next_permutation (BidirectionalIterator first, BidirectionalIterator last);

// 아래처럼 직접 비교함수 삽입 가능
bool next_permutation (BidirectionalIterator first, BidirectionalIterator last, Compare comp);

// 첫번째 인자가 구하고자 하는 순열의 시작, 두번째 인자가 순열의 끝
bool prev_permutation (BidirectionalIterator first, BidirectionalIterator last);

// 아래처럼 직접 비교함수 삽입 가능
bool prev_permutation (BidirectionalIterator first, BidirectionalIterator last, Compare comp);
```

### 사용 예시 
```C++ 

do { 
    ... 
} while ( next_permutation(v.begin(), v.end())) ; 
```

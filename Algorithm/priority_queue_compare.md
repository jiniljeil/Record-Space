# Priority Queue

### 기본 형태  

```C++ 
#include <queue>
priority_queue<int, vector<int>, greater<int>> pq; // 작은 값이 맨 앞
priority_queue<int, vector<int>, less<int>> pq ; // 큰 값이 맨 앞
```

### 구조체를 priority queue 에 넣기

```C++ 
struct Point { 
    int result, curr_dir ;  
    int x, y ; 
}

struct compare { 
    bool operater() (const Point& p1, const Point& p2) { 
        return p1.result < p2.result ; 
    }
}

priority_queue<Point, vector<Point>, compare> pq ; 
```

위의 경우 result 값이 큰 순서대로 heap에 나열된다. 
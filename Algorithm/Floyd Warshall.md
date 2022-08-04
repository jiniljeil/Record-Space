# Floyd Warshall Algorithm

플로이드-와샬 알고리즘은 <strong>"모든 정점에서 모든 정점으로의 최단 경로"</strong>를 구하고 싶을 때 사용된다. 

음의 사이클이 없다면, 가중치가 음의 정수일 때도 사용 가능하다. 

Dynamic Programming 방식

```C++
DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j]) ; 
```

### 시간 복잡도 

플로이드-와샬 알고리즘은 모든 정점을 거치는 알고리즘이기 때문에 3중 for문을 사용하여 시간 복잡도는 $O(V^3)$이다. 

```C++
void floyd_warshall() { 
    for (int k = 0 ; k < n ; k++) { 
        for (int i = 0 ; i < n ; i++) { 
            for (int j = 0 ; j < n; j++) {
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j]) ; 
            }
        }
    }
}
```
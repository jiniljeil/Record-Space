# Bipartite Matching 

## 시간 복잡도
$O(V * E)$

## 이분 매칭 기본 코드

```C++
#include <iostream> 
#include <vector> 
#include <cstring> 
#define MAX 1001
using namespace std ;

vector<int> persons[MAX] ; 
int d[MAX] ; 
int visited[MAX] ; 
int N, M ; 

bool dfs(int k ) {
    for (int i = 0 ; i < persons[k].size(); i++) { 
        int t = persons[k][i]; 
        if (visited[t]) continue; 
        visited[t] = true ;
        if ( d[t] == 0 || dfs(d[t])) { 
            d[t] = k ; return true ;  
        }
    }
    return false; 
}
int main(void) { 
    ios::sync_with_stdio(false); cin.tie(0) ; 

    cin >> N >> M ; 

    for (int i = 0, n = 0; i < N ; i++) { 
        cin >> n ; 
        for (int j = 0, k = 0 ; j < n ;j++) { 
            cin >> k ; 
            persons[i + 1].push_back(k) ; 
        }
    }

    int cnt = 0 ; 
    for (int i = 1; i <= N; i++) { 
        memset(visited, false, sizeof(visited)) ; 
        if (dfs(i)) cnt++; 
    }

    cout << cnt << '\n'; 

    return 0 ; 
}
```
## BFS를 수행하면서 최솟값을 구해야하는 경우 

1. visited 값을 MAX 값으로 초기화 
2. if ( visited[dir_y][dir_x] >= result ) 일 때 queue에 push

### 예제 코드 (BOJ 6087)
```C++ 
#include <iostream> 
#include <string> 
#include <queue> 

#define MAX 101
using namespace std ;

int H, W; 
char MAP[MAX][MAX] ; 
int visited[MAX][MAX] ; 
int dx[4] = {-1, 0, 1, 0} ; 
int dy[4] = { 0, 1, 0,-1} ; 
int start_x = -1, start_y = -1 ; 
int end_x = -1, end_y = -1 ; 
typedef struct point { 
    int result ; 
    int curr_dir ; 
    int x, y ; 
} Point ; 

void BFS() { 
    queue<Point> Q; 
    for (int i = 0 ; i < 4 ; i++)  {
        Point p = {0, i, start_x, start_y}; 
        Q.push(p) ; 
    }
    visited[start_y][start_x] = 0 ; 

    while (!Q.empty()) { 
        Point curr = Q.front(); 
        Q.pop() ; 

        for (int i = 0 ; i < 4; i++) { 
            int dir_x = curr.x + dx[i] ; 
            int dir_y = curr.y + dy[i] ; 
            int cnt = curr.result ; 
            if ( dir_x < 0 || dir_x >= W || dir_y < 0 || dir_y >= H) continue;  
            if ( MAP[dir_y][dir_x] == '*') continue ; 
            if ( curr.curr_dir != i ) cnt++;  
            if ( visited[dir_y][dir_x] >= cnt) { 
                visited[dir_y][dir_x] = cnt ; 
                Point next = {cnt, i, dir_x, dir_y} ; 
                Q.push(next) ; 
            }
        }
    }

    cout << visited[end_y][end_x] << '\n'; 
}

void Input() { 
    cin >> W >> H ; 

    for (int i = 0 ; i < H ; i++) { 
        string s ; 
        cin >> s ; 
        for (int j = 0; j < W; j++) { 
            MAP[i][j] = s[j] ;
            visited[i][j] = 1e8; 

            if ( MAP[i][j] == 'C') { 
                if ( start_x == -1 && start_y == -1 ) {
                    start_y = i ; start_x = j ; 
                } else { 
                    end_y = i ; end_x = j ; 
                } 
            }
        }
    }
}

int main(void) { 
    ios::sync_with_stdio(false); 
    cin.tie(0) ; 

    Input() ;
    BFS(); 

    return 0 ;
}
```
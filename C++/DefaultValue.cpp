#include <iostream> 
#include <assert.h>
using namespace std; 

// Correct Conducting
int sum_default1(int a = 1, int b = 2, int c = 3) { 
    return a + b + c ; 
}

/* Compile Error
    함수에 전달되는 인자가 왼쪽에서부터 오른쪽으로 채워지기 때문에, 오른쪽부터 Default Value 를 정의해야한다. 
    Because the argument sent to the function is filled from left to right, 
    default value in function must be defined from right to left. 
    DefaultValue.cpp:12:40: error: missing default argument on parameter 'c'
    
    int sum_default2(int a, int b = 2, int c) { 
        return a + b + c ; 
    }
*/

int main(void) { 

    cout << "[TestCase]" << '\n'; 

    assert(sum_default1() == 6) ; // true 
    assert(sum_default1(5,5) ==  13) ; // true 
    assert(sum_default1(2) == 7) ;

    cout << "Test Clear" << '\n'; 
    return 0 ;
}
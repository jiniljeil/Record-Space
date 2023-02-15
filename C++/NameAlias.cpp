#include <iostream> 
#include <assert.h>

namespace Test1 {
    int num1 = 1; 
    int num2 = 2 ;

    namespace Test2 { 
        int num1 = 3; 
        int num2 = 4;

        namespace Test3 { 
            int num1 = 5;  
            int num2 = 6; 
        }
    }
}

int main(void) { 

    std::cout << "[NameAlias Test] " << '\n' ; 
    
    namespace T1=Test1 ; 
    namespace T2=Test1::Test2 ;
    namespace T3=Test1::Test2::Test3; 

    assert(T1::num1 == 1) ; 
    assert(T1::num2 == 2) ; 

    assert(T2::num1 == 3) ; 
    assert(T2::num2 == 4) ; 

    assert(T3::num1 == 5) ; 
    assert(T3::num2 == 6) ; 

    std::cout << "Test Clear" << '\n' ; 
}
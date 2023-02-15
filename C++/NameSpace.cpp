#include <iostream> 
#include <assert.h> 

// 하나의 프로젝트를 만들 때 여러 명에서 작업할 경우 지정한 함수 명이 같을 수도 있다.  
// 그러한 경우를 대비하여, 이와 같이 NameSpace 를 사용해주면, 
// 겹치는 일을 방지할 수 있다. 

// using 선언을 통해서 이름 공간의 지정 없이 호출 가능 

namespace FirstCompany { 
    void func() { 
        std::cout << "First Company Function" << '\n'; 
    }
    namespace Team { 
        int num = 3 ; 
        void introduction() { 
            std::cout << "Team in First Company Function" << '\n'; 
        }
    }
}

namespace SecondCompany {
    void func() {  
        std::cout << "Second Company Function" << '\n'; 
    }   
    namespace Team { 
        int num = 5; 
        void introduction() { 
            std::cout << "Team in Second Company Function" << '\n'; 
        }
    }
}

int main(void) {

    FirstCompany::func(); 
    SecondCompany::func();  

    FirstCompany::Team::introduction() ;
    SecondCompany::Team::introduction() ; 

    assert(FirstCompany::Team::num == 3) ; 
    assert(SecondCompany::Team::num == 5) ; 

    std::cout << "Test Clear" << '\n';

    return 0 ;
}
#include <iostream>


void foo() {}

int main()
{
//    void *ptr;
//    std::cout << *ptr << std::endl;
//    std::cout << ptr+1;

//    int *iptr = new int(5);
//    std::cout << "iptr: " << iptr << std::endl;
//    std::cout << "*iptr: " << *iptr << std::endl;

//    int i1, i2;
//    int * const ptr1 = &i1;
//    const int* ptr2 = &i1;
//    const int* const ptr3 = &i1;
//    *ptr1 = 5;
//    ptr2 = &i2;
//    *ptr2 = 5;
//    ptr3 = &i2;
//    *ptr3 = 5;

//    auto pf = &foo;
//    pf + 1;

    int var = 12;
    int *ptr1;
    ptr1 = &var;
    int **ptr2 = &ptr1;
    int ***ptr3 = &ptr2;

    std::cout  << std::endl;
    std::cout << "&ptr2 = " <<

    return 0;
}

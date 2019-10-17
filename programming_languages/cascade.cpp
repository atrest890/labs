#include <iostream>

int cascade(int a)
{
    if (a == 0 || a == 1) return 1;
    else return cascade(a-1) + cascade(a - 2);
}

int main()
{
    int a;
    std::cout << "Enter a number: "; std::cin >> a;
    std::cout << "Answer: " << cascade(a) << std::endl;
    return 0;
}

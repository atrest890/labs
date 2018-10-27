#include <iostream>

int repeated(int a, int b, int c)
{
    if (a < b) return c;
    else return (repeated(a-b, b, c+1));
    с = 0;
}

int main()
{
    int a, b, c;
    std::cout << "Enter numbers:" << std::endl;
    std::cin >> a >> b >> c;
    std::cout << "Answer: " << repeated(a, b, c) << std::endl;
    return 0;
}

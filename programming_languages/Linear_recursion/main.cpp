#include <iostream>

int linear(int a, int b)
{
    if (a < b) return 0;
    else return (linear((a-b), b) + 1);
}

int main()
{
    int a, b;
    std::cout << "Enter numbers:\n";
    std::cin >> a >> b;
    std::cout << "Answer: " << linear(a, b) << std::endl;
    return 0;
}

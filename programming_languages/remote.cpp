#include <iostream>

int remote(int a, int b)
{
    if (a == 0) return b + 1;
    else if (b == 0) return remote(a-1, 1);
    else return remote(a-1, remote(a, b-1));
}

int main()
{
    int a, b;
    std::cout << "Enter numbers:\n"; std::cin >> a >> b;
    std::cout << "Answer: " << remote(a, b) << std::endl;
    return 0;
}

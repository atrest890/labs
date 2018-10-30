#include <iostream>

int repeated(int a, int b, int c)
{
    if (a < b) return c;
    else
    {
        int r = repeated(a-b, b, c+1);
        c = 0;
        return r;
    }
}

int main()
{
    int a, b, c;
    std::cout << "Enter numbers:" << std::endl;
    std::cin >> a >> b >> c;
    std::cout << "Answer: " << repeated(a, b, c) << std::endl;
    return 0;
}

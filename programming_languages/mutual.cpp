#include <iostream>

double mutual1(int);
double mutual2(int a)
{
    if (a > 0)
    {
        double m2 = mutual1(a-1);
        return m2;
    }
    else return 1;
}

double mutual1(int a)
{
    if (a == 0) return 3;
    else
    {
        if (a % 2 == 0) return (mutual2(a-1)+1);
        else return (mutual1(a-1));
    }
}

int main()
{
    int a;
    std::cout << "Enter a number: "; std::cin >> a;
    std::cout << "Answer: " << mutual1(a) << std::endl;
    return 0;
}

#include <iostream>

const int x1 = 1, x2 = 1, x3 = 0,
          y1 = 1, y2 = 2, y3 = 1,
          z1 = 0, z2 = 1, z3 = 2,
          b1 = 2, b2 = 4, b3 = 3;

int main()
{
    int det = x1*y2*z3 + x2*y3*z1 + x3*y1*z2 - x3*y2*z1 - x2*y1*z3 - x1*y3*z2;
    int detx = b1*y2*z3 + b2*y3*z1 + b3*y1*z2 - b3*y2*z1 - b2*y1*z3 - b1*y3*z2;
    int dety = x1*b2*z3 + x2*b3*z1 + x3*b1*z2 - x3*b2*z1 - x2*b1*z3 - x1*b3*z2;
    int detz = x1*y2*b3 + x2*y3*b1 + x3*y1*b2 - x3*y2*b1 - x2*y1*b3 - x1*y3*b2;

    int x = detx / det;
    int y = dety / det;
    int z = detz / det;

    std::cout << "Roots: x = " << x << "\ty = " << y << "\tz = " << z << std::endl << std::endl;
    std::cout << "Checking:\n";
    std::cout << "x + y = " << x1*x + y1*y << std::endl;
    std::cout << "x + 2y + z = " << x2*x + y2*y + z2*z << std::endl;
    std::cout << "y + 2z = " << y3*y + z3*z << std::endl << std::endl;
    return 0;
}

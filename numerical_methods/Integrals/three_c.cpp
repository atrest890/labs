#include <iostream>
#include <math.h>
 
using namespace std;
 
int main() {
    double a,b,n,sum,step,integr,x,q,res;
    cout << "Введите границы интегрирования (нижняя-верхняя): ";
    cin >> a >> b;
    cout << "Введите количество разбиений: ";
    cin >> n;
    step = (b-a)/(3*n);
    sum=a*a*sin(a)+b*b*sin(b);
    q=3*n-1;
    for (int i = 0; i <=q; ++i) {
        x=a+step*i;
        if(i%3==0){
            sum+=2*x*x*sin(x);
        }
        else{
            sum+=3*x*x*sin(x);
        }
    }
    sum *=3*step/8;
    cout << "Результат: " << sum;
}

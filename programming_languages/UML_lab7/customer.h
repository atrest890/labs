#ifndef CUSTOMER_H
#define CUSTOMER_H
#include <string>
#include <bill.h>

static int id = 0;

class Customer
{
private:
    std::string fullName;
    int tableNumber;
    double wallet;
    std::string order;

public:
    Customer(int id, std::string fn)
    {
        id++;
        this->fullName = fn;
    };

    int getId()
    {
        return id;
    }

    void setTableNumber(int tn)
    {
        this->tableNumber = tn;
    }

    double pay(double billValue)
    {
        return wallet - billValue;
    }

    void setOrder(std::string o)
    {
        this->order = o;
    }

    std::string getOrder()
    {
        return this->order;
    }
};

#endif // CUSTOMER_H

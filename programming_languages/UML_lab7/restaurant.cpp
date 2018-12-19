#include "restaurant.h"

Restaurant::Restaurant(std::string a, std::string n)
{
    a = address;
    n = name;
}

void Restaurant::addNewCustomer(const Customer &cust)
{
    customerList.emplace_back(cust);
}


int Restaurant::findEmptyTable()
{
    for (int i = 0; i < 10; ++i) {
        if ()
    }
}

bool Restaurant::isTableBooked()
{
    return
}

std::string Restaurant::provideService(Order *o)
{

    return "You're order is accepted!";
}


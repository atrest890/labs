#ifndef RESTAURANT_H
#define RESTAURANT_H
#include <customer.h>
#include <enterprise.h>
#include <vector>
#include <table.h>
#include <list>


class Restaurant : public Enterprise
{
private:
     std::vector<Table> tables;
     std::list<Customer> customers;

public:
    Restaurant();

    Table bookTable()
    {
        for (auto t : tables) {
            if ( t.getStatus() ) {
                return t;
            }
        }
    }

    void addNewCustomer(Customer c)
    {
        customers.emplace_back(c);
    }

    std::string giveBill(Customer c)
    {
        return "Your bill is " + c.getOrder();
    }

    std::string provideService()
    {
        return "Welcome to our restaurant. What do you want?";
    }
};

#endif // RESTAURANT_H

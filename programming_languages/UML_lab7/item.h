#ifndef ITEM_H
#define ITEM_H
#include <string>

class Item
{
private:
    double price;
    std::string product;

public:
    Item();
    void setPrice(double p)
    {
        this->price = p;
    }

    double getPrice()
    {
        return price;
    }

    void setProduct(std::string p)
    {
        this->product = p;
    }
};

#endif // ITEM_H

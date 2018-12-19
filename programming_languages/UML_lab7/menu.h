#ifndef MENU_H
#define MENU_H
#include <iostream>
#include <ilist.h>
#include <vector>

class Menu : IList
{
private:
    class Item
    {
    private:
        double price;
        std::string product;
        std::string name;

    public:
        Item();
        void setName(std::string n)
        {
            this->name = n;
        }

        std::string getName()
        {
            return name;
        }

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

        std::string getProduct()
        {
            return this->product;
        }
    };

private:
    std::vector<Item> items;

public:
    Menu();

    void showList()
    {
        for (auto i : items) {
            std::cout << i.getName() << " "
                      << i.getProduct() << " "
                      << i.getPrice() << std::endl;
        }
    }
};

#endif // MENU_H

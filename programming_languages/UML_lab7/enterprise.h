#ifndef ROOM_H
#define ROOM_H
#include <string>

class Enterprise
{
protected:
    std::string address;
    std::string name;

public:
    Enterprise(std::string a, std::string n)
    {
        this->address = a;
        this->name = n;
    }

    std::string getAddress()
    {
        return this->address;
    }
    std:: string getName()
    {
        return this->name;
    }
    virtual std::string provideService() = 0;
    virtual ~Enterprise();
};

#endif // ROOM_H

#ifndef ILIST_H
#define ILIST_H
#include <list>
#include <item.h>

class IList
{
public:
    IList();
    virtual std::list<Item> getList() = 0;
    virtual ~IList();
};

#endif // ILIST_H

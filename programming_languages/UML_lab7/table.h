#ifndef TABLE_H
#define TABLE_H


class Table
{
private:
    int tableNumber;
    bool status;

public:
    Table();

    void setTableNumber(int n)
    {
        this->tableNumber = n;
    }

    int getTableNumber()
    {
        return tableNumber;
    }

    void setStatus(bool s)
    {
        this->status = s;
    }

    bool getStatus()
    {
        return this->status;
    }
};

#endif // TABLE_H

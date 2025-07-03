#ifndef _POINT_H_
#define _POINT_H_

class Point{
private :
    int x, y;
protected :

public : 
    Point();
    Point(int x, int y);
    ~Point();
    void printPoint();
    int getX();
    void setX(int x);
    int getY();
    void setY(int y);
};
void print();
#endif
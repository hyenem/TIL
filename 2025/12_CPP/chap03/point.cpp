#include <iostream>
#include "point.h"
using namespace std;

Point::Point(){}
Point::Point(int xx, int yy):x(xx), y(yy){}
Point::~Point(){}
void Point::printPoint(){
    cout << "x = " << x << ", y = " << y << endl;
}
int Point::getX(){
    return x;
}
void Point::setX(int xx){
    this->x = xx;
}
int Point::getY(){
    return y;
}
void Point::setY(int yy){
    this->y = yy;
}
void print(){
    
}
#include <iostream>
#include <math.h>

using namespace std;

class Motion{

    float x1, y1, x2, y2, dist;
    
    public: Motion(){
        cout << "Enter x1, y1, x2, and y2" << endl;
        cin >> x1 >> y1 >> x2 >> y2;
    }
    void distance(){
        dist = sqrt(pow((x2 - x1), 2) + ((y2 - y1), 2));                    //calculation of distance
        cout << "Distance = " << dist;
    }
};

int main(){
    Motion m;
    m.distance();

    return 0;
}
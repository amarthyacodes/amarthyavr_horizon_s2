#include <iostream>
#include <math.h>

using namespace std;

class Motion{

    float x1, y1, x2, y2, dist, initial_velcity, accn, max_speed;
    
    public: Motion(){
        cout << "Enter x1, y1, x2, and y2" << endl;
        cin >> x1 >> y1 >> x2 >> y2;
    }
    void distance(){
        dist = sqrt(pow((x2 - x1), 2) + ((y2 - y1), 2));                    //calculation of distance
        cout << "Distance = " << dist;
    }
    void time_taken(){
        cout << "Enter Initial Velocity, Acceleration, and Maximum speed" << endl;
        cin >> initial_velcity >> accn >> max_speed;
        float t1 = (max_speed - initial_velcity) / accn;     // time taken for rover to reach maximum speed
        float d1 = initial_velcity * t1 + 0.5 * accn * (pow(t1, 2));           // distance covered during time t1
        float d2 = dist - d1;                                // distance covered after reaching top speed
        float t2 = d2 / max_speed;                           // time taken after maximum speed
        cout << "Total time to reach destination = " << t1 + t2 << endl;
    }
};

int main(){
    Motion m;
    m.distance();
    m.time_taken();

    return 0;
}
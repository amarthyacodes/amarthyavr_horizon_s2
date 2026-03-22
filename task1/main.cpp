#include <iostream>
#include <math.h>

using namespace std;

class Motion{

    float x1, y1, x2, y2, dist, initial_velocity, accn, max_speed;
    
    public: Motion(){
        cout << "Enter x1, y1, x2, and y2" << endl;
        cin >> x1 >> y1 >> x2 >> y2;
    }
    void distance(){
        dist = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));                    // calculation of distance
        if(dist == 0){
        cout << "Rover is already at the destination." << endl;
        return;
        }
        cout << "Distance = " << dist << endl;
    }
    void time_taken(){
        cout << "Enter Initial Velocity, Acceleration, and Maximum speed" << endl;
        cin >> initial_velocity >> accn >> max_speed;
        
        if(accn == 0){
        cout << "Acceleration cannot be zero." << endl;
        return;
        }

        if(initial_velocity < 0 || max_speed < 0){
        cout << "Speed cannot be negative." << endl;
        return;
        }

        if(initial_velocity > max_speed){
        cout << "Initial velocity cannot exceed maximum speed." << endl;
        return;
        }

        float t1 = (max_speed - initial_velocity) / accn;                         // time taken for rover to reach maximum speed
        float d1 = initial_velocity * t1 + 0.5 * accn * (pow(t1, 2));            // distance covered during time t1
        float d2 = dist - d1;                                                    // remaining distance after acceleration
        float t2 = d2 / max_speed;                                              // time to travel remaining distance at maximum speed
        cout << "Total time to reach destination = " << t1 + t2 << endl;
    }
};



int main(){
    Motion m;
    m.distance();
    m.time_taken();

    return 0;
}
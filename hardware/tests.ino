#include <stdio.h>
#include <conio.h>

/* Input and Output

Inputs

1) Microphones -- Range (Voltage)
2) Ultrasound --  (Voltage)

Output

1) Gyro (int)
2) Motordriver (int )
3) Motors (voltage)

*/

#define M1 ;
#define M2 ;
#define M3 ;
#define M4 ;

// Ultrasound

#define USOUND_TRIGGER 6
#define USOUND_ECHO 5

// Motor Driver

#define MOTOR1 8
#define MOTOR2 9

// Gyroscope
#define Gyro ;

void setup()
{
}

char get_robo_direction()
{
}

char check_target_direction()
{
}

void turn_obst(char target_direction)
{
}

void turn(int target_dir)
{

    while (target_dir != get_robo_direction())
    {
        // keep changing the robot direction...
    }
}

void move_robo(char target_dir)
{

    char robo_dir;

    robo_dir = get_robo_direction();
    char check = check_obstacle();

    if (check != 'Y')
    {

        if (robo_dir == target_dir)
        {
            /*provide voltage to motor driver 1
                and motor driver 2*/
            int d;
            move(d);
        }
        else
        {
            turn(target_dir);
        }
    }
    else
    {
        turn_obst(target_dir);
    }
}

void move_straight(int d)
{

    Serial.println("Moving...");
    digitalWrite(MOTOR2, HIGH);
    digitalWrite(MOTOR1, LOW);
    delay(d);
    digitalWrite(MOTOR2, LOW);
    delay(d);
}

void loop()
{

    char target_direction;
    // char robo_dir;

    // robo_dir = get_robo_direction();
    target_direction = check_target_direction();
    move_robot(target_direction);
}
#include "Station.h"
#include <math.h>

Station :: Station(int d)
{
    delay = d;
    carrierStatus = (delay == 0);
    failcount = 0;
    clear = true;
}

bool Station::getCarrierStatus()
{
    return carrierStatus;
}

void Station::setDelay()
{
    if(failcount < 9)failcount++;
    delay = rand() % ((int)pow(2, failcount)) + 1;
    carrierStatus = false;
}

void Station::updateStatus()
{
    
    delay--;
    if(delay < 0)
    {
        if(clear)
        {
            carrierStatus = true;
        }
        else 
        {
            carrierStatus = false;
            delay = 1;
        }
    }
    else
    {
        carrierStatus = false;
    }
}

void Station::onSuccess()
{
    failcount = 0;
    delay = rand() % 4;
}

void Station::isClear(Station *s1, Station *s2)
{
    if(s1->carrierStatus || s2->carrierStatus)
    {
        clear = false;
    }
    else
    {
        clear = true;
    }
}
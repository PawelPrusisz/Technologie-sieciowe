
#include <bits/stdc++.h>
#include "Station.h"
#include <time.h>
#include <stdlib.h> 
#include <unistd.h> 

using namespace std;

Station *s1, *s2, *s3;

void colision()
{
    if(s1->getCarrierStatus())
    {
        s1->setDelay();
        cout<<"s1 delay "<<s1->delay<<" failCount "<<s1->failcount<<"\n";
    }
    if(s2->getCarrierStatus())
    {
        s2->setDelay();
        cout<<"s2 delay "<<s2->delay<<" failCount "<<s2->failcount<<"\n";
    }
    if(s3->getCarrierStatus())
    {
        s3->setDelay();
        cout<<"s3 delay "<<s3->delay<<" failCount "<<s3->failcount<<"\n";
    }
}

int randomInt()
{
    return rand() % 4;
}

int main()
{
    srand(time(0));

    float r1, r2, r3, r4, r5;

    bool carrierStatus;
    
    s1 = new Station(randomInt());

    s2 = new Station(randomInt());

    s3 = new Station(randomInt());

    for(int i=0; i<100; i++)
    {
        //cerr<<i<<"\n";
        //cout<<"\n-----------------------------------\n";
        s1->isClear(s2, s3);
        s2->isClear(s1, s3);
        s3->isClear(s1, s2);

        s1->updateStatus();
        s2->updateStatus();
        s3->updateStatus();

        if(s1->getCarrierStatus())
        {
            cout<<"Sending message form s1\n";

            if(s2->getCarrierStatus() || s3->getCarrierStatus())
            {
                colision();
                cout<<"Collision occur, Transmission stop\n";
            }
            else
            {
                cout<<"Data has been transmited successfully \n";
                s1->onSuccess();
            }
        }
    
        if(s2->getCarrierStatus())
        {
            cout<<"Sending message form s2\n";

            if(s3->getCarrierStatus() || s1->getCarrierStatus())
            {
                colision();
                cout<<"Collision occur, Transmission stop\n";
            }
            else
            {
                cout<<"Data has been transmited successfully \n";
                s2->onSuccess();
            }
        }

        if(s3->getCarrierStatus())
        {
            cout<<"Sending message form s3\n";

            if(s1->getCarrierStatus() || s2->getCarrierStatus())
            {
                colision();
                cout<<"Collision occur, Transmission stop\n";
            }
            else
            {
                cout<<"Data has been transmited successfully \n";
                s3->onSuccess();
            }
        }
    }

    return 0;
}
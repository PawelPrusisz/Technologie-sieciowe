#include "CRC.h"
#include <bits/stdc++.h>

using namespace std;
int packetsRead = 0;
string input;

bool frame(int index)
{
    if(input[index] != '0') return false;
    for(int j = index+1; j < index+7; j++)
        if(input[j] != '1') return false;
    
    if(input[index+7] != '0')return false;

    return true;
}


int main()
{
    cin>>input;

    int i = 0;

    string output = ""; 

    while(i < input.size())
    {
        output = "";
        bool start = true;
        while(!frame(i))
        {
            i++;
            if(i >= input.size())
            {
                start = false;
                break;
            }
        }
        if(!start)break;

        int ones = 0;
        output = "";
        for(i+=8; i < input.size(); i++)
        {
            if(frame(i))
            {
                break;
            }
            if (input[i] == '1') ones++;
            else ones = 0;

            if (ones == 5)
            {
                output += input[i];
                i++;
                ones = 0;
            }
            else
            {
                output += input[i];
            }
        }
        if(output.size() > 32)
        {
            string message = "";
            string crcString = "";
            message = output.substr(0, output.size()-32);
            crcString = output.substr(output.size()-32, output.size());

            //cerr<<message<<"\n"<<crcString<<"\n";
            cerr<<crcString<<"\n";
            
            uint32_t crc = CRC::Calculate(message.c_str(), sizeof(message), CRC::CRC_32());

            stringstream ss;
            ss << std::hex << crc;
            unsigned n;
            ss >> n;
            bitset<32> bset(n);

            if(crcString != bset.to_string())
            {
                cerr<<"error, corrupted data\n";
            }
            else
            {
                packetsRead++;
                cout<<message<<"\n";
            }
        }
        else{
            cerr<<"empty frame\n";
        }
        output = "";
        i++;
    }
    cerr<<"odczytano "<<packetsRead<<" pakietow\n";
    return 0;
}
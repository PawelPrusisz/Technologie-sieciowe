#include "CRC.h"

#include <iomanip>  // Includes ::std::hex
#include <iostream> // Includes ::std::cout
#include <cstdint>  // Includes ::std::uint32_t
#include <bitset>
#include <vector> 

using namespace std;

string input;

string output = "";

void frame()
{
    output += "01111110";
}

int main()
{
    cin>>input;
    // ToDo: 01111110 -> 011111 0 10
    // ToDo: CRC?

    uint32_t crc = CRC::Calculate(input.c_str(), sizeof(input), CRC::CRC_32());

    stringstream ss;
	ss << std::hex << crc;
	unsigned n;
	ss >> n;
	bitset<32> bset(n);

    string crcString = bset.to_string();

    cerr<<crcString<<"\n";
    input += crcString;

    frame();

    int ones = 0;  
    for(int i = 0; i < input.size(); i++)
    {
        if(input[i] == '1') ones++;
        else ones = 0;

        if(ones == 5)
        {
            output += input[i];
            output += "0";
            ones = 0;
        }
        else
        {
            output += input[i];
        }
    }

    

    frame();

    cout<<output<<"\n";

    return 0;
}
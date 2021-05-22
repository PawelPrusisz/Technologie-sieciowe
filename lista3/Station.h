using namespace std;

class Station
{
    private:
    bool carrierStatus;
    
    public:
    Station(int d);
    int delay;
    int failcount;
    bool clear;
    void isClear(Station *s1, Station *s2);
    bool getCarrierStatus();
    void setDelay();
    void updateStatus();
    void onSuccess();
};

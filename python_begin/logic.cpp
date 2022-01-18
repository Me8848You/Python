// #include<stdio.h>
// #include<math.h>
#include<iostream>
// #include<conio.h>

using namespace std;


void Matrix()
{
    char a1[5]={'a','b','c','d','e'};
    char a2[5]={'f','g','h','i','j'};
    char a3[5]={'k','l','m','n','o'};
    char a4[5]={'p','q','r','s','t'};
    char a4[5]={'u','v','w','x','y'};
    char a5[5]={'z'};

    char b1[6]={'a','f','k','p','u','z'};
    char b2[5]={'b','g','l','q','v'};
    char b3[5]={'c','h','m','r','w'};
    char b4[5]={'d','i','n','s','x'};
    char b5[5]={'e','j','o','t','y'};

    cout<<"1:"<<a1[0]<<a1[1]<<a1[3]<<a1[4]<<a1[5]<<endl;
    cout<<"2:"<<a2[0]<<a2[1]<<a2[3]<<a2[4]<<a2[5]<<endl;
    cout<<"3:"<<a3[0]<<a3[1]<<a3[3]<<a3[4]<<a3[5]<<endl;
    cout<<"4:"<<a4[0]<<a4[1]<<a4[3]<<a4[4]<<a4[5]<<endl;
    cout<<"5:"<<a5[0]<<a5[1]<<a5[3]<<a5[4]<<a5[5]<<endl;
    cout<<"6:"a6[0]<<endl;

    cout<<"****Enter the location of the letters of your crush****"<<endl;
    // cout<<"Be aware the input format must be seperated by a single space"<<endl;

    int column;

    cin>>column;

    for (int i = 1; i < 7; i++)
        {
            if (column==i)
            {
                cout<<bi[0]<<bi[1]<<bi[2]<<bi[3]<<bi[4]<<bi[5]<<endl;
            }
            else
            {}
            
        } 

    int column2;
    cin>>column2;

    for (int i = 0; i < 5; i++)
    {
        if (column2==i)
        {
            char N[5]=b[i];
        }
        
    }
    for (int i = 0; i < 5; i++)
    {
        cout<<N[i]<<endl;
    }
    
     
}

int main()
{
    cout<<"****WELCOME CHUPARUSTAM ****"<<endl;
    cout<<"Be careful from today your secret won't be that secret"endl;
    Matrix();
    return 0;
}
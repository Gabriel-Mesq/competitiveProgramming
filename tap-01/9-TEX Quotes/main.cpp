#include <bits/stdc++.h>

using namespace std;

int main(){

    char c;
    int counter = 0;

    while(scanf("%c", &c) != EOF){
        if(c == '\"'){
            if(counter & 1){
                cout << "\'\'";
            }else{
                cout << "``";
            }
            counter++;
        }else{
            cout << c;
        }
    }

    return 0;
}

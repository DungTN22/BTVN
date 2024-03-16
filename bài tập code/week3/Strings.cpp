#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    getline(cin,a);
    getline(cin,b);
    cout << a.size() << " "<< b.size() <<endl;
    cout << a +b << endl;
    char c=a[0],d=b[0];
    a[0]=d; b[0]=c;
    cout << a << " " << b;
    return 0;
}

#include <iostream>
#include <string>
using namespace std;
int main(){
    int a=12345;
    string k=to_string(a);
    for (int i=0;i<k.length();i++){
        cout << 100/(k[i]-48)<<" ";
    }
}

// hoán vị
#include <iostream>
using namespace std;
void dequy(int *arr1,int k,int n){
    if (k>=n){
        for (int i=0;i<n;i++) cout << arr1[i] <<" ";
        cout << endl;
    }
    else{
        for (int i=1;i<=n;i++){
            bool mode=true;
            for(int j=0;j<k;j++){
                if (i==arr1[j]){
                    mode=false; 
                    break;
                }
            }
            if(mode==true) {
                arr1[k]=i;
                dequy(arr1,k+1,n);
            }
        }
    }
}
int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=1;i<=n;i++){
        arr[0]=i;
        dequy(arr,1,n);
    }
}

/*
#include <iostream>
using  namespace std;
 
int n, kq[11], dd[10];
 
void xuat()
{
    for (int j=1; j<=n; j++)
        cout<< kq[j]<<" ";
    cout << endl;
}
 
void backtrack(int i)
{
    if (i>n) xuat();
    for (int j=1; j<=n; j++)
        if (dd[j]==0)
        {
            dd[j]=1;
            kq[i]=j;
            backtrack(i+1);
            dd[j]=0;
        }
}
 
int main()
{
    cin >> n;
    for (int i=1; i<=9; i++)
        dd[i]=0;
    backtrack(1);
}*/


#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    string a="D",b="d";
    if (a==b) cout << "yes";
    else cout << "no";
    char c='a';
    cout << a+c;
    
}
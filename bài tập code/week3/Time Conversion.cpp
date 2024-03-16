#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    string moi = s.substr(0,8);
    string time = s.substr(0,2); 
    int times = stoll(time);
    string a;
    if (s[8] == 'P'){
        if (times <12) times+=12;
        a= to_string(times);
        moi.replace(0,2,a);
    }
    else if (s[8] == 'A'){
        if (times >=12) times-=12;
        a= to_string(times);
        if (times<10) a="0"+a;
        moi.replace(0,2,a);
    }
    return moi;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

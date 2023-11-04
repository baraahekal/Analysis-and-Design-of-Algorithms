// Enjoying the journey
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

#define el '\n'
#define all(vec) vec.begin(), vec.end()

vector<string> gen_bit_strings(int n) {
    vector<string> bitStrings;
    
    // iterating over 2^n using left shifting
    for (int i = 0; i < (1 << n); i++) {
        string bitString;
        int temp = i;
        for (int j = 0; j < n; j++) bitString += to_string(temp % 2), temp /= 2;
        bitStrings.push_back(bitString);
    }
    return bitStrings;
}

int main() {
    for (const string& bitString : gen_bit_strings(3))
        cout << bitString << el;
}



// Enjoying the journey
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

#define el '\n'
#define all(vec) vec.begin(), vec.end()

const int oo = 0x3f3f3f3f;

void firstCommit() {
    cin.tie(nullptr);
    istream::sync_with_stdio(false);
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);

}

ll fast_pow(ll base, ll exponent, ll mod) {
    if (!exponent) return 1;
    ll sq = fast_pow(base, exponent / 2, mod);
    sq *= sq;

    return (exponent & 1) ? (sq * base % mod) : (sq % mod);
}

int main() {
    firstCommit();

    ll base, exponent, mod;
    while (cin >> base >> exponent >> mod)
        cout << fast_pow(base, exponent, mod) << el;
}


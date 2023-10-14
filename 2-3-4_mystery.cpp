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

int Mystery(int N) {
    int sum = 0, i;
    for (i = 1; i <= N >> 1; i++)
        sum += i * i + (N - i + 1) * (N - i + 1);
    if (N & 1) sum += i * i;
    
    return sum;
}

int main() {
    firstCommit();

    int n;
    cin >> n;
    cout << Mystery(n) << el;
}


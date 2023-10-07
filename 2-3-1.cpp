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

void solve() {
    // A)
    int N = 999;
    int sum = 0;
    for (int i = 1; i <= N; i -=- 2) sum += i; // Time Complexity O(N)

    // B)
    N = 1024;
    sum = 0;
    for (int i = 2; i <= N; i *= 2) sum += i; // Time Complexity O(log(N))

    // C)
    sum = 0;
    for (int i = 3; i <= N + 1; i++) sum += 1; // Time Complexity O(N)

    // D)
    sum = 0;
    for (int i = 3; i <= N + 1; i++) sum += i; // Time Complexity O(N)

    // E)
    sum = 0;
    for (int i = 0; i <= N - 1; i++) sum += i * (i + 1); // Time Complexity O(N)

    // F)
    sum = 0;
    for (int i = 1; i <= N; i++) sum += pow(3, i + 1); // Time Complexity O(N(log(N)))

    // G)
    sum = 0;
    for (int i = 1; i <= N; i++) for (int j = 1; j <= N; j++) sum += i * j; // Time Complexity O(N^2)

    // H)
    sum = 0;
    for (int i = 1; i <= N; i++) sum += 1 / i * (i + 1); // Time Complexity O(N)
}

int main() {
    firstCommit();

    int testCases = 1;
//    cin >> testCases;
    while (testCases--) solve();
}


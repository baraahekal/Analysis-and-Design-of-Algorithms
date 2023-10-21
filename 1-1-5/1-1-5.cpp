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
    vector<int> list1 {2, 5, 5, 5};
    vector<int> list2 {2, 2, 3, 5, 5, 7};
    vector<int> intersection;

    for (auto it1 = list1.begin(); it1 != list1.end(); it1++)
        for (auto it2 = list2.begin(); it2 != list2.end(); it2++)
            if (*it1 == *it2) list2.erase(it2), intersection.push_back(*it1);

    for (int &i : intersection)
        cout << i << " ";
    cout << el;
}

int main() {
    firstCommit();

    int testCases = 1;
//    cin >> testCases;
    while (testCases--) solve();
}

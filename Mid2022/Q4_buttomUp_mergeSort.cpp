// Enjoying the journey
#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& arr, int l, int mid, int h) {
    int n1 = mid - l + 1;
    int n2 = h - mid;

    // Generating two new lists for left and right halves of arr
    vector<int> left_half(arr.begin() + l, arr.begin() + l + n1);
    vector<int> right_half(arr.begin() + mid + 1, arr.begin() + mid + 1 + n2);

    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2)
        if (left_half[i] <= right_half[j])
            arr[k++] = left_half[i++];
        else
            arr[k++] = right_half[j++];

    while (i < n1) arr[k++] = left_half[i++];
    while (j < n2) arr[k++] = right_half[j++];

}

void mergeSort(vector<int>& arr) {
    int n = arr.size();

    for (int p = 1; p <= n; p *= 2) {
        for (int l = 0; l < n - 1; l += 2 * p) {
            int mid = l + p - 1;
            int h = min(l + 2 * p - 1, n - 1);
            merge(arr, l, mid, h);
        }
    }
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    mergeSort(arr);

    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }

    return 0;
}


class Solution {
 public:
  int twoEggDrop(int n) {
    return superEggDrop(2, n);
  }

 private:
  vector<vector<int>> dp;

  int superEggDrop(int K, int N) {
    // dp[k][n] := min # of moves to know F with k eggs and n floors
    dp.resize(K + 1, vector<int>(N + 1, -1));
    return drop(K, N);
  }

  int drop(int k, int n) {
    if (k == 0)  // No eggs -> done
      return 0;
    if (k == 1)  // One egg -> drop from 1-th floor to n-th floor
      return n;
    if (n == 0)  // No floor -> done
      return 0;
    if (n == 1)  // One floor -> drop from that floor
      return 1;
    if (dp[k][n] != -1)
      return dp[k][n];

    //   broken[i] := drop(k - 1, i - 1) is increasing w/ i
    // unbroken[i] := drop(k,     n - i) is decreasing w/ i
    // dp[k][n] := 1 + min(max(broken[i], unbroken[i])), 1 <= i <= n
    // Find the first index i s.t broken[i] >= unbroken[i],
    // Which minimizes max(broken[i], unbroken[i])

    int l = 1;
    int r = n + 1;

    while (l < r) {
      const int m = (l + r) / 2;
      const int broken = drop(k - 1, m - 1);
      const int unbroken = drop(k, n - m);
      if (broken >= unbroken)
        r = m;
      else
        l = m + 1;
    }

    return dp[k][n] = 1 + drop(k - 1, l - 1);
  }
};

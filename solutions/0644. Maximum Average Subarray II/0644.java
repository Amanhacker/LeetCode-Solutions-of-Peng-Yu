class Solution {
  public double findMaxAverage(int[] nums, int k) {
    final double kErr = 1e-5;
    double l = (double) Arrays.stream(nums).min().getAsInt();
    double r = (double) Arrays.stream(nums).max().getAsInt();

    while (r - l > kErr) {
      final double m = (l + r) / 2;
      if (check(nums, k, m))
        l = m;
      else
        r = m;
    }

    return l;
  }

  // True if there's a subarray with length >= k and average sum >= m
  private boolean check(int[] nums, int k, double m) {
    double sum = 0;
    double prevSum = 0;
    double minPrevSum = 0;

    for (int i = 0; i < nums.length; ++i) {
      // Trick: -m for each num so that we can check if the sum of the
      // Subarray >= 0
      sum += nums[i] - m;
      if (i >= k) {
        prevSum += nums[i - k] - m;
        minPrevSum = Math.min(minPrevSum, prevSum);
      }
      // If sum - minPrevSum >= 0,
      // We know there's a subarray with length >= k and average sum >= m
      if (i + 1 >= k && sum >= minPrevSum)
        return true;
    }

    return false;
  }
}

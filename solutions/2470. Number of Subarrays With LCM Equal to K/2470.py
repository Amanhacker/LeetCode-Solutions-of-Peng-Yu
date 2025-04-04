class Solution:
  def subarrayLCM(self, nums: List[int], k: int) -> int:
    ans = 0

    for i, runningLcm in enumerate(nums):
      for j in range(i, len(nums)):
        runningLcm = lcm(runningLcm, nums[j])
        if runningLcm > k:
          break
        if runningLcm == k:
          ans += 1

    return ans

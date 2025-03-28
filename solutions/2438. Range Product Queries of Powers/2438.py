class Solution:
  def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    kMod = 1_000_000_007
    kMaxDigit = 30
    ans = []
    powers = [1 << i for i in range(kMaxDigit) if n >> i & 1]

    for left, right in queries:
      prod = 1
      for i in range(left, right + 1):
        prod *= powers[i]
        prod %= kMod
      ans.append(prod)

    return ans

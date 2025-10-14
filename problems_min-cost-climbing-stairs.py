# problems/min-cost-climbing-stairs

"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

---
示例 1

输入 cost = [10,15,20]
输出 15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

---
示例 2

输入 cost = [1,100,1,1,1,100,1,1,100,1]
输出 6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。


### 解题

和最原始的爬楼梯思路其实差不多，只不过 f(i) 代表的并不是从 **起点** 到 i 格楼梯的方案总数，而应该是从 **起点** 到 i 格楼梯的 **最小花费**。
所以最后到达楼顶 (n) 的最小花费 f(n) 为 min(f(n - 1) + cost(n - 1), f(n - 2) + cost(n - 2))

边界是 len(cost) == 1 or len(cost) == 2
这时候不需要花费，不过题目规定了 2 <= cost.length <= 1000

f(2) = min(f(1) + cost[1], f(0) + cost[0])

#### 错误分析 1

我好像搞错了一个，就是它并不是到了最后一个格子就行，它要从最后一个格子 len(cost) 再往上一步

其实求的是 f(n + 1) <- min(f(n) + cost(n), f(n - 1) + cost(n - 1))

#### 错误分析 2

好像还是搞错计算边界了。因为 cost 的下标没有 cost[n]

#### 错误分析 3

整个计算逻辑已经对了应该，但是 badcase (cost = [1,100] -> 1)
就不用写这个
```python
if len(cost) == 1 or len(cost) == 2:
    return 0
```
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) == 1 or len(cost) == 2:
        #     return 0

        i_fi_dict = {
            0: 0,
            1: 0,
        }
        for i in range(2, len(cost)):
            fi = min(i_fi_dict[i - 1] + cost[i - 1], i_fi_dict[i - 2] + cost[i - 2])
            i_fi_dict[i] = fi

        return min(i_fi_dict[len(cost) - 1] + cost[-1], i_fi_dict[len(cost) - 2] + cost[-2])


if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(len(cost))
    print(Solution().minCostClimbingStairs(cost))

# problems/n-th-tribonacci-number

"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n 请返回第 n 个泰波那契数 Tn 的值。

---
示例 1

输入 n = 4
输出 4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

---
示例 2

输入 n = 25
输出 1389537
 
提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。


### 解题

其实还是和斐波那契数列、爬楼梯一样，就不停地往前计算，最后得到 Tn
T(n) = T(n - 1) + T(n - 2) + T(n - 3)

昨天做题的时候，把所有中间结果存在了一个 map 里，其实可以只保留 2 个（斐波那契）或者 3 个（这道题）就够了，这样空间复杂就是 O(1) 而不是 O(n)
但这里还是保留了 map 的做法，复制过来比较简单，偷懒了
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        i_fi_dict = {
            0: 0,
            1: 1,
            2: 1,
        }
        for i in range(3, n + 1):
            fi = i_fi_dict[i - 1] + i_fi_dict[i - 2] + i_fi_dict[i - 3]
            i_fi_dict[i] = fi

        return i_fi_dict[n]

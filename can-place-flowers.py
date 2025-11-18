# https://leetcode.cn/problems/can-place-flowers
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        if len(flowerbed) == 1:
            # 特殊情况，直接判断
            if (flowerbed[0] == 0 and n == 1) or (n == 0):
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                # 坑位被占了
                continue

            if i == 0:
                # 最左边，所以只考虑右边是不是 0
                if flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                # 最右边，所以只考虑左边是不是 0
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                # 中间位置，考虑两边是不是 0
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            if n == 0:
                break

        return n == 0
        

if __name__ == "__main__":
    sol = Solution()

    f = [0,0,0,0,0,1,0,0]
    n = 0
    print(sol.canPlaceFlowers(f, n))

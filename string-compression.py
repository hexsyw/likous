# https://leetcode.cn/problems/string-compression

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        curr_c_cnt = 0
        for i in range(len(chars)):
            curr_c = chars[i]
            curr_c_cnt += 1

            if i + 1 == len(chars):
                # 最后一个
                s += curr_c
                if curr_c_cnt > 1:
                    s += str(curr_c_cnt)
            else:
                next_c = chars[i + 1]
                if curr_c != next_c:
                    # 连续重复字符终止
                    s += curr_c
                    if curr_c_cnt > 1:
                        s += str(curr_c_cnt)
                    curr_c_cnt = 0

        # 重写 chars
        for i in range(len(chars)):
            if i + 1 <= len(s):
                chars[i] = s[i]
            else:
                chars.pop(-1)

        return len(chars)


if __name__ == "__main__":
    sol = Solution()
    sol.compress(["a", "a", "b", "b", "c", "c", "c"])

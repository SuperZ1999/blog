---
title: "LeetCode 1109"
date: 2022-09-25T23:57:09+08:00
tags: ["leetcode"]
draft: false
---

### 思路

标准差分数组，详见LeetCode-note

### 我的代码

```java
class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] nums = new int[n];
        Difference df = new Difference(nums);
        for (int[] booking : bookings) {
            df.increment(booking[0] - 1, booking[1] - 1, booking[2]);
        }
        return df.result();
    }

    static class Difference {
        private int[] diff;

        public Difference(int[] nums) {
            assert nums.length > 0;
            diff = new int[nums.length];

            diff[0] = nums[0];
            for (int i = 1; i < nums.length; i++) {
                diff[i] = nums[1] - nums[0];
            }
        }

        public void increment(int i, int j, int val) {
            diff[i] += val;
            // 注意这里j有可能是最后一个元素，此时的意思就是i后面的元素全部加val，所以不需要减val了
            if (j + 1 < diff.length) {
                diff[j + 1] -= val;
            }
        }

        public int[] result() {
            int[] res = new int[diff.length];
            res[0] = diff[0];

            for (int i = 1; i < diff.length; i++) {
                res[i] = res[i - 1] + diff[i];
            }
            return res;
        }
    }
}
```

### References

---

#### 1. [航班预订统计](https://leetcode.cn/problems/corporate-flight-bookings/)

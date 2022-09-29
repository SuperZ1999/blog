---
title: "LeetCode 1094"
date: 2022-09-26T00:32:18+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用差分数组的思想即可，这里把路程中各个地方的乘客数目当作数组的元素，每个trip相当于对这个数组的某一段进行加运算

### 我的代码

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int len = 0;
        for (int[] trip : trips) {
            len = len > trip[2] ? len : trip[2];
        }

        int[] nums = new int[len];
        Difference df = new Difference(nums);

        for (int[] trip : trips) {
            df.increment(trip[1], trip[2] - 1, trip[0]);
        }
        for (int num : df.result()) {
            if (num > capacity) {
                return false;
            }
        }
        return true;
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

#### 1. [拼车](https://leetcode.cn/problems/car-pooling/)

---
title: "LeetCode 698"
date: 2022-12-17T18:48:50+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

利用回溯算法，这种排列组合问题的各种变体都可以抽象成「球盒模型」，将子集看成盒子，那么每个盒子遍历一遍数组，要么将元素放盒子里面要么不放，就这样回溯，只不过代码有点难写

### 代码

```java
class Solution {
    private Map<Integer, Boolean> memo = new HashMap<>();

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int n = nums.length, sum = 0;
        if (k > n) {
            return false;
        }
        for (int num : nums) {
            sum += num;
        }
        if (sum % k != 0) {
            return false;
        }
        int used = 0;
        return backtrack(nums, used, 0, 0, sum / k, k);
    }

    private boolean backtrack(int[] nums, int used, int bucket,
                              int start ,int target, int k) {
        if (k == 0) {
            return true;
        }
        if (bucket == target) {
            boolean res = backtrack(nums, used, 0, 0, target, k - 1);
            memo.put(used, res);
            return res;
        }
        if (memo.containsKey(used)) {
            return memo.get(used);
        }

        for (int i = start; i < nums.length; i++) {
            if (((used >> i) & 1) == 1) {
                continue;
            }
            if (bucket + nums[i] > target) {
                continue;
            }
            bucket += nums[i];
            used |= 1 << i;
            if (backtrack(nums, used, bucket, i + 1, target, k)) {
                return true;
            }
            bucket -= nums[i];
            used ^= 1 << i;
        }
        return false;
    }
}
```

### References

---

#### 1. [划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)

---
title: "LeetCode 39"
date: 2022-12-17T20:29:05+08:00
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

经典可复选组合问题，保证递归的时候还能选择已经选择的元素即可

### 代码

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> track = new LinkedList<>();
    int trackSum = 0;

    private void backtrack(int[] nums, int start, int target) {
        if (trackSum == target) {
            res.add(new LinkedList<>(track));
            return;
        }
        if (trackSum > target) {
            return;
        }

        for (int i = start; i < nums.length; i++) {
            track.add(nums[i]);
            trackSum += nums[i];
            backtrack(nums, i, target);
            track.remove(track.size() - 1);
            trackSum -= nums[i];
        }
    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtrack(candidates, 0, target);
        return res;
    }
}
```

### References

---

#### 1. [组合总和](https://leetcode.cn/problems/combination-sum/)

---
title: "LeetCode 40"
date: 2022-12-17T19:52:20+08:00
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

经典带重复元素的组合问题，详见思想篇章

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
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            track.add(nums[i]);
            trackSum += nums[i];
            backtrack(nums, i + 1, target);
            track.remove(track.size() - 1);
            trackSum -= nums[i];
        }
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtrack(candidates, 0, target);
        return res;
    }
}
```

### References

---

#### 1. [组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)

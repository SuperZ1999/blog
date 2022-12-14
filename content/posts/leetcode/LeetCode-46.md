---
title: "LeetCode 46"
date: 2022-12-14T22:41:32+08:00
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

经典回溯问题，直接套模板即可，决策树如下：

![img](https://labuladong.gitee.io/algo/images/backtracking/3.jpg)

### 代码

```java
class Solution {
    private List<List<Integer>> res = new LinkedList<>();

    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        boolean[] used = new boolean[n];
        List<Integer> track = new LinkedList<>();
        backtrack(track, nums, used);
        return res;
    }

    private void backtrack(List<Integer> track, int[] nums, boolean[] used) {
        if (track.size() == nums.length) {
            res.add(new LinkedList<>(track));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            track.add(nums[i]);
            used[i] = true;
            backtrack(track, nums, used);
            used[i] = false;
            track.remove(track.size() - 1);
        }
    }
}
```

### References

---

#### 1. [全排列](https://leetcode.cn/problems/permutations/)

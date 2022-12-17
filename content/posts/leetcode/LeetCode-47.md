---
title: "LeetCode 47"
date: 2022-12-17T20:00:53+08:00
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

经典有重复元素的全排列问题，需要注意怎么去重，可以固定相同元素在全排列里的相对位置来去重，代码如下：

```java
if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
    continue;
}
```

### 代码

```java
class Solution {
    private List<List<Integer>> res = new LinkedList<>();

    private void backtrack(List<Integer> track, int[] nums, boolean[] used) {
        if (track.size() == nums.length) {
            res.add(new LinkedList<>(track));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }
            track.add(nums[i]);
            used[i] = true;
            backtrack(track, nums, used);
            used[i] = false;
            track.remove(track.size() - 1);
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        boolean[] used = new boolean[n];
        List<Integer> track = new LinkedList<>();
        backtrack(track, nums, used);
        return res;
    }
}
```

### References

---

#### 1. [全排列 II](https://leetcode.cn/problems/permutations-ii/)

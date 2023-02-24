---
title: "LeetCode 78"
date: 2022-12-17T19:15:12+08:00
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

两种思路：

#### 回溯

经典子集问题，不解释了，详见思想篇章

#### 迭代

因为每一个元素要么选要么不选，所以可以看成有n个盒子n个数，每个数要么放进盒子，要么不放，可以把放进盒子看成1，不放盒子看成0，那么所有的2^n个情况就是[0, 2^n - 1]。

### 代码

#### 回溯

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> track = new LinkedList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0);
        return res;
    }

    private void backtrack(int[] nums, int start) {
        res.add(new LinkedList<>(track));

        for (int i = start; i < nums.length; i++) {
            track.add(nums[i]);
            backtrack(nums, i + 1);
            track.remove(track.size() - 1);
        }
    }
}
```

#### 迭代

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> track = new ArrayList<>();
        List<List<Integer>> res = new LinkedList<>();
        int n = nums.length;
        for (int mask = 0; mask < (1 << n); mask++) {
            track.clear();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    track.add(nums[i]);
                }
            }
            res.add(new ArrayList<>(track));
        }
        return res;
    }
}
```

### References

---

#### 1. [子集](https://leetcode.cn/problems/subsets/)

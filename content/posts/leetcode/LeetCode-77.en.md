---
title: "LeetCode 77"
date: 2022-12-17T19:28:21+08:00
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

经典组合问题，不解释了，详见思想篇章

### 代码

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> track = new LinkedList<>();

    public List<List<Integer>> combine(int n, int k) {
        backtrack(n, 1, k);
        return res;
    }

    private void backtrack(int n, int start, int k) {
        if (track.size() == k) {
            res.add(new LinkedList<>(track));
            return;
        }

        for (int i = start; i <= n; i++) {
            track.add(i);
            backtrack(n, i + 1, k);
            track.remove(track.size() - 1);
        }
    }
}
```

### References

---

#### 1. [组合](https://leetcode.cn/problems/combinations/)

---
title: "LeetCode 56"
date: 2022-12-23T10:17:05+08:00
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

先按起点排序，然后寻找可以合并的最大终点即可

### 代码

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> {
            return a[0] - b[0];
        });
        List<int[]> res = new LinkedList<>();
        res.add(intervals[0]);
        for (int i = 1; i < n; i++) {
            int[] last = res.get(res.size() - 1);
            if (intervals[i][0] <= last[1]) {
                last[1] = Math.max(intervals[i][1], last[1]);
            } else {
                res.add(intervals[i]);
            }
        }
        int[][] ans = new int[res.size()][];
        return res.toArray(ans);
    }
}
```

### References

---

#### 1. [合并区间](https://leetcode.cn/problems/merge-intervals/)

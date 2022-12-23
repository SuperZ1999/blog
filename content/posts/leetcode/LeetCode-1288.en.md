---
title: "LeetCode 1288"
date: 2022-12-23T09:45:26+08:00
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

先按起点排序，然后遍历，如果终点小于之前最大的终点，那这个区间就可以被覆盖

### 代码

```java
class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        int res = n, right = intervals[0][1];
        for (int i = 1; i < n; i++) {
            if (intervals[i][1] <= right) {
                res--;
            } else {
                right = intervals[i][1];
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/)

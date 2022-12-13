---
title: "LeetCode 435"
date: 2022-12-13T22:03:10+08:00
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

利用贪心算法，每次选择结束最早的区间（这就是局部最优选择），然后统计就可以了

### 代码

```java
class Solution {
    private int intervalSchedule(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            return a[1] - b[1];
        });
        int count = 1, x_end = intervals[0][1];
        for (int[] interval : intervals) {
            if (interval[0] >= x_end) {
                count++;
                x_end = interval[1];
            }
        }
        return count;
    }

    public int eraseOverlapIntervals(int[][] intervals) {
        return intervals.length - intervalSchedule(intervals);
    }
}
```

### References

---

#### 1. [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

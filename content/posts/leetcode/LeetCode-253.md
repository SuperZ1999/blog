---
title: "LeetCode 253"
date: 2022-12-14T21:49:15+08:00
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

其实就是求同一时刻最多有多少重叠区间，其实投影到x轴然后看看有几个区间重合到一起了就可以，有两种代码思路：

#### 用数组表示x轴+差分数组优化

举例来说，如果输入 `meetings = [[0,30],[5,10],[15,20]]`，那么我们就给数组中 `[0,30],[5,10],[15,20]` 这几个索引区间分别加一，最后遍历数组，求个最大值就行了。

#### 扫描法

只记录start和end时间，然后扫描这些时间点，碰到start，count++，碰到end，count--，记录count的最大值即可

### 代码

```java
class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int n = intervals.size();
        int[] start = new int[n];
        int[] end = new int[n];
        for (int i = 0; i < n; i++) {
            start[i] = intervals.get(i).start;
            end[i] = intervals.get(i).end;
        }
        Arrays.sort(start);
        Arrays.sort(end);
        int i = 0, j = 0, res = 0, count = 0;
        while (i < n) {
            if (start[i] < end[j]) {
                count++;
                i++;
            } else {
                count--;
                j++;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}
```

### References

---

#### 1. [会议室 II](https://leetcode.cn/problems/meeting-rooms-ii/)

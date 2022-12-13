---
title: "LeetCode 452"
date: 2022-12-13T22:30:48+08:00
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

其实就是求解无重叠区间最多有几个，同[LeetCode-435](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-435/)，因为可以每一发都打在无重叠区间中每个区间的最右边，这样下一个区间之前的区间都被贯穿，如下图所示：

![img](https://labuladong.gitee.io/algo/images/interval/3.jpg)

只不过这道题相邻的两个区间边界触碰也算是重叠区间，`interval[0] >= x_end`改成`interval[0] > x_end`就可以了

### 代码

```java
class Solution {
    private int intervalSchedule(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[1] > b[1]) {
                return 1;
            } else if (a[1] < b[1]) {
                return -1;
            } else {
                return 0;
            }
        });
        int count = 1, x_end = intervals[0][1];
        for (int[] interval : intervals) {
            if (interval[0] > x_end) {
                count++;
                x_end = interval[1];
            }
        }
        return count;
    }

    public int findMinArrowShots(int[][] points) {
        return intervalSchedule(points);
    }
}
```

### References

---

#### 1. [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

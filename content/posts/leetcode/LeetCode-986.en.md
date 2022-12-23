---
title: "LeetCode 986"
date: 2022-12-23T11:29:12+08:00
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

利用双指针遍历两个区间集合，谁的终点小，谁往前走，同时判断两个指针指向的区间是否有交集，详见代码

### 代码

```java
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int m = firstList.length, n = secondList.length;
        int i = 0, j = 0;
        List<int[]> res = new LinkedList<>();
        while (i < m && j < n) {
            if (firstList[i][1] >= secondList[j][0] && firstList[i][0] <= secondList[j][1]) {
                res.add(new int[]{Math.max(firstList[i][0], secondList[j][0]), Math.min(firstList[i][1], secondList[j][1])});
            }
            if (firstList[i][1] > secondList[j][1]) {
                j++;
            } else {
                i++;
            }
        }
        int[][] ans = new int[res.size()][];
        return res.toArray(ans);
    }
}
```

### References

---

#### 1. [区间列表的交集](https://leetcode.cn/problems/interval-list-intersections/)

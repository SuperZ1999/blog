---
title: "LeetCode 1024"
date: 2022-12-13T23:32:03+08:00
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

利用贪心算法，思路很简单，先按start排序，遍历区间，找end最大的区间，然后再遍历区间找start小于前一个end，end最大的区间，就是代码有点难写，算法过程见下图：

![img](https://labuladong.gitee.io/algo/images/%e5%89%aa%e8%a7%86%e9%a2%91/4.jpeg)

### 代码

```java
class Solution {
    public int videoStitching(int[][] clips, int time) {
        Arrays.sort(clips, (a, b) -> {
            return a[0] == b[0] ? b[1] - a[1] : a[0] - b[0];
        });
        int n = clips.length, i = 0, curEnd = 0, nextEnd = 0, res = 0;
        while (i < n && clips[i][0] <= curEnd) {
            while (i < n && clips[i][0] <= curEnd) {
                nextEnd = Math.max(nextEnd, clips[i][1]);
                i++;
            }
            res++;
            curEnd = nextEnd;
            if (curEnd >= time) {
                return res;
            }
        }
        return -1;
    }
}
```

### References

---

#### 1. [视频拼接](https://leetcode.cn/problems/video-stitching/)

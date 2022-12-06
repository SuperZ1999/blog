---
title: "LeetCode 295"
date: 2022-12-06T20:15:23+08:00
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

用两个优先队列（最大/小堆），等量的将数据流分成两部分，最大堆放小的那一部分，最小堆放大的那一部分，中位数就是堆顶的元素平均数，详见：<https://mp.weixin.qq.com/s/oklQN_xjYy--_fbFkd9wMg>

### 代码

```java
class MedianFinder {
    private Queue<Integer> small;
    private Queue<Integer> large;

    public MedianFinder() {
        small = new PriorityQueue<>();
        large = new PriorityQueue<>((a, b) -> {
            return b - a;
        });
    }

    public void addNum(int num) {
        if (small.size() > large.size()) {
            small.offer(num);
            large.offer(small.poll());
        } else {
            large.offer(num);
            small.offer(large.poll());
        }
    }

    public double findMedian() {
        if (small.size() > large.size()) {
            return small.peek();
        } else if (small.size() < large.size()) {
            return large.peek();
        } else {
            return (small.peek() + large.peek()) / 2.0;
        }
    }
}
```

### References

---

#### 1. [数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/)

---
title: "LeetCode 382"
date: 2022-12-18T22:15:21+08:00
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

从一堆数据里随机取出一个数据，可以使用蓄水池抽样算法，详见思想篇章

### 代码

```java
class Solution {
    private ListNode head;

    public Solution(ListNode head) {
        this.head = head;
    }
    
    public int getRandom() {
        Random random = new Random();
        int i = 0, res = 0;
        ListNode p = head;
        while (p != null) {
            i++;
            if (random.nextInt(i) == 0) {
                res = p.val;
            }
            p = p.next;
        }
        return res;
    }
}
```

### References

---

#### 1. [链表随机节点](https://leetcode.cn/problems/linked-list-random-node/)

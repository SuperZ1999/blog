---
title: "LeetCode 2"
date: 2023-01-01T21:25:13+08:00
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

直接按位相加就可以了

### 代码

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(), p = res;
        int c = 0;
        while (l1 != null || l2 != null) {
            int v1 = l1 == null ? 0 : l1.val;
            int v2 = l2 == null ? 0 : l2.val;
            p.next = new ListNode((v1 + v2 + c) % 10);
            p = p.next;
            c = (v1 + v2 + c) / 10;
            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }
        if (c != 0) {
            p.next = new ListNode(c);
        }
        return res.next;
    }
}
```

### References

---

#### 1. [两数相加](https://leetcode.cn/problems/add-two-numbers/)

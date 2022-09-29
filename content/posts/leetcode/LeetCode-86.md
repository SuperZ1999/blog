---
title: "LeetCode 86"
date: 2022-09-23T00:09:37+08:00
tags: [leetcode]
draft: false
---

### 思路

从头到尾遍历一遍链表，将小于x的放到一个链表里，将大于等于x的放到一个链表里，最后再拼接这两个链表即可，注意dummy节点的使用。

### 我的代码

```java
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummy1 = new ListNode(-1), dummy2 = new ListNode(-1);
        ListNode p1 = dummy1, p2 = dummy2, p = head;

        while (p != null) {
            if (p.val < x) {
                p1.next = p;
                p1 = p1.next;
            } else {
                p2.next = p;
                p2 = p2.next;
            }
            ListNode temp = p.next;
            p.next = null;
            p = temp;
        }

        p1.next = dummy2.next;
        return dummy1.next;
    }
```

### References

---

#### 1. [分隔链表](https://leetcode.cn/problems/partition-list/)


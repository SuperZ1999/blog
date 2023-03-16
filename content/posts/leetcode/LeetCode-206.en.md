---
title: "LeetCode 206"
date: 2022-09-23T22:01:54+08:00
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

两种思路：

#### 递归

利用递归的思想，先反转head后面的，然后把head也反转即可。

#### 迭代

利用头插法的思想即可，直接看代码

### 代码

#### 递归

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        // 递归出口
        if (head == null || head.next == null) {
            return head;
        }

        ListNode last = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return last;
    }
}
```

#### 迭代

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newHead = new ListNode();
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead.next;
            newHead.next = head;
            head = next;
        }
        return newHead.next;
    }
}
```

### References

---

#### 1. [反转链表](https://leetcode.cn/problems/reverse-linked-list/)

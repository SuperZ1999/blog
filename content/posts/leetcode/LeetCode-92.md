---
title: "LeetCode 92"
date: 2022-09-23T22:52:35+08:00
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

#### 递归法

与反转链表前n个节点区别在于不是从第一个节点开始反转，而是从left开始，那么只需要利用递归一次head往后移一位，left和right分别减一的特性，把head移到left的位置，然后反转前n个节点即可。

#### 头插法

先找到反转链表的前驱节点，和前驱结点的后一个结点（其实就是反转后的尾结点），然后把尾结点后的结点插到前驱结点后，注意尾结点要连上下一个需要头插的结点。

### 代码

#### 递归法

```java
class Solution {
    private ListNode succesor = null;	// 后驱节点

    public ListNode reverseN(ListNode head, int n) {
        // 递归出口
        if (n == 1) {
            succesor = head.next;
            return head;
        }

        ListNode last = reverseN(head.next, n - 1);
        head.next.next = head;
        head.next = succesor;

        return last;
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (left == 1) {
            return reverseN(head, right);
        }

        head.next = reverseBetween(head.next, left - 1, right - 1);
        return head;
    }
}
```

#### 头插法

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(), tail = dummy, pre = dummy;
        dummy.next = head;
        for (int i = 0; i < left; i++) {
            pre = tail;
            tail = tail.next;
        }

        for (int i = left; i < right; i++) {
            ListNode cur = tail.next;
            tail.next = cur.next;
            cur.next = pre.next;
            pre.next = cur;
        }
        return dummy.next;
    }
}
```

### References

---

#### 1. [反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

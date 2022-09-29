---
title: "LeetCode 19"
date: 2022-09-23T12:32:27+08:00
tags: ["leetcode"]
draft: false
---

### 思路

关键是找到倒数第n+1个节点，找到倒数第n个节点的做法：先让p1指针走n步，然后p1和p2指针一起动，当p1指针到头了的时候，p2指针指向的就是需要找的节点。

注意使用dummy节点可以避免特殊性，比如就5个节点，删除倒数第5个，那需要找倒数第6个节点，可是总共就5个节点，会有空指针。

### 我的代码

```java
class Solution {
    private ListNode findFromEnd(ListNode head, int n) {
        ListNode p1 = head;
        // 先让p1指针走n步
        for (int i = 0; i < n; i++) {
            p1 = p1.next;
        }

        ListNode p2 = head;
        // p1指针走到头，p2指针指向的就是需要找的节点
        while (p1 != null) {
            p1 = p1.next;
            p2 = p2.next;
        }

        return p2;
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        // 找到倒数第n+1个节点
        ListNode node = findFromEnd(dummy, n + 1);
        node.next = node.next.next;

        return dummy.next;
    }
}
```

### References

---

#### 1. [删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

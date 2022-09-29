---
title: "LeetCode 92"
date: 2022-09-23T22:52:35+08:00
tags: ["leetcode"]
draft: false
---

### 思路

与反转链表前n个节点区别在于不是从第一个节点开始反转，而是从left开始，那么只需要利用递归一次head往后移一位，left和right分别减一的特性，把head移到left的位置，然后反转前n个节点即可。

### 我的代码

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

### References

---

#### 1. [反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

---
title: "LeetCode 206"
date: 2022-09-23T22:01:54+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用递归的思想，先反转head后面的，然后把head也反转即可。

### 我的代码

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

### References

---

#### 1. [反转链表](https://leetcode.cn/problems/reverse-linked-list/)

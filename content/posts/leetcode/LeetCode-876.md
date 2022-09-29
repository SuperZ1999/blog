---
title: "LeetCode 876"
date: 2022-09-23T14:18:22+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用快慢指针的思想，每当慢指针 `slow` 前进一步，快指针 `fast` 就前进两步，这样，当 `fast` 走到链表末尾时，`slow` 就指向了链表中点。

需要注意的是，如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点。

### 我的代码

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;

        // 经典快慢指针
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        return slow;
    }
}
```

### References

---

#### 1. [链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)
---
title: "LeetCode 141"
date: 2022-09-23T14:49:25+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用快慢指针的思想，如果快指针为空，说明没有环，如果快慢指针相遇说明有环

### 我的代码

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;

        // 快慢指针如果相遇，说明链表有环
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return true;
            }
        }

        return false;
    }
}
```

### References

---

#### 1. [环形链表](https://leetcode.cn/problems/linked-list-cycle/)
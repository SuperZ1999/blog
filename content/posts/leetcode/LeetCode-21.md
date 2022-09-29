---
title: "LeetCode 21"
date: 2022-09-22T23:42:59+08:00
tags: ["leetcode"]
draft: false
---

### 思路

不解释

### 我的代码

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1), p = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                p.next = list1;
                list1 = list1.next;
            } else {
                p.next = list2;
                list2 = list2.next;
            }
            p = p.next;
        }

        if (list1 != null) {
            p.next = list1;
        }
        if (list2 != null) {
            p.next = list2;
        }

        return dummy.next;
    }
}
```

### References

---

#### 1. [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

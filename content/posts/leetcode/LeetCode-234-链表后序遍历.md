---
title: "LeetCode 234 链表后序遍历"
date: 2022-09-24T00:00:43+08:00
tags: ["leetcode"]
draft: false
---

### 思路

链表也可以后序遍历，这道题只需要使用后序遍历，然后提前存一下head，从两边向中间逼近就可以了。

### 我的代码

```java
class Solution {
    private ListNode left;

    public boolean isPalindrome(ListNode head) {
        left = head;
        return traverse(head);
    }

    private boolean traverse(ListNode right) {
        if (right == null) {
            return true;
        }

        boolean res = traverse(right.next);
        res = res && (left.val == right.val);
        left = left.next;

        return res;
    }
}
```

### References

---

#### 1. [回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

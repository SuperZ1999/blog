---
title: "LeetCode 234 快慢指针+反转链表"
date: 2022-09-24T00:05:26+08:00
tags: ["leetcode"]
draft: false
---

### 思路

先用快慢指针找到链表的中点，从而找到回文串的后一半，然后将后一半反转，然后判断前后两部分是否相等就行了。

### 我的代码

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        // 快慢指针找中点
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        // 如果是奇数个节点，slow需要后移一位
        if (fast != null) {
            slow = slow.next;
        }

        // 反转slow之后的
        ListNode right = reverse(slow), left = head;

        // 判断回文
        while (right != null) {
            if (left.val != right.val) {
                return false;
            }
            left = left.next;
            right = right.next;
        }
        return true;
    }

    private ListNode reverse(ListNode head) {
        ListNode pre = null, cur = head;
        while (cur != null) {
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }
}
```

### References

---

#### 1. [回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

---
title: "LeetCode 25"
date: 2022-09-23T23:21:30+08:00
tags: ["leetcode"]
draft: false
---

### 思路

**1、先反转以 `head` 开头的 `k` 个元素**。

**2、将第 `k + 1` 个元素作为 `head` 递归调用 `reverseKGroup` 函数**。

**3、将上述两个过程的结果连接起来**。

注意base case为最后元素不足 k 个时的情况

### 我的代码

```java
class Solution {
    private ListNode reverse(ListNode a, ListNode b) {
        // 这个做法需要对第一个节点特殊判断
//        if (head == null) {
//            return null;
//        }
//
//        ListNode pre = head, cur = head.next;
//        head.next = null;
//        while (cur != null) {
//            ListNode temp = cur.next;
//            cur.next = pre;
//            cur = temp;
//        }
//
//        return pre;
        // 这个做法不需要对第一个节点特殊判断
        ListNode pre = null, cur = a;
        while (cur != b) {
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode p = head;
        // 找出前k个节点，不满k个直接return
        for (int i = 0; i < k; i++) {
            if (p == null) {
                return head;
            }
            p = p.next;
        }

        // 反转前k个
        ListNode newHead = reverse(head, p);

        // 拼接后面反转后的链表
        head.next = reverseKGroup(p, k);

        return newHead;
    }
}
```

### References

---

#### 1. [K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

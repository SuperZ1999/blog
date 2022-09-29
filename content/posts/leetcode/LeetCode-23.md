---
title: "LeetCode 23"
date: 2022-09-23T10:47:55+08:00
tags: ["leetcode"]
draft: false
---

### 思路

每次取出一个最小的加到链表中去，那问题就是怎么高效的获取最小的节点，这很明显用优先队列（二叉堆）就可以解决这个问题。

### 我的代码

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        // 创建优先队列，将头节点加入
        ListNode dummy = new ListNode(-1), p = dummy;
        PriorityQueue<ListNode> pq = new PriorityQueue<>(lists.length, (a, b) -> {
            return a.val - b.val;
        });
        for (ListNode head : lists) {
            if (head != null) {
                pq.add(head);
            }
        }

        // 每次取出来一个最小的
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            p.next = node;
            p = p.next;
            if (node.next != null) {
                pq.add(node.next);
            }
        }

        return dummy.next;
    }
}
```

### References

---

#### 1.[合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

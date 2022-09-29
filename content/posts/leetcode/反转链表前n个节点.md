---
title: "反转链表前n个节点"
date: 2022-09-23T22:20:19+08:00
tags: ["leetcode"]
draft: false
---

### 思路

解决思路和反转整个链表差不多，只要稍加修改即可：

1、base case 变为 `n == 1`，反转一个元素，就是它本身，同时**要记录后驱节点**。

2、刚才我们直接把 `head.next` 设置为 null，因为整个链表反转后原来的 `head` 变成了整个链表的最后一个节点。但现在 `head` 节点在递归反转之后不一定是最后一个节点了，所以要记录后驱 `successor`（第 `n + 1` 个节点），反转之后将 `head` 连接上。

[![img](https://labuladong.gitee.io/algo/images/%e5%8f%8d%e8%bd%ac%e9%93%be%e8%a1%a8/7.jpg)](https://labuladong.gitee.io/algo/images/反转链表/7.jpg)

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
}
```


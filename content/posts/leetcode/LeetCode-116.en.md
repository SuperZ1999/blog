---
title: "LeetCode 116"
date: 2022-10-11T14:33:15+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

有两种思路，分别是层序遍历和把间隙看成结点的遍历

#### 思路一

层序遍历，遍历一层就把这层的结点加上next，没什么好说的

#### 思路二

把间隙看成结点，那么间隙组成的数据结构就是一颗三叉树，遍历这个三叉树即可解决问题，每个间隙结点需要做的事是把这个间隙的两个结点连接起来，在前中后序位置都可以

### 我的代码

#### 思路一

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return null;
        }

        Deque<Node> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node cur = queue.poll();
                if (cur.left != null) {
                    queue.offer(cur.left);
                    queue.offer(cur.right);
                }
                if (i == size - 1) {
                    cur.next = null;
                } else {
                    cur.next = queue.peek();
                }
            }
        }

        return root;
    }
}
```

#### 思路二

```java
class Solution {
    private void traverse(Node left, Node right) {
        if (left == null) {
            return;
        }
        left.next = right;
        traverse(left.left, left.right);
        traverse(left.right, right.left);
        traverse(right.left, right.right);
    }

    public Node connect(Node root) {
        if (root == null) {
            return null;
        }

        traverse(root.left, root.right);

        return root;
    }
}
```

### References

---

#### 1. [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

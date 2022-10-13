---
title: "LeetCode 114"
date: 2022-10-11T15:09:41+08:00
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

由于题目要求原地转换为链表所以不能使用遍历的方法，一边遍历一遍新建一个链表，只能使用分解问题的思路

将该问题分解为：左子树展开+右子树展开+将右子树接到左子树上，即可，不过需要注意左右子树为空的情况

### 代码

```java
class Solution {
    private TreeNode tranToLinkedList(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode left = root.left;
        TreeNode right = root.right;
        TreeNode leftLast = tranToLinkedList(left);
        TreeNode rightLast = tranToLinkedList(right);
        if (leftLast == null) {
            root.left = null;
            root.right = right;
        } else if (rightLast == null) {
            root.left = null;
            root.right = left;
        } else {
            root.left = null;
            root.right = left;
            leftLast.right = right;
        }

        return rightLast != null ? rightLast : (leftLast != null ? leftLast : root);
    }

    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        tranToLinkedList(root);
    }
}
```

### References

---

#### 1. [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

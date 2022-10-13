---
title: "LeetCode 226"
date: 2022-10-11T13:48:45+08:00
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

遍历方式和分解方式都可以

#### 遍历思路

利用二叉树的遍历思想，遍历一遍，遍历的时候，将每个正在遍历的结点交换左右子树即可

#### 分解思路

利用二叉树的分解问题思想，将原问题分解为左子树的翻转和右子树的分解，然后翻转左右子树

### 代码

#### 遍历思路

```java
class Solution {
    private void traverse(TreeNode root) {
        if (root == null) {
            return;
        }

        TreeNode temp = root.right;
        root.right = root.left;
        root.left = temp;

        traverse(root.left);
        traverse(root.right);
    }

    public TreeNode invertTree(TreeNode root) {
        traverse(root);
        return root;
    }
}
```

#### 分解思路

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);

        root.left = right;
        root.right = left;
        return root;
    }
}
```

### References

---

#### 1. [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

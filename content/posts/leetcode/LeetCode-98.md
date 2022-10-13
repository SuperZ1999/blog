---
title: "LeetCode 98"
date: 2022-10-13T15:34:20+08:00
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

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，从而判断是都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去

### 我的代码

```java
class Solution {
    private boolean isValidBST(TreeNode root, TreeNode min, TreeNode max) {
        if (root == null) {
            return true;
        }
        if (min != null && root.val <= min.val) return false;
        if (max != null && root.val >= max.val) return false;
        return isValidBST(root.left, min, root) & isValidBST(root.right, root, max);
    }

    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, null, null);
    }
}
```

### References

---

#### 1. [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)


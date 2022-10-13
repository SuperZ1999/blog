---
title: "LeetCode 701"
date: 2022-10-13T16:21:01+08:00
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

类比构造二叉树，需要把问题分解为：构造root+构造左子树+构造右子树，注意只有root为null时需要构造

### 我的代码

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        if (val > root.val) {
            root.right = insertIntoBST(root.right, val);
        }
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        }
        return root;
    }
}
```

### References

---

#### 1. [二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

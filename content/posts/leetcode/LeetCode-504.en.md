---
title: "LeetCode 504"
date: 2022-10-14T10:37:01+08:00
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

删除时先把删除的结点跟root比较，小于root在左子树中删除，大于root在右子树中删除，等于root时，需要删除root，有以下三种情况：

1. root左右皆为空，此时直接删除
2. root左右有一个为空，将不为空的子树替换为当前结点的位置
3. root左右都不为空，找左子树中最大的或右子树中最小的替换root

### 我的代码

```java
class Solution {
    private TreeNode getMin(TreeNode root) {
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }

    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (root.val == key) {
            // 删除该结点
            if (root.left == null && root.right == null) {
                return null;
            }
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode min = getMin(root.right);
            root.right = deleteNode(root.right, min.val);
            min.left = root.left;
            min.right = root.right;
            root = min;
        }
        if (key > root.val) {
            root.right = deleteNode(root.right, key);
        }
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        }
        return root;
    }
}
```

### References

---

#### 1. [删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/)

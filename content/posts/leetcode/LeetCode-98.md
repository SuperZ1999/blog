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

两种思路：

#### 递归

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小+右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，而判断是子树的节点都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去

#### 中序遍历

先中序遍历，然后看遍历的序列是不是有序的

### 我的代码

#### 递归

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

#### 中序遍历

```java
class Solution {
    private List<Integer> track = new LinkedList<>();

    public boolean isValidBST(TreeNode root) {
        inorder(root);
        for (int i = 0; i < track.size() - 1; i++) {
            if (track.get(i) >= track.get(i + 1)) {
                return false;
            }
        }
        return true;
    }

    private void inorder(TreeNode root) {
        if (root == null) {
            return;
        }

        inorder(root.left);
        track.add(root.val);
        inorder(root.right);
    }
}
```

### References

---

#### 1. [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)


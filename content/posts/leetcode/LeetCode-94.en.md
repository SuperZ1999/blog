---
title: "LeetCode 94"
date: 2023-02-24T22:16:35+08:00
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

三种思路：

#### 递归

经典二叉树中序遍历，闭着眼写，详见思想篇章

#### 迭代

暂时没看

#### Morris 中序遍历

感觉没必要看

### 代码

#### 递归

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorderTraversal(root, res);
        return res;
    }

    private void inorderTraversal(TreeNode root, List<Integer> res) {
        if (root == null) {
            return;
        }

        inorderTraversal(root.left, res);
        res.add(root.val);
        inorderTraversal(root.right, res);
    }
}
```

### References

---

#### 1. [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

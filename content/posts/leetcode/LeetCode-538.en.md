---
title: "LeetCode 538"
date: 2022-10-13T14:42:01+08:00
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

因为要累加比自己更大的结点的值，所以完全可以在升序序列里倒着遍历，把累加的值放到节点里去，所以这里采用中序遍历，但是是先右子树再左子树，这样的话遍历到当前节点的时候，比这个结点大的结点已经遍历完了，用个变量累加一下，然后赋值给当前结点就可以了

### 我的代码

```java
class Solution {
    private int sum = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root == null) {
            return null;
        }
        convertBST(root.right);
        sum += root.val;
        root.val = sum;
        convertBST(root.left);

        return root;
    }
}
```

### References

---

#### 1. [把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

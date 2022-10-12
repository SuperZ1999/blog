---
title: "LeetCode 105"
date: 2022-10-12T11:53:59+08:00
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

经典根据前中遍历序列构造树，利用分解问题的思想，将问题拆分为找出root+构造左子树+构造右子树，前序遍历第一个就是root，再根据root在中序遍历的位置得到左右子树节点的个数，再构造左右子树即可

注意这里可以用map优化通过元素的值找所在数组的索引，用一个valToIndex的hashmap即可

### 我的代码

```java
class Solution {
    private Map<Integer, Integer> valToIndex = new HashMap();

    private TreeNode build(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart > preEnd) {
            return null;
        }

        int val = preorder[preStart];
        TreeNode root = new TreeNode(val);
        int index = valToIndex.get(val);
        int leftSize = index - inStart;
        TreeNode left = build(preorder, preStart + 1, preStart + leftSize,
                inorder, inStart, index - 1);
        TreeNode right = build(preorder, preStart + leftSize + 1, preEnd,
                inorder, index + 1, inEnd);
        root.left = left;
        root.right = right;

        return root;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            valToIndex.put(inorder[i], i);
        }
        return build(preorder, 0, preorder.length - 1,
                inorder, 0, inorder.length - 1);
    }
}
```

### References

---

#### 1. [从前序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

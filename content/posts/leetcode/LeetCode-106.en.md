---
title: "LeetCode 106"
date: 2022-10-12T12:05:51+08:00
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

同LeetCode-105，就是改一下递归的参数

详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-105/>

### 代码

```java
class Solution {
    private Map<Integer, Integer> valToIndex = new HashMap();

    private TreeNode build(int[] postorder, int postStart, int postEnd, int[] inorder, int inStart, int inEnd) {
        if (postStart > postEnd) {
            return null;
        }

        int val = postorder[postEnd];
        TreeNode root = new TreeNode(val);
        int index = valToIndex.get(val);
        int leftSize = index - inStart;
        TreeNode left = build(postorder, postStart, postStart + leftSize - 1,
                inorder, inStart, index - 1);
        TreeNode right = build(postorder, postStart + leftSize, postEnd - 1,
                inorder, index + 1, inEnd);
        root.left = left;
        root.right = right;

        return root;
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for (int i = 0; i < inorder.length; i++) {
            valToIndex.put(inorder[i], i);
        }
        return build(postorder, 0, postorder.length - 1,
                inorder, 0, inorder.length - 1);
    }
}
```

### References

---

#### 1. [从后序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

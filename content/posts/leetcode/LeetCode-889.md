---
title: "LeetCode 889"
date: 2022-10-12T13:57:30+08:00
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

同LeetCode-105，就是改一下递归的参数，而且前序和后序无法唯一确定一棵树

详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-105/>

### 代码

```java
class Solution {
    private Map<Integer, Integer> valToIndex = new HashMap();

    private TreeNode build(int[] preorder, int preStart, int preEnd, int[] postorder, int postStart, int postEnd) {
        if (preStart > preEnd) {
            return null;
        }
        if (preStart == preEnd) {
            return new TreeNode(preorder[preStart]);
        }

        int val = preorder[preStart];
        TreeNode root = new TreeNode(val);
        int leftIndex = valToIndex.get(preorder[preStart + 1]);
        int leftSize = leftIndex - postStart + 1;
        TreeNode left = build(preorder, preStart + 1, preStart + leftSize,
                postorder, postStart, leftIndex);
        TreeNode right = build(preorder, preStart + leftSize + 1, preEnd,
                postorder, leftIndex + 1, postEnd - 1);
        root.left = left;
        root.right = right;

        return root;
    }

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        for (int i = 0; i < postorder.length; i++) {
            valToIndex.put(postorder[i], i);
        }
        return build(preorder, 0, preorder.length - 1,
                postorder, 0, postorder.length - 1);
    }
}
```

### References

---

#### 1. [根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

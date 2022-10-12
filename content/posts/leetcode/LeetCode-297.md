---
title: "LeetCode 297"
date: 2022-10-12T15:25:34+08:00
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

有空再写

### 我的代码

```java
public class Codec {
    private static final char NULL = '#';
    private static final char SEP = ',';

    private void doSerialize(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append(NULL).append(SEP);
            return;
        }

        sb.append(root.val).append(SEP);
        doSerialize(root.left, sb);
        doSerialize(root.right, sb);
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        doSerialize(root, sb);
        return sb.toString();
    }

    private TreeNode newTreeNode(String val) {
        if ("#".equals(val)) {
            return new TreeNode(-1001);
        }
        return new TreeNode(Integer.parseInt(val));
    }

    private TreeNode fixTree(TreeNode root) {
        if (root == null || root.val == -1001) {
            return null;
        }

        root.left = fixTree(root.left);
        root.right = fixTree(root.right);

        return root;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] nodes = data.split(",");
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode dummyRoot = new TreeNode(1001);
        stack.push(dummyRoot);
        for (int i = 0; i < nodes.length; i++) {
            stack.push(newTreeNode(nodes[i]));
            while (stack.peek().val == -1001 || stack.peek().left != null && stack.peek().right != null) {
                TreeNode peek = stack.pop();
                if (stack.peek().left == null) {
                    stack.peek().left = peek;
                } else {
                    stack.peek().right = peek;
                }
            }
        }
        return fixTree(dummyRoot).left;
    }
}
```

### References

---

#### 1. [二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)

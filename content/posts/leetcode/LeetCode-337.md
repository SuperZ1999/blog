---
title: "LeetCode 337"
date: 2022-12-12T15:03:50+08:00
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

同[LeetCode-198](https://superz1999.github.io/blog/posts/leetcode/leetcode-198/)，只不过变成了二叉树

### 代码

#### 原版

```java
class Solution {
    private Map<TreeNode, Integer> memo = new HashMap<>();

    public int rob(TreeNode root) {
        if (root == null) {
            return 0;
        }
        if (memo.containsKey(root)) {
            return memo.get(root);
        }
        int do_it = root.val
                + (root.left == null ? 0 : rob(root.left.left) + rob(root.left.right))
                + (root.right == null ? 0 : rob(root.right.left) + rob(root.right.right));
        int not_do = rob(root.left) + rob(root.right);
        int res = Math.max(do_it, not_do);
        memo.put(root, res);
        return res;
    }
}
```

#### 更加优秀的版本

```java
class Solution {
    private int[] dp(TreeNode root) {
        if (root == null) {
            return new int[]{0, 0};
        }
        int[] left = dp(root.left);
        int[] right = dp(root.right);
        int do_it = root.val + left[0] + right[0];
        int not_do = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{not_do, do_it};
    }

    public int rob(TreeNode root) {
        int[] res = dp(root);
        return Math.max(res[0], res[1]);
    }
}
```

### References

---

#### 1. [打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/)

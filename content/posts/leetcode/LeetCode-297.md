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

#### 我的思路

序列化采用前序遍历即可，反序列化先把序列化的字符串分隔开，然后将分割的元素转换为结点，逐个加入栈中，并且判断栈顶是不是完整的树（空结点和左右子树都不为null的结点），如果是那就出栈挂在新栈顶的左子树或右子树上，循环往复，直到所有的结点都被加入到栈中，树就被反序列化完成了

#### 官方思路一

序列化和反序列化均采用分解问题的思想，序列化不用多说，这里把反序列化问题拆分为：新建根节点+反序列化左子树+反序列化右子树（我当时为什么没想到，因为没想到还要写base case）

#### 官方思路二

使用文法的思想，可以将树用`T -> (T) num (T) | X`文法来序列化和反序列化，其实本质思路和我的思路一样

### 代码

#### 我的代码

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

#### 官方思路一

```java
public class Codec {
    public String serialize(TreeNode root) {
        return rserialize(root, "");
    }
  
    public TreeNode deserialize(String data) {
        String[] dataArray = data.split(",");
        List<String> dataList = new LinkedList<String>(Arrays.asList(dataArray));
        return rdeserialize(dataList);
    }

    public String rserialize(TreeNode root, String str) {
        if (root == null) {
            str += "None,";
        } else {
            str += str.valueOf(root.val) + ",";
            str = rserialize(root.left, str);
            str = rserialize(root.right, str);
        }
        return str;
    }
  
    public TreeNode rdeserialize(List<String> dataList) {
        if (dataList.get(0).equals("None")) {
            dataList.remove(0);
            return null;
        }
  
        TreeNode root = new TreeNode(Integer.valueOf(dataList.get(0)));
        dataList.remove(0);
        root.left = rdeserialize(dataList);
        root.right = rdeserialize(dataList);
    
        return root;
    }
}
```

#### 官方思路二

```java
public class Codec {
    public String serialize(TreeNode root) {
        if (root == null) {
            return "X";
        }
        String left = "(" + serialize(root.left) + ")";
        String right = "(" + serialize(root.right) + ")";
        return left + root.val + right;
    }

    public TreeNode deserialize(String data) {
        int[] ptr = {0};
        return parse(data, ptr);
    }

    public TreeNode parse(String data, int[] ptr) {
        if (data.charAt(ptr[0]) == 'X') {
            ++ptr[0];
            return null;
        }
        TreeNode cur = new TreeNode(0);
        cur.left = parseSubtree(data, ptr);
        cur.val = parseInt(data, ptr);
        cur.right = parseSubtree(data, ptr);
        return cur;
    }

    public TreeNode parseSubtree(String data, int[] ptr) {
        ++ptr[0]; // 跳过左括号
        TreeNode subtree = parse(data, ptr);
        ++ptr[0]; // 跳过右括号
        return subtree;
    }

    public int parseInt(String data, int[] ptr) {
        int x = 0, sgn = 1;
        if (!Character.isDigit(data.charAt(ptr[0]))) {
            sgn = -1;
            ++ptr[0];
        }
        while (Character.isDigit(data.charAt(ptr[0]))) {
            x = x * 10 + data.charAt(ptr[0]++) - '0';
        }
        return x * sgn;
    }
}
```

### References

---

#### 1. [二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)

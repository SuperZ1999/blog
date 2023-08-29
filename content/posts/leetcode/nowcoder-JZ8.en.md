---
title: "nowcoder JZ8"
date: 2023-08-29T22:56:46+08:00
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

有两种思路：

#### 中序遍历法

先中序遍历一次，得到遍历序列，然后从序列里找到当前待查找的结点，然后再找到这个节点的下一个节点

#### 分类直接寻找法

可以分成三种情况

1. 该结点存在右子树，那么下一个节点就是右子树最左边的结点
2. 该结点不存在右子树，且该结点是父结点的左子树，那么下一个节点就是父结点
3. 该结点不存在右子树，且该结点是父结点的右子树，则先要沿着左上方父节点爬树，一直爬到当前结点是其父节点的左子节点为止，返回的就是这个父节点；或者没有满足上述情况的则返回为NULL

其中第二三种情况可以合并，合并成从当前结点开始找，找到当前结点是其父节点的左子节点为止

### 代码

#### 中序遍历法

```java
public class Solution {
    ArrayList<TreeLinkNode> nodes = new ArrayList<>();
    public TreeLinkNode GetNext(TreeLinkNode pNode) {
        // 获取根节点
        TreeLinkNode root = pNode;
        while(root.next != null) root = root.next;
        
        // 中序遍历打造nodes
        InOrder(root);
        
        // 进行匹配
        int n = nodes.size();
        for(int i = 0; i < n - 1; i++) {
            TreeLinkNode cur = nodes.get(i);
            if(pNode == cur) {
                return nodes.get(i+1);
            }
        }
        return null;
    }
    
    // 中序遍历
    void InOrder(TreeLinkNode root) {
        if(root != null) {
            InOrder(root.left);
            nodes.add(root);
            InOrder(root.right);
        }
    }
}

```

#### 分类直接寻找法

```java
public class Solution {
    public TreeLinkNode GetNext(TreeLinkNode pNode) {
        if (pNode.right != null) {
            TreeLinkNode node = pNode.right;
            while (node.left != null) {
                node = node.left;
            }
            return node;
        }
        while (pNode != null) {
            if (pNode.next == null) {
                return null;
            }
            if (pNode.next.left == pNode) {
                return pNode.next;
            }
            pNode = pNode.next;
        }
        return null;
    }
}
```

### References

---

#### 1. [二叉树的下一个结点](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e)

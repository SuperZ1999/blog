---
title: "LeetCode Note"
date: 2022-09-23T10:21:48+08:00
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

# 链表

## 合并两个有序链表

### 解法

略

### 题目

#### 1. [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-21/>

## 单链表的分解

### 解法

从头到尾遍历一遍链表，将小于x的放到一个链表里，将大于等于x的放到一个链表里，最后再拼接这两个链表即可，注意dummy节点的使用。

### 题目

#### 1. [分隔链表](https://leetcode.cn/problems/partition-list/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-86/>

## 合并 k 个有序链表

### 解法

每次取出一个最小的加到链表中去，那问题就是怎么高效的获取最小的节点，这很明显用优先队列（二叉堆）就可以解决这个问题。

### 题目

#### 1. [合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-23/>

## 寻找单链表的倒数第 k 个节点

### 解法

关键是找到倒数第n+1个节点，找到倒数第n个节点的做法：先让快指针走n步，然后快慢指针一起动，当快指针到头了的时候，慢指针指向的就是需要找的节点。

注意使用dummy节点可以避免特殊性，比如就5个节点，删除倒数第5个，那需要找倒数第6个节点，可是总共就5个节点，会有空指针。

### 题目

#### 1. [删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-19/>

## 单链表的中点

### 解法

利用快慢指针的思想，每当慢指针 `slow` 前进一步，快指针 `fast` 就前进两步，这样，当 `fast` 走到链表末尾时，`slow` 就指向了链表中点。

需要注意的是，如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点。

### 题目

#### 1. [链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-876/>

## 判断链表是否包含环

### 解法

利用快慢指针的思想，如果快指针为空，说明没有环，如果快慢指针相遇说明有环

### 题目

#### 1. [环形链表](https://leetcode.cn/problems/linked-list-cycle/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-141/>

## 存在环的链表中寻找环起点

### 解法

利用快慢指针的思想并且稍做分析，即可得出结论：当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置。

### 题目

#### 1. [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-142/>

## 判断两个链表是否相交

### 解法

找到相交点的关键是将相交点之前的节点数凑成相等的，这样的话同时遍历，如果相等的话就是相交了。怎么凑呢？将两个链表连接一下，节点数不就想等了吗。

代码实现方面，可以考虑四种情况：

1. 长度相等，有相交
2. 长度相等，无相交
3. 长度不等，有相交
4. 长度不等，无相交

符合这四种情况的链表连接方法如下：

l1 -> null -> l2 -> null

l2 -> null -> l1 -> null

另一种做法：将某一条链表首尾相连，该问题就转换为寻找有环链表的环起点问题。

### 题目

#### 1. [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-160/>

## 反转单链表

### 解法

利用递归的思想，先反转head后面的，然后把head也反转即可。

### 思想

反转的过程就是改变指针方向的过程并且最后一个指向null，比如反转第2个---第5个：

1 -> 2 -> 3 -> 4 -> 5 -> null

反转后为：

1 -> 2 <- 3 <- 4 <- 5

​	 null

### 题目

#### 1. [反转链表](https://leetcode.cn/problems/reverse-linked-list/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-206/>

## 反转链表前n个节点

### 解法

解决思路和反转整个链表差不多，只要稍加修改即可：

1、base case 变为 `n == 1`，反转一个元素，就是它本身，同时**要记录后驱节点**。

2、刚才我们直接把 `head.next` 设置为 null，因为整个链表反转后原来的 `head` 变成了整个链表的最后一个节点。但现在 `head` 节点在递归反转之后不一定是最后一个节点了，所以要记录后驱 `successor`（第 `n + 1` 个节点），反转之后将 `head` 连接上。

### 题目

无

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/反转链表前n个节点/>

## 反转链表节点(m, n)

### 解法

与反转链表前n个节点区别在于不是从第一个节点开始反转，而是从left开始，那么只需要利用递归一次head往后移一位，left和right分别减一的特性，把head移到left的位置，然后反转前n个节点即可。

### 题目

#### 1. [反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-92/>

## K 个一组翻转链表

### 解法

**1、先反转以 `head` 开头的 `k` 个元素**。

**2、将第 `k + 1` 个元素作为 `head` 递归调用 `reverseKGroup` 函数**。

**3、将上述两个过程的结果连接起来**。

注意base case为最后元素不足 k 个时的情况

### 题目

#### 1. [K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-25/>

## 链表的前后序遍历

```java
void traverse(ListNode head) {
    // 前序遍历代码
    traverse(head.next);
    // 后序遍历代码
}
```

## 回文串

### 寻找回文串

核心思想是从中心向两端扩展

### 判断回文串

核心思想是从两端向中间逼近

## 判断回文链表

### 解法

可以将链表全部反转，也可以部分反转

#### 链表全部反转

链表全部反转的方法共3种：

##### 将原链表反转，然后与原链表比较

略

##### 链表后序遍历

链表也可以后序遍历，这道题只需要使用后序遍历，然后提前存一下head，从两边向中间逼近就可以了。

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-234-链表后序遍历/>

##### 利用栈

同链表后序遍历

#### 链表部分反转

##### 快慢指针+反转链表

先用快慢指针找到链表的中点，从而找到回文串的后一半，然后将后一半反转，然后判断前后两部分是否相等就行了。

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-234-快慢指针+反转链表/>

### 题目

#### 1. [回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

# 数组

## 快慢指针在数组中的应用

### 数组元素去重

#### 解法

慢指针指向当前已经去重的数据的最后一个，快指针去前面探路，碰到和slow不一样的数据就让这个数据放在slow后面，slow++。

具体变种详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-26+83+27+283/>

#### 题目

##### 1. [删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

##### 2. [删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)

##### 3. [移除元素](https://leetcode.cn/problems/remove-element/)

##### 4. [移动零](https://leetcode.cn/problems/move-zeroes/)

### 滑动窗口

#### 解法

`left` 指针在后，`right` 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

详见思想章节

#### 题目

##### 1. [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-76/>

##### 2. [字符串的排列](https://leetcode.cn/problems/permutation-in-string/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-567/>

##### 3. [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-438/>

##### 4. [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-3/>

## 左右指针在数组中的应用

### 二分查找

#### 解法

就是将搜索空间合理的分成两部分，摒弃不可能的那部分，缩减搜索空间，加快搜索速度，详见思想章节

#### 题目

##### 1. [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-34/>

##### 2. [二分查找](https://leetcode.cn/problems/binary-search/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-704/>

### 两数之和

#### 解法

利用左右指针的思想，从两边向中间逼近，如果左右之和太大，那就right--，否则left++，直到左右之和等于target。

#### 题目

##### 1. [两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-167/>

### 反转数组

#### 解法

利用左右指针的思想，从两边向中间逼近，同时交换左右的值

##### 扩展

###### 反转字符数组里的单词

先反转整个数组，然后再反转各个单词即可

###### 旋转矩阵

先按对角线对折矩阵（注意对折矩阵时，只需要遍历矩阵的一半即可，如果整个矩阵都遍历，那矩阵不会有任何变化，相当于对折了两次），再反转矩阵的每一行即可

#### 题目

##### 1. [反转字符串](https://leetcode.cn/problems/reverse-string/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-344/>

##### 2. [反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-151/>

##### 3. [旋转图像](https://leetcode.cn/problems/rotate-image/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-48/>

### 回文串判断

#### 解法

遍历一遍数组，同时从中心向两边寻找回文串，并且保存最长的即可。

#### 题目

##### 1. [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-5/>

## 前缀和在数组里的应用

### 一维数组中的前缀和

#### 解法

利用前缀和的思想轻松秒杀，需要注意在preSum中，第n + 1个元素存的时nums前n个元素的和，整体往后挪一位

#### 题目

##### 1. [区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-303/>

### 二维数组中的前缀和

#### 解法

利用前缀和的思想轻松秒杀，需要注意在preSum中，第[n + 1, n+1]个元素存的是matrix前n*n个元素的和，整体往右下挪一位

还需要注意做减法时，会多减一块区域，需要加回来

#### 题目

##### 1. [二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-304/>

## 差分数组

### 解法

详见思想章节

### 题目

#### 1. [航班预订统计](https://leetcode.cn/problems/corporate-flight-bookings/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1109/>

#### 2. [拼车](https://leetcode.cn/problems/car-pooling/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-1094/>

## 矩阵的螺旋遍历

### 解法

**解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界**：

![img](https://labuladong.gitee.io/algo/images/%e8%8a%b1%e5%bc%8f%e9%81%8d%e5%8e%86/6.png)

需要注意水平遍历需要判断upperBound<=lowerBound，垂直遍历需要判断leftBound<=rightBound

### 题目

#### 1. [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-54/>

#### 2. [螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-59/>

## 带权重的随机选择算法

### 解法

可以想象成一条线段，分成好几段，每段长度不一样，然后往上面撒石子，返回石子撒到了第几条线段上，直接把这个线段当成一个数组不现实，因为数值有可能很大，所以可以压缩一下，把每一段的长度当成一个元素，但这样寻找随机数处在哪一段还得把前面都加起来，不方便，那就压缩成一个前缀和数组，这样只需要从左往右遍历前缀和数组找第一个大于等于随机数的元素就行了，但是前缀和数组是一个有序数组，我们寻找第一个大于等于随机数的元素使用二分查找就可以快速定位，不需要从头遍历一遍

有两个需要注意的地方：

1. ”线段“和前缀和的”格子“的对应关系需要想清楚，这个画张图就明白了
2. 寻找第一个大于等于随机数的元素，需要用寻找左边界的二分查找，而不是寻找右边界的二分查找，详见思想章节二分查找注意点第10条

### 题目

#### 1. [按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-528/>

## 常数时间删除/查找数组中的任意元素

### 解法

为了随机选取元素，需要用到数组，并且得是紧凑的，但是数组增删不是O(1)的，所以再来个map，key是数组元素的值，value是数组的索引，这样就做到了O(1)的数组增删，增删的时候注意修改map和数组

核心思想就是为了随机选取元素，肯定得用**数组**存，并且得是**紧凑**的

### 题目

#### 1. [O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-380/>

#### 2. [黑名单中的随机数](https://leetcode.cn/problems/random-pick-with-blacklist/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-710/>

# 二叉树

## 遍历问题

### 解法

利用前中后序遍历模板（见思想），用一个 traverse 函数配合外部变量来实现。

搞清楚二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 题目

#### 1. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-104/>

#### 2. [二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

题解略

#### 3. [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-226/>

#### 4. [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-116/>

## 分解问题

### 解法

主要思想就是定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案

首先写出这个递归函数的定义，并充分利用这个函数的返回值(这个返回值就是需要用到的子树信息)。

搞清楚二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 题目

#### 1. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-104/>

#### 2. [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-543/>

#### 3. [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-226/>

#### 4. [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-114/>

## 层序遍历

### 解法

就是一个BFS，可以计算一些类似结点与root之间的距离的问题。详见思想里的模板

### 题目

#### 1. [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-116/>

## 构造二叉树

### 解法

二叉树的构造问题一般都是使用「分解问题」的思想：构造整棵树 = 根节点 + 构造左子树 + 构造右子树。

### 题目

#### 1. [最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-654/>

#### 2. [从前序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-105/>

#### 3. [从后序和中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-106/>

#### 4. [根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-889/>

## 二叉搜索树性质

### 解法

只需要利用二叉树左边子树全部小于根节点，右边全部大于根节点，中序遍历就是升序序列就可以了

### 题目

#### 1. [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-230/>

#### 2. [把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-538/>

## 二叉搜索树合法性

### 解法

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，从而判断是都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去

### 题目

#### 1. [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-98/>

## 二叉搜索树增删改查

### 解法

见思想

### 题目

#### 1. [二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-700/>

#### 2. [二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-701/>

#### 3. [删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-504/>

## n个结点的BST的种类

### 解法

#### 递归思路

递归函数定义为n个结点可以组成几种BST，那么对于n个结点的BST的种类=将n个结点逐个当成root，左右子树的种类相乘，再把这些结果相加就是n个结点BST的种类

#### 动态规划

递归明显有重复计算的问题，我们可以对已经计算好的数据进行存储，需要时就不需要重新计算了，这种重复利用子问题的解的方式就是动态规划

### 题目

#### 1. [不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-96/>

#### 2. [不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-95/>

## 扁平化嵌套列表迭代器

### 解法

#### 思路一

将NestedInteger当成树的节点，list当成该节点的孩子，那么只需要遍历该树就可以完成迭代了，直接看代码

#### 思路二

思路一会在构造的时候将此树遍历一遍，所以速度会很慢，最好弄成懒惰式的，所以可以把NestedInteger当成一个队列，循环把第一个元素展开，直到第一个元素为数字为止，这样就可以完成迭代

### 题目

#### 1. [扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-341/>

## 最近公共祖先

### 解法

主要思想就是遍历二叉树，同时查找左子树和右子树是否分别含有一个节点，如果是，那么这个结点就是LCA

### 题目

#### 1. [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-236/>

#### 2. [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-235/>

## 最近公共祖先

### 解法

主要思想就是遍历二叉树，同时查找左子树和右子树是否分别含有一个节点，如果是，那么这个结点就是LCA

### 题目

#### 1. [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-236/>

#### 2. [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-235/>

## 完全二叉树的结点个数

### 解法

普通二叉树需要对二叉树进行遍历才能统计结点个数，满二叉树只需要知道树的高度就可以计算出来，那么完全二叉树可以结合这两个的做法，如果左边和右边高度相同，就用满二叉树的计算方式，如果不同那就遍历二叉树，同时判断该节点为root的树是不是满二叉树

这种做法时间复杂度是O(logn*logn)，详见：<https://labuladong.gitee.io/algo/2/21/48/>

### 题目

#### 1. [完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-222/>

# 图

## 图的遍历

### 解法

直接套模板，详见思想章节

### 题目

#### 1. [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)

题解详见：<https://blog.zhangmengyang.tk/posts/leetcode/leetcode-797/>

# 思想

## 双指针

就是两个指针，分为左右指针和快慢指针，只要数组有序，就应该想到双指针技巧

### 左右指针

两个指针一个左一个右

#### 二分查找

就是将搜索空间合理的分成两部分，摒弃不可能的那部分，缩减搜索空间，加快搜索速度

##### 经典思路

```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid -1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        }
    }

    return -1;
}
```

这种就是一边缩减搜索空间，一边寻找要找的元素。

但是有时候问题并不是这么简单，比如寻找一个可能在数组里不存在，或者是找边界这样的问题，这时使用进阶思路 ，在循环体内排除一定不存在目标元素的区间会更简单一些。

经典思路是寻找元素

进阶思路是排除n-1个不可能的元素

##### 进阶思路

```java
class Solution {
    public int search(int[] nums, int target) {
        // 此思路搜索空间为[left, right]，闭闭空间
        int left = 0, right = nums.length - 1;

        // 循环条件写成left<right，因为循环体内把数组分成两部分，那么一定会达到left和right重合的状态
        // 所以循环条件写成left<right，可以保证退出循环时left等于right
        while (left < right) {
            // 求中点，left=mid+1时不需要向上取整
            int mid = left + (right - left) / 2;
            // left=mid时需要向上取整，记忆方式：left和mid要有一个+1
            // 这么做的原因是：向下取整时，如果还剩下两个元素，刚好又走到left=mid这个分支，就死循环了，因为此时mid就等于left
            //int mid = left + (right - left + 1) / 2;
            // 下面是核心逻辑，分成两个区间是因为这样扩展性更强
            // 这块主要就是筛选不可能的区间，然后缩减搜索空间，具体问题具体分析，注意left没加一时mid要加一
            if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
            /*if (target <= nums[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }*/
            /*if (target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid;
            }*/
            /*if (target >= nums[mid]) {
                left = mid;
            } else {
                right = mid -1;
            }*/
        }

        // 此时left一定等于right，所以返回left或者right都一样
        // 排除了n-1个不可能的元素，还剩下[left, right]区间的元素，而left=right，就看剩下这个是不是要寻找的元素了
        // 如果该题一定存在指定的元素，那么下一步可以省略，直接return left就好了
        if (nums[left] == target) {
            return left;
        }

        return -1;
    }
}
```

###### 步骤

1. left和right分别设置为搜索空间的左右端点，注意是闭区间
2. 循环条件写成left<right
3. 求中点，先写成`int mid = left + (right - left) / 2;`
4. 根据具体问题将搜索空间分成两部分，其中一部分必须是不可能的区域，然后根据这个不可能区域的特征写出第一个if，然后else里写和if互补的区域就好了，注意如果结果是left=mid，上面求中点要改成`int mid = left + (right - left + 1) / 2;`
5. 如果根据题意不能判断出一定存在寻找的元素，需要判断下`nums[left]`是不是寻找的元素，是则`return left`，否则未找到该元素；如果根据题意能判断出一定存在寻找的元素，那直接`return left`就好了

###### 注意点

1. 此思路搜索空间为[left, right]，闭闭空间
2. 循环条件写成left<right，因为循环体内把数组分成两部分，并且根据left的取值选择mid是向上或向下取整，那么一定会达到left和right重合的状态（把所有情况都模拟一边就可以得出这个结论），所以循环条件写成left<right，可以保证退出循环时left等于right
3. 求中点时，如果使用`(left + right) / 2`有可能相加溢出，为了防止溢出使用`left + (right - left) / 2`
4. 求中点时，left=mid+1时不需要向下取整，left=mid时需要向上取整，记忆方式：left和mid要有一个+1。这么做的原因是：向下取整时，如果还剩下两个元素，刚好又走到left=mid这个分支，就死循环了，因为此时mid就等于left。right=mid时需要向下取整，原因同理
5. 把搜索空间分成两个区间是因为这样扩展性更强
6. 缩减搜索空间时，将搜索空间分成两部分需要注意分出不可能的区间，然后缩减搜索空间，具体问题具体分析，根据这个不可能区间的特征写出第一个if，然后else里写和if互补的区域
7. 注意left没加一时mid要加一
8. 退出循环后left和right相等，并且是唯一有希望的元素（只是有希望，有可能不是它，还要再判断一下，如果该题一定存在指定的元素，那么直接`return left`就好了）
9. 对于寻找左右侧边界的二分查找，在缩减搜索空间时一定要考虑>=或<=的情况，因为这样才能使用找左或右侧这个性质，比如`target <= nums[mid]`，可以寻找左边界，因为这时左边界不可能在mid右边所以直接`right=mid`就可以找到左边界，右边界同理。为什么找到的是左边界，也可以这么理解：`target <= nums[mid]`->`right=mid`，所以`target > nums[mid]`->`left=mid + 1`，此时left左边全部都小于target，因为退出循环时如果能找到target，left指向的就是target，又因为left左边全部都小于target，所以此时left指向左边界。找右边界同理。
10. 对于寻找左侧边界的二分查找，说是寻找该元素的左侧边界，实际上是寻找大于等于target的所有元素的左侧边界，同理，寻找右侧边界的二分查找实际上是寻找小于等于target的所有元素的右侧边界，也可以理解成左侧边界的左边都小于target，右侧边界的右边都大于target，并且左右边界不一定等于target

详见：leetcode笔记word版和<https://leetcode.cn/leetbook/read/learning-algorithms-with-leetcode/xs41qg/>

#### 其他

见上面各知识点章节

### 快慢指针

两个指针一个快一个慢

#### 滑动窗口

`left` 指针在后，`right` 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

##### 模板

```java
/* 滑动窗口算法模板 */
void slidingWindow(String s) {
   	Map<Character, Integer> window = new HashMap<>();

    int left = 0, right = 0;
    // 这里用<而不用<=不是说明使用的闭闭区间，而是right当前位置的元素是我们下一个要入窗口的元素，所以这里其实是闭开窗口
    while (right < s.length()) {
        // 获取移入窗口的元素，并扩大窗口
        char c = s.charAt(right);
        right++;
        // 进行扩大窗口时数据的一系列更新
        ...
        
        // debug位置
        // System.out.println("left:" + left + "\t" + "right:" + right);

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // 获取移出窗口的元素，并收缩窗口
            char d = s.charAt(left);
            left++;
            // 进行收缩窗口时数据的一系列更新，一般与上面扩大窗口时数据更新相反
        	...
        }
    }
}

```

##### 步骤

1. 设置存储窗口内元素的数据结构，并且设置循环`while (right < s.length())`
2. 扩大窗口，并更新相关的数据
3. 判断是否需要收缩窗口，如需要，则收缩窗口，并更新相关的数据
4. 退出循环后，返回相应的数据

##### 注意点

1. 此模板采用闭开区间，循环条件用<而不用<=是因为right当前位置的元素是我们下一个要入窗口的元素
2. 收缩窗口和扩大窗口对数据的更新一般是相反的（更新顺序和加减等都是相反的）

详见：<https://labuladong.gitee.io/algo/2/20/27/>

##### 进阶

==RABIN KARP 字符匹配算法==，详见：<https://labuladong.gitee.io/algo/2/20/28/>

#### 其他

见上面各知识点章节

## 递归

一个问题 = 规模更小的同类问题 + 扩展成该问题要解决的问题

这种情况就可以用递归，递归的关键是不要跳进递归，而是明确递归函数的定义

递归由两部分组成：递归出口和递归公式

注意递归需要递归出口（也就是base case）

值得一提的是，递归操作链表并不高效。和迭代解法相比，虽然时间复杂度都是 O(N)，但是迭代解法的空间复杂度是 O(1)，而递归解法需要堆栈，空间复杂度是 O(N)。

## 前缀和与差分

前缀和数组的差分是原数组，差分数组的前缀和是原数组，两者互逆。

### 前缀和

对于一个数组，求此数组[left, right]区域内的和时，不需要从left--right逐个相加，直接right+1前的和减去left前的和即可，要想使用这种方式就得有一个前缀和数组，用来存该数组前k个的和。注意也可能是二维数组，稍作修改即可。

**主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和**。

详见：<https://labuladong.gitee.io/algo/2/20/24/>

#### 标准模板

```JAVA
class NumArray {
    int[] preSum;

    public NumArray(int[] nums) {
        preSum = new int[nums.length + 1];

        for (int i = 1; i < preSum.length; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
    }
    
    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }
}
```

### 差分数组

**差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减**

类似前缀和构造的 `preSum` 数组，我们先对 `nums` 数组构造一个 `diff` 差分数组，**`diff[i]` 就是 `nums[i]` 和 `nums[i-1]` 之差**，通过这个 `diff` 差分数组是可以反推出原始数组 `nums` 的，理解：diff[0]就是原数组的第一个元素，其他元素就是比前一个元素高多少

**这样构造差分数组 `diff`，就可以快速进行区间增减的操作**，如果你想对区间 `nums[i..j]` 的元素全部加 3，那么只需要让 `diff[i] += 3`，然后再让 `diff[j+1] -= 3` 即可

**原理很简单，回想 `diff` 数组反推 `nums` 数组的过程，`diff[i] += 3` 意味着给 `nums[i..]` 所有的元素都加了 3，然后 `diff[j+1] -= 3` 又意味着对于 `nums[j+1..]` 所有元素再减 3，那综合起来，就是对 `nums[i..j]` 中的所有元素都加 3 了**

详见：<https://labuladong.gitee.io/algo/2/20/25/>

#### 标准模板

```java
class Difference {
    private int[] diff;

    public Difference(int[] nums) {
        assert nums.length > 0;
        diff = new int[nums.length];

        diff[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            diff[i] = nums[1] - nums[0];
        }
    }

    public void increment(int i, int j, int val) {
        diff[i] += val;
        // 注意这里j有可能是最后一个元素，此时的意思就是i后面的元素全部加val，所以不需要减val了
        if (j + 1 < diff.length) {
            diff[j + 1] -= val;
        }
    }

    public int[] result() {
        int[] res = new int[diff.length];
        res[0] = diff[0];

        for (int i = 1; i < diff.length; i++) {
            res[i] = res[i - 1] + diff[i];
        }
        return res;
    }
}
```

## 二叉树

### 前中后序理解

前中后序是遍历二叉树过程中处理每一个节点的三个特殊时间点：

前序位置的代码在刚刚进入一个二叉树节点的时候执行；

后序位置的代码在将要离开一个二叉树节点的时候执行；

中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。

![img](https://labuladong.gitee.io/algo/images/%e4%ba%8c%e5%8f%89%e6%a0%91%e6%94%b6%e5%ae%98/2.jpeg)

比如快速排序就是个二叉树的前序遍历，归并排序就是个二叉树的后序遍历

### 遍历模板

```java
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
}
```

多叉树的遍历模板：

```java
/* 多叉树遍历框架 */
void traverse(TreeNode root) {
    if (root == null) return;
    // 前序位置
    for (TreeNode child : root.children) {
        traverse(child);
    }
    // 后序位置
}
```

### 做题思路

有两种思路，分别是**分解问题**和**遍历二叉树**

遇到一道二叉树的题目时的通用思考过程是：

1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现。

2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值(这个返回值就是需要用到的子树信息)，这样的话递归函数就会一直分解这个问题，直到该问题不能再分解，所以我们还需要考虑base case(递归出口)。

3、无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

### 后序位置的特殊之处

因为前序位置的代码执行是自顶向下的，而后序位置的代码执行是自底向上的，所以：

前序位置的代码只能从函数参数中获取父节点传递来的数据，而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据。一旦你发现题目和子树有关，那大概率要给函数设置合理的定义和返回值，在后序位置写代码了。

### 层序遍历

就是一个BFS，可以计算一些类似结点与root之间的距离的问题。

#### 模板

```java
// 输入一棵二叉树的根节点，层序遍历这棵二叉树
void levelTraverse(TreeNode root) {
    if (root == null) return;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    // 从上到下遍历二叉树的每一层
    while (!q.isEmpty()) {
        int sz = q.size();
        // 从左到右遍历每一层的每个节点
        for (int i = 0; i < sz; i++) {
            TreeNode cur = q.poll();
            // 将下一层节点放入队列
            if (cur.left != null) {			// 注意不要把null放队列里面
                q.offer(cur.left);
            }
            if (cur.right != null) {		// 注意不要把null放队列里面
                q.offer(cur.right);
            }
        }
    }
}
```

### 注意点

前序中序，后序中序可以唯一确定一颗二叉树，或者带空指针的任意一个遍历序列都可以唯一确定一棵二叉树

前序后序不能唯一确定一颗二叉树，因为：

当节点左右子树都存在时，可以确定左右子树，但是当其中一个为空时，无法确定不为空的子树是左子树还是右子树

### 二叉搜索树

#### 性质

二叉树左边子树全部小于根节点，右边全部大于根节点，中序遍历就是升序序列，并且中序遍历到一个结点时，比该结点小的结点全部都遍历过了，这个性质可以用于二叉搜索树的累加上，二叉搜索树最左边是最小的结点，最右边是最大的结点

#### 合法性

利用二叉树的分解思想，将原问题分解为：root左边的的结点都比root小右边的的结点都比root大+左子树是BST+右子树是BST，问题在于root只能获得左右孩子的值，从而判断是都大于小于root，想要让整个子树都小于或大于自己，需要将min和max传下去，如果当前节点会对下面的子节点有整体影响，可以通过辅助函数增长参数列表，借助参数传递信息。

#### 增删改查

在二叉树递归框架之上，扩展出一套 BST 代码框架：

```java
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
```

根据代码框架掌握了 BST 的增删查改操作。

## 图

### 存储方式

#### 邻接表

优点：省空间

#### 邻接矩阵

优点：可以随机访问

### 遍历模板

和多叉树类似，只不过需要记录访问过的结点

```java
// 记录被遍历过的节点
boolean[] visited;
// 记录从起点到当前节点的路径
boolean[] onPath;

/* 图遍历框架 */
void traverse(Graph graph, int s) {
    if (visited[s]) return;
    // 进入结点时
    // 经过节点 s，标记为已遍历
    visited[s] = true;
    // 做选择：标记节点 s 在路径上
    onPath[s] = true;
    for (int neighbor : graph.neighbors(s)) {
        traverse(graph, neighbor);
    }
    // 离开结点时
    // 撤销选择：节点 s 离开路径
    onPath[s] = false;
}
```

## 回溯

回溯和DFS的区别：

回溯关注的是树枝，DFS关注的是结点，反映到代码上：

```java
// DFS 算法，关注点在节点
void traverse(TreeNode root) {
    if (root == null) return;
    printf("进入节点 %s", root);
    for (TreeNode child : root.children) {
        traverse(child);
    }
    printf("离开节点 %s", root);
}

// 回溯算法，关注点在树枝
void backtrack(TreeNode root) {
    if (root == null) return;
    for (TreeNode child : root.children) {
        // 做选择
        printf("从 %s 到 %s", root, child);
        backtrack(child);
        // 撤销选择
        printf("从 %s 到 %s", child, root);
    }
}
```

# 其他

## 零碎

从整体到细节，自顶向下，从抽象到具体的框架思维是通用的，不只是学习数据结构和算法，学习其他任何知识都是高效的。

数据结构的物理存储方式就是链式和顺序两种，基本操作就是增删改查，遍历方式无非迭代和递归。

计算机算法的本质就是枚举，只不过这里枚举需要做到两个方面：无遗漏和无冗余，有时候还可以利用一些定理进行优化（缩小搜索范围），比如剪枝和数学定理

难点在无遗漏的问题：

难点在无冗余的问题：递归类问题（动态规划）

难点在优化的问题：非递归类问题（并查集，贪心，KMP）

Java里优先队列就是二叉堆，也就是PriorityQueue

base case就是最基本的情况，从递归的角度理解就是递归出口，从分解问题(分治)的角度理解就是最基本的问题（不能再分了）

如果需要通过值找到其在数组的索引，将数组遍历一遍是一种做法，还可以创建一个valToIndex的hashmap

序列化就是把结构化的数据（比如树）打平（比如转换为字符串）

序列化和反序列化的目的：以某种特定格式组织数据，使得数据可以独立于编程语言。

## 待做

https://labuladong.gitee.io/algo/1/3/的那几个算法框架及之后的几个框架文章都没看

https://labuladong.gitee.io/algo/2/21/41/没看

https://labuladong.gitee.io/algo/2/21/45/没看

## 技巧

dummy（虚拟头结点)：可以很好的避免第一个节点的特殊性，将第一个节点当作第二个节点，也即是所有节点统一处理

## 学习方法

以后做题，先想这道题考察什么知识点。


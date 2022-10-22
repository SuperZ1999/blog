---
title: "LeetCode 341"
date: 2022-10-22T21:57:50+08:00
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

#### 思路一

将NestedInteger当成树的节点，list当成该节点的孩子，那么只需要遍历该树就可以完成迭代了，直接看代码

#### 思路二

思路一会在构造的时候将此树遍历一遍，所以速度会很慢，最好弄成懒惰式的，所以可以把NestedInteger当成一个队列，循环把第一个元素展开，直到第一个元素为数字为止，这样就可以完成迭代

### 代码

#### 思路一

```java
public class NestedIterator implements Iterator<Integer> {
    private Iterator<Integer> it;

    public NestedIterator(List<NestedInteger> nestedList) {
        List<Integer> result = new ArrayList<>();
        for (NestedInteger nestedInteger : nestedList) {
            traverse(nestedInteger, result);
        }
        it = result.iterator();
    }

    private void traverse(NestedInteger nestedInteger, List<Integer> result) {
        if (nestedInteger.isInteger()) {
            result.add(nestedInteger.getInteger());
            return;
        }
        List<NestedInteger> list = nestedInteger.getList();
        for (NestedInteger integer : list) {
            traverse(integer, result);
        }
    }

    @Override
    public Integer next() {
        return it.next();
    }

    @Override
    public boolean hasNext() {
        return it.hasNext();
    }
}
```

#### 思路二

```java
public class NestedIterator implements Iterator<Integer> {
    private LinkedList<NestedInteger> nestedList;

    public NestedIterator(List<NestedInteger> nestedList) {
        this.nestedList = new LinkedList<>(nestedList);
    }

    @Override
    public Integer next() {
        return nestedList.remove(0).getInteger();
    }

    @Override
    public boolean hasNext() {
        while (!nestedList.isEmpty() && !nestedList.get(0).isInteger()) {
            List<NestedInteger> first = nestedList.remove(0).getList();
            for (int i = first.size() - 1; i >= 0; i--) {
                nestedList.addFirst(first.get(i));
            }
        }
        return !nestedList.isEmpty();
    }
}
```

### References

---

#### 1. [扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

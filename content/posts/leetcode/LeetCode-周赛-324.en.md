---
title: "LeetCode 周赛-324"
date: 2022-12-18T14:56:08+08:00
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

#### 第一题

暴力解法即可，见代码

#### 第二题

需要知道一个数一定能被分解为质数之积，且是唯一的，分解质数的方法是从2开始除，没法整除就将2加一，再除，直到将原数除成1，这道题需要把数分解同时求和，然后循环这个过程，直到求的和>=上次求的和，那么上次求的和就是答案

#### 第三题

把度数为奇数的节点记到 odd 中，记 m 为 odd 的长度，分类讨论：

- 如果 m=0，那么已经符合要求。
- 如果 m=2，记 x=odd[0],y=odd[1]：
  - 如果 x 和 y 之间没有边，那么连边之后就符合要求了。
  - 如果 x 和 y 之间有边，那么枚举 [1,n] 的所有不为 x 和 y 的点 i，由于 i 的度数一定是偶数，如果 i 和 x 以及 i 和 y 之间没有边，那么连边之后就符合要求了。
- 如果 m=4，记 a=odd[0],b=odd[1],c=odd[2],d=odd[3]：
  - 如果 a 和 b 以及 c 和 d 之间没有边，那么连边之后就符合要求了。
  - 如果 a 和 c 以及 b 和 d 之间没有边，那么连边之后就符合要求了。
  - 如果 a 和 d 以及 b 和 c 之间没有边，那么连边之后就符合要求了。
- 其余情况无法满足要求。

#### 第四题

设 LCA 为 a 和 b 的最近公共祖先，那么环长等于 LCA 到 a 的距离加 LCA 到 b 的距离加一。怎么求LCA？可以这样：

不断循环，每次循环比较 a 和 b 的大小：

- 如果 a>b，则 a 的深度大于等于 b 的深度，那么把 a 移动到其父节点，即 a=a/2；
- 如果 a<b，则 a 的深度小于等于 b 的深度，那么把 b 移动到其父节点，即 b=b/2；
- 如果 a=b，则找到了 LCA ，退出循环。

循环次数加一即为环长。

我的这种做法不够优雅

### 代码

#### 第一题

```java
class Solution {
    private boolean isSimilar(String word1, String word2) {
        HashSet<Character> set1 = new HashSet<>();
        HashSet<Character> set2 = new HashSet<>();
        for (int i = 0; i < word1.length(); i++) {
            set1.add(word1.charAt(i));
        }
        for (int i = 0; i < word2.length(); i++) {
            set2.add(word2.charAt(i));
        }
        if (set1.size() != set2.size()) {
            return false;
        }
        for (Character character : set2) {
            if (!set1.contains(character)) {
                return false;
            }
        }
        return true;
    }

    public int similarPairs(String[] words) {
        int n = words.length, res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isSimilar(words[i], words[j])) {
                    res++;
                }
            }
        }
        return res;
    }
}
```

#### 第二题

```java
class Solution {
    public int smallestValue(int n) {
        int i = 2, res = 0, preRes = Integer.MAX_VALUE;
        while (i <= n) {
            if (n % i == 0) {
                n /= i;
                res += i;
                if (n == 1) {
                    if (preRes <= res) {
                        return preRes;
                    }
                    n = res;
                    preRes = res;
                    i = 2;
                    res = 0;
                }
            } else {
                i++;
            }
        }
        return res;
    }
}
```

#### 第三题

```java
class Solution {
    private Set<String> edgeSet = new HashSet<>();

    public boolean isPossible(int n, List<List<Integer>> edges) {
        int[] degree = new int[n + 1];
        for (List<Integer> edge : edges) {
            edgeSet.add(edge.get(0) + "," + edge.get(1));
            edgeSet.add(edge.get(1) + "," + edge.get(0));
            degree[edge.get(0)]++;
            degree[edge.get(1)]++;
        }
        ArrayList<Integer> nodes = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (degree[i] % 2 == 1) {
                nodes.add(i);
            }
        }
        int count = nodes.size();
        if (count == 0) {
            return true;
        }
        if (count == 2) {
            if (!edgeSet.contains(nodes.get(0) + "," + nodes.get(1))) {
                return true;
            }
            for (int i = 1; i <= n; i++) {
                if (i == nodes.get(0) || i == nodes.get(1)) {
                    continue;
                }
                if (!edgeSet.contains(nodes.get(0) + "," + i) && !edgeSet.contains(i + "," + nodes.get(1))) {
                    return true;
                }
            }
        }
        if (count == 4) {
            if (!edgeSet.contains(nodes.get(0) + "," + nodes.get(1)) && !edgeSet.contains(nodes.get(2) + "," + nodes.get(3))
            || !edgeSet.contains(nodes.get(0) + "," + nodes.get(2)) && !edgeSet.contains(nodes.get(1) + "," + nodes.get(3))
            || !edgeSet.contains(nodes.get(0) + "," + nodes.get(3)) && !edgeSet.contains(nodes.get(1) + "," + nodes.get(2))) {
                return true;
            }
        }
        return false;
    }
}
```

#### 第四题

```java
class Solution {
    private int getLen(int node1, int node2) {
        int len1 = 0, len2 = 0, n1 = node1, n2 = node2;
        while (n1 != 1) {
            n1 /= 2;
            len1++;
        }
        while (n2 != 1) {
            n2 /= 2;
            len2++;
        }
        n1 = node1;
        n2 = node2;
        int l1 = len1;
        int l2 = len2;
        while (n1 != n2) {
            if (l1 > l2) {
                n1 /= 2;
                l1--;
            } else if (l1 < l2) {
                n2 /= 2;
                l2--;
            } else {
                n1 /= 2;
                n2 /= 2;
                l1--;
                l2--;
            }
        }
        return len1 - l1 + len2 - l2 + 1;
    }

    public int[] cycleLengthQueries(int n, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            answer[i] = getLen(queries[i][0], queries[i][1]);
        }
        return answer;
    }
}
```

### References

---


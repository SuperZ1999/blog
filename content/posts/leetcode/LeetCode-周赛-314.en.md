---
title: "LeetCode 周赛 314"
date: 2022-10-09T14:17:29+08:00
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

考察差分数组和模拟，差分之后数组的每个元素就是该任务所用的时间，找最大的即可

#### 第二题

考察差分数组和异或的性质

由a^b=c ---> a^a^b=a^c ---> 0^b=a^c ---> b=a^c，因为相同的数异或为0，任何数异或0都不变

给你的数组相当于是前缀和数组，前缀和数组的差分既是原数组，知道了异或的结果，求异或前的值，用上述推断，然后遍历数组逐个异或即可

#### 第三题

考察贪心和栈

哪里贪心了？答：因为题目要求给出字典序最小的字符串，也就是需要尽量把最小的字母放在前面，那么可以比较栈顶和没入栈的那些字母，看下没入栈的那些字母是否有比栈顶小的字母，如果没有，那直接出栈，如果有，那就入栈直到遇到最小的字符串，这样贪心，最后的结果一定是字典序最小的字符串。

#### 第四题

考察动态规划

非常典型的动态规划，唯一要注意的就是动态规划数组里的元素不能是所有路径长度的list，因为逐个遍历list的元素会超时，需要使用map，key为路径长度，value为长度为key的路径的个数，还需要注意value有可能很大，需要取余1000000007，key有可能很多，所以需要取余k，因为最终只需要长度能整除k的路径个数，而不需要具体的路径长度。

#### 总结

本次周赛难度偏低，但是我刷题太少，做起来不熟练，需要多练习多总结。

### 我的代码

#### 第一题

```java
class Solution {
    public int hardestWorker(int n, int[][] logs) {
        int[] time = new int[logs.length];
        int id = logs[0][0], maxTime = logs[0][1];
        time[0] = logs[0][1];
        for (int i = 1; i < time.length; i++) {
            time[i] = logs[i][1] - logs[i - 1][1];
            if (time[i] > maxTime || time[i] == maxTime && id > logs[i][0]) {
                maxTime = time[i];
                id = logs[i][0];
            }
        }
        return id;
    }
}
```

#### 第二题

```java
class Solution {
    public int[] findArray(int[] pref) {
        for (int i = pref.length - 1; i > 0; i--) {
            pref[i] = pref[i] ^ pref[i - 1];
        }
        return pref;
    }
}
```

#### 第三题

```java
class Solution {
    private boolean hasSmaller(int[] count, int i) {
        for (int j = 0; j < i; j++) {
            if (count[j] != 0) {
                return true;
            }
        }
        return false;
    }

    public String robotWithString(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        StringBuilder ans = new StringBuilder();
        Deque<Character> stack = new ArrayDeque<>();
        stack.push((char) ('z' + 1));
        int index = 0;
        while (ans.length() != s.length()) {
            Character peek = stack.peek();
            if (hasSmaller(count, peek - 'a')) {
                stack.push(s.charAt(index));
                count[s.charAt(index) - 'a']--;
                index++;
            } else {
                ans.append(peek);
                stack.pop();
            }
        }
        return ans.toString();
    }
}
```

#### 第四题

```java
class Solution {
    public int numberOfPaths(int[][] grid, int k) {
        Map<Integer, Integer>[] path = new HashMap[grid[0].length];
        path[0] = new HashMap<>();
        path[0].put(grid[0][0] % k, 1);
        for (int i = 1; i < grid[0].length; i++) {
            path[i] = new HashMap<>();
            for (Integer integer : path[i - 1].keySet()) {
                path[i].put((integer + grid[0][i]) % k, 1);
            }
        }
        for (int i = 1; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                HashMap<Integer, Integer> temp = new HashMap<>(path[j]);
                path[j].clear();
                for (Map.Entry<Integer, Integer> entry : temp.entrySet()) {
                    path[j].put((entry.getKey() + grid[i][j]) % k, entry.getValue());
                }
                if (j != 0) {
                    for (Map.Entry<Integer, Integer> entry : path[j - 1].entrySet()) {
                        int newKey = (entry.getKey() + grid[i][j]) % k;
                        path[j].put(newKey, (path[j].getOrDefault(newKey, 0) + entry.getValue()) % 1000000007);
                    }
                }
            }
        }
        return path[path.length - 1].getOrDefault(0, 0);
    }
}
```

### References

---

#### 1. [处理用时最长的那个任务的员工](https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task/)

#### 2. [找出前缀异或的原始数组](https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/)

#### 3. [使用机器人打印字典序最小的字符串](https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/)

#### 4. [矩阵中和能被 K 整除的路径](https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)

---
title: "LeetCode 32"
date: 2023-01-06T22:54:56+08:00
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

三种思路：

#### 栈

定义一个栈，保证栈底为最后一个不匹配的右括号的下标，然后碰到左括号就入栈，碰到右括号就出栈，如果出栈后栈为空，说明当前的右括号没有相对应的左括号，那么此右括号就是最后一个不匹配的右括号，将其下标入栈，如果出栈后栈不为空，说明有相应的左括号，那么更新res最大值即可，为什么这样是正确的呢？因为栈里存的是最后一个不匹配的右括号和尚未匹配的左括号，任何一个有效括号序列一定是以这些元素开头，所以可以通过这种方式获取有效括号序列的长度

#### 动态规划

构建dp数组，数组里存放以该元素结尾的最长有效括号，状态转移方程为：

```java
if (s.charAt(i) == '(') {
    dp[i] = 0;
} else {
    if (s.charAt(i - 1) == '(') {
        dp[i] = i - 2 >= 0 ? dp[i - 2] + 2 : 2;
    } else {
        if (i - dp[i - 1] - 1 >= 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
            dp[i] = dp[i - 1] + 2 + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0);
        } else {
            dp[i] = 0;
        }
    }
}
```

当该元素为右括号，前面元素也是右括号时，先根据前面元素的有效括号长度找到有可能与该元素匹配的左括号，如果`i - dp[i - 1] - 1`位置的元素是左括号，那么就匹配上了`dp[i] = dp[i - 1] + 2 + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0);`，如果`i - dp[i - 1] - 1`位置的元素是右括号，则该元素的最长有效括号为0，生成dp数组元素的同时维护大值即可

base case为`dp[-1] = dp[0] = 0`，不能优化空间复杂度

#### 两次遍历

从左往右遍历一次，统计碰到的左括号的数量（left）和右括号的数量（right），如果left == right就记录长度，如果right>left，就让left和right归零，因为此时前面的元素都可以扔掉不考虑，但是这种情况无法判断(()这种情况，此时从右往左遍历一遍就可以了，如果right<left，就让left和right归零，遍历的同时维护最大值即可

### 代码

#### 栈

```java
class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length(), res = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(-1);
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    res = Math.max(res, i - stack.peek());
                }
            }
        }
        return res;
    }
}
```

#### 动态规划

```java
class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length(), res = 0;
        int[] dp = new int[n];
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == '(') {
                dp[i] = 0;
            } else {
                if (s.charAt(i - 1) == '(') {
                    dp[i] = i - 2 >= 0 ? dp[i - 2] + 2 : 2;
                } else {
                    if (i - dp[i - 1] - 1 >= 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
                        dp[i] = dp[i - 1] + 2 + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0);
                    } else {
                        dp[i] = 0;
                    }
                }
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

#### 两次遍历

```java
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0, res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                res = Math.max(res, left + right);
            } else if (left < right) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                res = Math.max(res, left + right);
            } else if (left > right) {
                left = right = 0;
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/)

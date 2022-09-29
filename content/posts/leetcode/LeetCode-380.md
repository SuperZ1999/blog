---
title: "LeetCode 380"
date: 2022-09-27T14:35:51+08:00
tags: ["leetcode"]
draft: false
---

### 思路

为了随机选取元素，需要用到数组，并且得是紧凑的，但是数组增删不是O(1)的，所以再来个map，key是数组元素的值，value是数组的索引，这样就做到了O(1)的数组增删，增删的时候注意修改map和数组

### 我的代码

```java
class RandomizedSet {
    private List<Integer> nums;
    private Map<Integer, Integer> valToIndex;

    public RandomizedSet() {
        nums = new ArrayList<>();
        valToIndex = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (valToIndex.containsKey(val)) {
            return false;
        }

        valToIndex.put(val, nums.size());
        nums.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!valToIndex.containsKey(val)) {
            return false;
        }

        int index = valToIndex.get(val);
        int lastNum = nums.get(nums.size() - 1);
        valToIndex.put(lastNum, index);
        valToIndex.remove(val);
        nums.set(index, lastNum);
        nums.remove(nums.size() - 1);
        return true;
    }
    
    public int getRandom() {
        return nums.get(new Random().nextInt(nums.size()));
    }
}
```

### References

---

#### 1. [O(1) 时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)

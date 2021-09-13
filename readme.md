# 91算法 

* DAY1
[989. Add to Array-Form of Integer](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
#### thought：brutal way： traverse list->str->int->list python is fine with this but in other language will cause an overflow because the length of the list is super long

the brutal way
[989 file](https://github.com/Lllouiselao/Leetcode/blob/master/Array/989_Add_To_Array.py)
#### complexcity O(n^2) 

#### 优化想法：

***

* DAY3
[1381. Design a Stack With Increment Operation](https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/)
#### 想法：设计一个栈 用list的方式来实现 
```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack_len = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack_len < self.maxSize:
            self.stack.append(x)
            self.stack_len +=1

    def pop(self) -> int:
        if self.stack_len == 0:
            return -1
        else:
            self.stack_len -= 1
            item = self.stack[self.stack_len]
            del self.stack[self.stack_len]
            return item

    def increment(self, k: int, val: int) -> None:
        for i in range(self.stack_len):
            if i < k:
                self.stack[i] = self.stack[i] + val
            else:
                return
```
#### complexcity pop:O(1) Push:O(1) increment:O(min(k, stack_len))


***
* DAY4
[394. Decode String](https://leetcode-cn.com/problems/decode-string/)
#### thoughts: think about -> [20. Valid Parentheses](https://leetcode-cn.com/problems/valid-parentheses/) but didn't know how to get touch on this, still didn't familiar with how stack work
```python
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []  
        num_val = 0
        result = ""  
        for ele in s:
            if ele.isdigit():
                num_val = num_val * 10 + int(ele)
            elif ele == "[":
                num_stack.append([result, num_val])
                result, num_val = "", 0
            elif ele == "]":
                top = num_stack.pop()
                result = top[0] + result * top[1]
            else:
                result += ele
        return result
```
#### Complexcity O(n)

[989. Add to Array-Form of Integer](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
# 91算法 DAY1
#### 想法：最brutal way： traverse list->str->int->list 
the brutal way
```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_turple = ''
        for i in num:
            str_turple += str(i)

        str_int = int(str_turple) + k
        int_str = str(str_int)

        output = []
        for n in int_str:
            output.append(int(n))
        return output
```
#### complexcity O(n^2) 
[989 file](https://github.com/Lllouiselao/Leetcode/blob/master/Array/989_Add_To_Array.py)

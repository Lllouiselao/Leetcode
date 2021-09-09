[989. Add to Array-Form of Integer](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
#### 想法：traverse list->str->int->list 
the brutal way
```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_turple = ''
        for i in num:
            str_turple += str(i)

        int_str = int(str_turple) + k
        int_str2 = str(int_str)

        output = []
        for n in int_str2:
            output.append(int(n))
        return output
```
#### complexcity O(n^2) 
[989 file](https://github.com/Lllouiselao/Leetcode/blob/master/Array/989_Add_To_Array.py)

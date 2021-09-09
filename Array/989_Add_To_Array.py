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

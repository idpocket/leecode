'''


给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''





class Solution:
    def isValid(self, s: str) -> bool:

        l = len(s)
        if len(s)%2!=2:
            return False
        for i in range(l/2):
            if s[l-1-i] ==s[l+i-1]:






if __name__ == '__main__':
    solution = Solution()

    p = solution.isValid('()[]{}')
    # print(p)
    {{()}}{}({})

    []{}{}








'''

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。



输入：x = 121
输出：true

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。



'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)%2
        ll = int(len(x)/2)
        if x[0]=='-':
            return False
        if l==0:
            for i in range(ll):
                if x[ll-i-1]!=x[ll+i]:
                    return False
            return True
        if l!=0:
            for i in range(ll):
                if x[ll-i-1]!=x[ll+i+1]:
                    return False
            return True

    def isPalindrome2(self, x: int) -> bool:
        l = int(len(str(x))/2)
        if str(x)[0]=='-':
            return False
        for i in range(l):
            if str(x)[i] != str(x)[-1+(-i)]:
                return False
        return True



if __name__ == '__main__':
    solution=Solution()
    x=1001
    re = solution.isPalindrome2(x=x)
    print(re)



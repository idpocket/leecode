




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        on = False
        sum =0;
        for x in s:

            if x !=' ':
                on=True
            if on==True:

                if x ==' ':
                    return sum
                sum+=1
        return sum

    def lengthOfLastWord2(self, s: str) -> int:

        s = s[::-1]
        s=s.split(' ')
        return len(s[-1])



if __name__ == '__main__':



    # s.split()
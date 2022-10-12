class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        i, j = 0, len(palindrome) - 1
        palindrome_list = list(palindrome)
        while i < j:
            if palindrome[i] != "a":
                palindrome_list[i] = "a"
                return "".join(palindrome_list)
            i+=1
            j-=1
        palindrome_list[-1] = "b"
        return "".join(palindrome_list)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def backtrack(first, last, count):
            if last > len(s):
                if count == len(s):
                    res.append(subset.copy())
                return

            curr_word = s[first:last]

            if is_palindrome(curr_word):
                subset.append(curr_word)
                backtrack(last, last + 1, count + last - first)
                subset.pop()
            
            backtrack(first, last + 1, count)


        def is_palindrome(word):
            l, r = 0, len(word) - 1

            while r > l:
                if word[r] == word[l]:
                    r -= 1
                    l += 1
                else:
                    return False

            return True

        backtrack(0, 1, 0)

        return res
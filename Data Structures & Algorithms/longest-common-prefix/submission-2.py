class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        base = strs[0]
        max_j = min(len(s) for s in strs)  # bound by shortest string
        result_chars = []

        for i in range(max_j):
            ch = base[i]
            for word in strs[1:]:
                if word[i] != ch:
                    return "".join(result_chars)
            result_chars.append(ch)

        return "".join(result_chars)

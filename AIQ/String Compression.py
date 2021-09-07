class Solution:
    def compress(self, chars: List[str]) -> int:
        sum_ = 1
        n = len(chars)
        for i in range(n - 1):
            if chars[i] == chars[i + 1]:
                sum_ += 1
            else:
                if sum_ > 1:
                    chars.append(chars[i])
                    if sum_ >= 10:
                        strSum = [char for char in str(sum_)]
                        for i in range(len(strSum)):
                            chars.append(strSum[i])
                    else:
                        chars.append(str(sum_))
                else:
                    chars.append(chars[i])
                sum_ = 1
        if sum_ > 1:
            chars.append(chars[n - 1])
            if sum_ >= 10:
                strSum = [char for char in str(sum_)]
                for i in range(len(strSum)):
                    chars.append(strSum[i])
            else:
                chars.append(str(sum_))
        else:
            chars.append(chars[n - 1])
        del chars[:n]
        return len(chars)
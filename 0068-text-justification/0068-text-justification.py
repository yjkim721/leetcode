class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        start_idx = 0
        width = 0
        for idx, word in enumerate(words):
            print(width, ret, word)
            if width == 0:
                width += len(word)
            else:
                width += len(word) + 1
            if width > maxWidth:
                elem = " ".join(words[start_idx:idx])
                ret.append(elem)
                start_idx = idx
                width = len(words[idx])
            if idx == len(words) - 1:
                elem = " ".join(words[start_idx:])
                ret.append(elem)
        print(ret)
        for i, r in enumerate(ret):
            n_spaces = maxWidth - len(r)
            if i == len(ret) - 1:
                ret[i] = r + n_spaces * " "
            else:
                words = r.split(" ")
                if len(words) == 1:
                    ret[i] = r + n_spaces * " "
                else:
                    word_spaces = [""] * (len(words) - 1)
                    idx = 0
                    for _ in range(n_spaces + len(words) - 1):
                        word_spaces[idx] = word_spaces[idx] + " "
                        idx += 1
                        if idx == len(word_spaces):
                            idx = 0
                    word_spaces += [""]
                    final = []
                    for w_i in range(len(words)):
                        final.append(words[w_i])
                        final.append(word_spaces[w_i])
                    ret[i] = "".join(final)
        return ret

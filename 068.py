class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        lines = []
        n = len(words)
        while i < n:
            current = []
            current_index = 0
            should_append = True
            while True:
                if i == n :
                    # should_append = False
                    break
                elif len(current) == 0 and len(words[i]) <= maxWidth:
                    current_index += len(words[i])
                    current.append(words[i])
                    i += 1
                elif current_index + len(words[i]) + 1 <= maxWidth:
                    current_index += len(words[i]) + 1
                    current.append(words[i])
                    i += 1
                else:
                    break
            if should_append:
                lines.append(current)
        print(lines)
        to_return = []
        # all but last line
        for line in lines[:-1]:
            return_line = ""
            whitespace_to_fill = maxWidth - sum(len(word) for word in line)
            num_words = len(line)
            if num_words == 1:
                return_line += line[0] + whitespace_to_fill * " "
            else:
                counter = 0
                while counter < whitespace_to_fill:
                    print(counter)
                    index = (counter) % (num_words - 1)
                    line[index + 1] = " " + line[index + 1]
                    counter += 1
                for word in line:
                    return_line += word
            to_return.append(return_line)
        # final line
        final_line = ""
        for word in lines[-1][:-1]:
            final_line += word + " "
        final_line += lines[-1][-1]
        final_line += (maxWidth - len(final_line)) * " " # final whitespace
        to_return.append(final_line)
        return to_return

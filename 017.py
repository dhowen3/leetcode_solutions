class Solution(object):
    d = {1:"", 2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz",0:""}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_digits = len(digits)
        to_return = [""]
        i = 0
        while(i < num_digits):
            current_digit = digits[i]
            current_letters = self.d[int(current_digit)]
            new_list = []
            for entry in to_return:
                for letter in current_letters:
                    new_list.append("%s%s" % (entry, letter)) 
            to_return = new_list
            i += 1
        if len(to_return) == 1 and to_return[0] == "":
            return []
        else:
            return to_return
        

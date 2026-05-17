class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {
            '(': ')', 
            '{': '}', 
            '[' : ']'
        }
        stack = []

        for bracket in s:
            if bracket in brackets_dict:
                stack.append(brackets_dict[bracket])
            else:
                dict_pop = stack.pop() if stack else None
                if bracket != dict_pop:
                    return False
        
        if stack:
            return False
        
        return True
        
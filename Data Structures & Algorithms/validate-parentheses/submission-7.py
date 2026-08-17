class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets_dict = {
            "(" : ")",
            "[" : "]",
            "{": "}"
        }

        for bracket in s:
            if bracket in brackets_dict:
                stack.append(brackets_dict[bracket])
            else:
                last_pop = stack.pop() if stack else None
                if bracket != last_pop:
                    return False
        
        if stack:
            return False
        
        return True

        
       
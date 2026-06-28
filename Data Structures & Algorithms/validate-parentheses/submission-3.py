class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            else:
                last_bracket = stack.pop() if stack else None
            
                if bracket != last_bracket:
                    return False
        
        if stack:
            return False
        
        return True
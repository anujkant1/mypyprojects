'''
Write a function that takes a string of text and returns True if the parentheses are balanced and False otherwise.
For example, the function should return True for the following strings:
    (if (zero? x) max (/ 1 x))
    I told him (that it’s not (yet) done). (But he wasn’t listening)
And False for these:
    :-)
    ())(
'''


def balanced_parantheses(user_input : str) -> bool:
    try:
        if not isinstance(user_input, str):
                raise TypeError("Input must be a string")
        
        stack = []			
        matching_parantheses = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for char in user_input:
            if char in matching_parantheses.keys():
                stack.append(char)
            elif char in matching_parantheses.values():
                if not stack or matching_parantheses[stack.pop()] != char:
                    return False
            elif char not in matching_parantheses.keys() and char not in matching_parantheses.values():
                continue

        return len(stack) == 0


    except Exception as e:
        print(f"An error occurred, {e}")
        return False


print(balanced_parantheses("(if (zero? x) max (/ 1 x))"))
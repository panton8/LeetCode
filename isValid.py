def isValid(s: str) -> bool:
    stack = [s[0]]
    open_ch = {'(', '[', '{'}
    for i in range(1,len(s)):
        if s[i] in open_ch:
            stack.append(s[i])
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
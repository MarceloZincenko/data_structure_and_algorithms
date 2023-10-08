#71. Simplify Path
def simplifyPath(path: str) -> str:
    """
    a = '/home//foo/'
    b = a.split('/')
    print(b)
    ['', 'home', '', 'foo', '']"""

    stack = []

    for i in path.split("/"):
        #  if i == "/" or i == '//', it becomes '' (empty string)

        if i == "..":
            if stack:
                stack.pop()
        elif i == "." or i == '':
            # skip "." or an empty string
            continue
        else:
            stack.append(i)

    res = "/" + "/".join(stack)
    return res
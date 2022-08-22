def repeatedCharacter(s: str) -> str:
    rep = set()

    for i in range(len(s)):
        if s[i] in rep:
            return s[i]
        rep.add(s[i])

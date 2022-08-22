def canConstruct(ransomNote: str, magazine: str) -> bool:
    count = 0
    for i in range(len(ransomNote)):
        if (count == len(ransomNote)):
            return True
        for j in range(len(magazine)):
            if ransomNote[i] == magazine[j]:
                count += 1
                magazine = magazine[:j] + magazine[j + 1:]
                break
    if count == len(ransomNote):
        return True
    return False

def capitalizeTitle(title: str) -> str:
    title = title.lower()
    symbols_count = 0

    for i in range(len(title)):
        if title[i] != ' ':
            symbols_count += 1
        if title[i] == ' ' or i == len(title) - 1:
            if symbols_count > 2 and i == len(title) - 1:
                old = title[i - symbols_count + 1:i+1]
                new = title[i - symbols_count + 1].upper() + title[i - symbols_count + 2: i+1]
                title = title.replace(old, new)
                continue
            if symbols_count > 2:
                old = title[i - symbols_count:i]
                new = title[i - symbols_count].upper() + title[i - symbols_count + 1: i]
                title = title.replace(old, new)
            symbols_count = 0

    return title

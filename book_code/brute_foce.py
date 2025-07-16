def text_match(txt, pattern):
    txt_cursor = 0
    pattern_cursor = 0

    while txt_cursor != len(txt) and pattern != len(pattern):
        if txt[txt_cursor] == pattern[pattern_cursor]:
            txt_cursor += 1
            pattern_cursor += 1
        else:
            txt_cursor = txt_cursor - pattern_cursor + 1
            pattern_cursor = 0

    return txt_cursor - pattern_cursor if pattern_cursor == len(pattern) else -1



txt = input()
pattern = input()

index = text_match(txt, pattern)

print(txt[index])




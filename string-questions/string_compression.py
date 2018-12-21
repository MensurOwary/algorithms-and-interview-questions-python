"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compress(st):
    cur = st[0]
    count = 0
    string_so_far = ''
    for ch in st:
        if cur == ch:
            count += 1
        else:
            string_so_far = string_so_far + cur + str(count)
            count = 1
            cur = ch
    string_so_far = string_so_far + cur + str(count)
    return string_so_far if len(string_so_far) < len(st) else st
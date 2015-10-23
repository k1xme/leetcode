
def shortest(s, p):
    rst = len(s)
    
    letter_count = {}
    for c in p:
        if c not in letter_count:
            letter_count[c] = 1
        else: letter_count[c] += 1

    cur_s = 0
    substart = 0
    letter_found = {c: 0 for c in p}
    found = 0
    while cur_s < len(s):
        if found < len(p):
            if s[cur_s] in letter_found:
                letter_found[s[cur_s]] += 1
                if letter_found[s[cur_s]] == letter_count[s[cur_s]]: found += 1
        else:
            while found == len(p) and substart < cur_s:
                rst = min(rst, cur_s-substart)
                c = s[substart]            
                if c in letter_found:
                    letter_found[c] -= 1
                if letter_found[c] == 0: found -= 1
                substart += 1

        cur_s += 1

    print rst
            


shortest('abxxxaxb', 'axb')



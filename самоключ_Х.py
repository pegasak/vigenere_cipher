def num(word):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for i in word:
        for ex in range(len(a)):
            if i == a[ex]:
                result.append(ex)
    return result

def into_word(num):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    result = []
    for i in num:
        result.append(a[i])
    return result

def encrypt(word, key):
    word_num = num(word)
    key_num = num(key)
    gam = []
    gam.append((key_num[0] + word_num[0]) % 26)
    a = 0
    j = 0
    for i in range(len(word_num) - 1):
        a = gam[j] + word_num[i+1]
        gam.append(a % 26)
        a = 0
        j += 1
    wer = [(x + y) % 26 for x, y in zip(word_num, gam)]
    result = into_word(wer)
    return ''.join(result)

def decrypt(dec_word, key):
    dec_word_num = num(dec_word)
    key_num = num(key)
    gam = [11, 25, 17, 19, 7, 3]
    wer = [(x - y) % 26 for x, y in zip(dec_word_num, gam)]
    result = into_word(wer)
    return ''.join(result)

print("Зашифрованное слово: ", encrypt("moscow", "z"))
print("Расшифрованный тест: ", decrypt("xnjvvz", "z"))
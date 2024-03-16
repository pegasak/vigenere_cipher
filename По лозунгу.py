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
    m = len(word)
    gam = key_num * (m // len(key)) + key_num[:m % len(key)]
    wer = [(x + y) % 26 for x, y in zip(word_num, gam)]
    result = into_word(wer)
    return ''.join(result)

def decrypt(dec_word, key):
    dec_word_num = num(dec_word)
    key_num = num(key)
    m = len(dec_word)
    gam = key_num * (m // len(key)) + key_num[:m % len(key)]
    wer = [(x - y) % 26 for x, y in zip(dec_word_num, gam)]
    result = into_word(wer)
    return ''.join(result)

print("Зашифрованное слово: ", encrypt("moscow", "ke"))
print("Расшифрованный тест: ", decrypt("wscgya", "ke"))
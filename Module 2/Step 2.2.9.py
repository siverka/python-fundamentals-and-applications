from simplecrypt import decrypt, DecryptionException

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

    with open('passwords.txt') as passwords:
        i = 0
        for password in passwords:
            print(i)
            try:
                answer = decrypt(password.strip(), encrypted)
            except DecryptionException:
                pass
            else:
                print(answer.decode('utf'))
                break
            i += 1

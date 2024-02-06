f = open('ntds.txt', 'r').readlines()
hashs = []

print('\n====    USERS AND HASHS    ====\n')
for i in range(len(f)):
    user = f[i].split(':')[0].split('\\')
    hash = f[i].split(':')[3]

    hashs.append(hash)

    if len(user) == 2 and '$' not in user[1]:
        print(f"{user[1]}:{hash}")

print('\n====    DUPLICATE HASHS    ====\n')
for hash in set(hashs):
    if hashs.count(hash) > 1:
        print({hash:hashs.count(hash)})

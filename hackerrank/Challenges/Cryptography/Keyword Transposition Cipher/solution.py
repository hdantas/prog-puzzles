def solve(pwd, ciphertext):
	pwd_unique = []
	[pwd_unique.append(c) for c in pwd if c not in pwd_unique]
	pwd_unique_sorted = sorted(pwd_unique)

	complete_alphabet = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
	alphabet = [chr(c) for c in range(ord('A'), ord('Z') + 1) if chr(c) not in pwd_unique]
	cipher = pwd_unique + alphabet

	key = ['.'] * 26
	j = 0
	for i in range(len(pwd_unique)):
		index = cipher.index(pwd_unique_sorted[i])
		for newindex in range(index, 26, len(pwd_unique)):
			c = chr(ord('A') + j)
			newc = cipher[newindex]
			key[ord(newc) - ord('A')] = c
			# print "%s -> %s" % (c, newc)
			j = j + 1
		i = i + 1


	plaintext = ""
	for c in ciphertext:
		if c == ' ':
			plaintext += ' '
		else:
			plaintext += key[ord(c) - ord('A')]
	print plaintext


testcases = int(raw_input())
pwd_list = []
ciphertext_list = []
for i in range(testcases):
	pwd_list.append(raw_input())
	ciphertext_list.append(raw_input())

for i in range(testcases):
	solve(pwd_list[i],ciphertext_list[i])
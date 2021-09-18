# wapp to read two strings and find if they are anagrams
# strings having same letters but different meanings
# listen <--> slient	fried <--> fired	earth <--> heart
# elinst <--> elinst 
# race <--> care  elbow <--> below

s1 = input(" enter first string ")
d1 = sorted(s1)
ns1 = "".join(d1)

s2 = input(" enter second string ")
d2 = sorted(s2)
ns2 = "".join(d2)

if ns1 == ns2:
	print(" yes it is an anagram")
else:
	print("nopes its not an anagram ")

# DRY --> dont repeat yourself

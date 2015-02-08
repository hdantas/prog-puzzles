# How to apply
# Find an 8 letter string of characters that contains only letters from acdegilmnoprstuw such that the hash(the_string) is 25180466553932
# if hash is defined by the following pseudo-code:

# Int64 hash (String s) {
#   Int64 h = 7
#   String letters = "acdegilmnoprstuw"
#   for(Int32 i = 0; i < s.length; i++) {
#       h = (h * 37 + letters.indexOf(s[i]))
#   }
#   return h
# }
# For example, if we were trying to find the 7 letter string where hash(the_string) was 680131659347, the answer would be "leepadg".)

def hash(s):
    h = 7
    letters = "acdegilmnoprstuw"
    for c in s:
        h = h * 37 + letters.index(c)
    
    return h

def dehash(hash_value, n):
    letters = "acdegilmnoprstuw"
    result = ""
    
    rhs = hash_value - 7 * 37**n
    for i in range(1, n + 1):
        index = rhs / (37**(n - i))
        result += letters[index]
        rhs -= index * 37**(n - i)

    return result

print dehash(hash("leepadg"), 7) == "leepadg"
print dehash(hash("lollipop"), 8) == "lollipop"


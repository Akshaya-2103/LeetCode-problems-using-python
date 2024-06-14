'''Given a string s consisting of words and spaces, return the length of the last word 
in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.'''

s = "   fly me   to   the moon  "
ans=""
s = s.rstrip()
n = len(s)
print(s)
for i in reversed(range(n)):
    '''if s[:-1] == " ":
        s = s.rstrip()
        print(s)
    else:'''
    if s[i] != " ":
            ans += s[i]
    else:
            break
print(ans)
print(len(ans))
"""
I wrote a crawler that visits web pages, stores a few keywords in a database, 
and follows links to other web pages. I noticed that my crawler was wasting a 
lot of time visiting the same pages over and over, so I made set visited where 
I'm storing URLs I've already visited. Now the crawler only visits a URL if it 
hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' 
basement (where I totally don't live anymore), and it keeps running out of 
memory because visited is getting so huge.

How can I trim down the amount of space taken up by visited?
"""

# Solution 1: 
# Use a bloom filter (hash map that returns 'probably' or 'no')

# Solution 2: 
# Use a trie (tree with nodes length one character, pointer to next character)

# We can use a trie. If you've never heard of a trie, think of it this way:

# Let's make visited a nested dictionary where each map has keys of just one character. So we would store 'google.com' as visited['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']['*'] = True.

# The '*' at the end means 'this is the end of an entry'. Otherwise we wouldn't know what parts of visited are real URLs and which parts are just prefixes. In the example above, 'google.co' is a prefix that we might think is a visited URL if we didn't have some way to mark 'this is the end of an entry.'

# Now when we go to add 'google.com/maps' to visited, we only have to add the characters '/maps', because the 'google.com' prefix is already there. Same with 'google.com/about/jobs'.

# We can visualize this as a tree, where each node is a character. We can even implement it with node objects and edge pointers instead of nested dictionaries.


# A trie containing "donut.net", "dogood.org", "dog.com", "dog.com/about", "dog.com/pug", and "dog.org"
# If you used a bloom filter, that's a great answer too. Especially if you use run-length encoding.

# Complexity
# How much space does this save? This is about to get MATHEMATICAL.

# How many characters were we storing in our flat dictionary approach? Suppose visited includes all possible URLs of length 5 or fewer characters. Let's ignore non-alphabetical characters to simplify, sticking to the standard 26 English letters in lowercase. There are 26^526
# ​5
# ​​  different possible 5-character URLs (26 options for the first character, times 26 options for the 2nd character, etc), and of course 26^426
# ​4
# ​​  different possible 4-character URLs, etc. If we store each 5-character URL as a normal string in memory, we are storing 55 characters per string, for a total of 5 * 26^55∗26
# ​5
# ​​  characters for all possible 5-character strings (and 4 * 26^44∗26
# ​4
# ​​  total characters for all 4-character strings, etc). So for all 1, 2, 3, 4, or 5 character URLs, our total number of characters stored is:

# 5 * 26^5 + 4 * 26^4 + 3 * 26^3 + 2 * 26^2 + 1 * 26 ^ 15∗26
# ​5
# ​​ +4∗26
# ​4
# ​​ +3∗26
# ​3
# ​​ +2∗26
# ​2
# ​​ +1∗26
# ​1
# ​​ 
# So for all possible URLs of length nn or fewer, our total storage space is:

# n26^n + (n-1)26^{(n-1)} + . . . + 1 * 26 ^ 1n26
# ​n
# ​​ +(n−1)26
# ​(n−1)
# ​​ +...+1∗26
# ​1
# ​​ 
# This is O(n26^n)O(n26
# ​n
# ​​ ).

# How many characters are stored in our trie? The first layer has 26 nodes (and thus 26 characters), one for each possible starting character. On the second layer, each of those 26 nodes has 26 children, for a total of 26^226
# ​2
# ​​  nodes. The fifth layer has 26^526
# ​5
# ​​  nodes. To store all 1, 2, 3, 4, or 5 character URLs our trie will have 5 layers. So the total number of nodes is:

# 26^5 + 26^4 + 26^3 + 26^2 + 26^126
# ​5
# ​​ +26
# ​4
# ​​ +26
# ​3
# ​​ +26
# ​2
# ​​ +26
# ​1
# ​​ 
# So for all URLs of length nn or fewer, we have:

# 26^n + 26^{(n-1)} + ... + 26^126
# ​n
# ​​ +26
# ​(n−1)
# ​​ +...+26
# ​1
# ​​ 
# This is O(26^n)O(26
# ​n
# ​​ ). We've shaved off a factor of nn.

# Bonus trivia: although the HTTP spec allows for unlimited URL length, in practice many web browsers won't support URLs over 2,000 characters.

# What We Learned
# We ended up using a trie. Even if you've never heard of a trie before, you can reason your way to deriving one for this question. That's what we did: we started with a strategy for compressing a common prefix ("www") and then we asked ourselves, "How can take this idea even further?" That gave us the idea to treat each character as a common prefix.

# That strategy—starting with a small optimization and asking, "How can we take this same idea even further?"—is hugely powerful. It's one of the keys to unlocking complex algorithms and data structures for problems you've never seen before.
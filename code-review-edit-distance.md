Determine the Edit Distance in a Word Ladder: Given two words (beginWord and endWord), and a dictionary's word list, find the minimum number of operations needed to change beginWord into endWord.

You can change only one letter at a time, and each intermediate word must exist in the word list. If there is no possible transformation, return None (Python)

Examples:
beginWord = 'hit'
endWord = 'cog'
wordList = ["hit", "hot", "dot", "dog", "cog"]
output: 4 # hit -> hot -> dot -> dog -> cog

beginWord = 'word'
endWord = 'word'
wordList = ['word', 'ward']
output: 0 

beginWord = 'hit'
endWord = 'cog'
wordList = ["hit", "hot", "dot", "dog"]
output: None  # because no 'cog' in list
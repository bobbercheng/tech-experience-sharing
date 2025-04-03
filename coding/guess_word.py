from typing import List


def get_matches(word1: str, word2: str) -> int:
    """
    Count the exact matches (same letter in same position) between two words.
    """
    return sum(c1 == c2 for c1, c2 in zip(word1, word2)) 

class Master:
    def __init__(self, secret: str):
        self.secret = secret
    def guess(self, word: str) -> int:
        """
        :type word: str
        :rtype: int
        """
        matches = get_matches(self.secret, word)
        # print the guess and matches
        print(f"Guess: {word}, Matches: {matches}")
        return matches

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
        :type words: List[str]
        :type master: Master
        :rtype: None
        """
        # Initialize the list of possible words
        possible_words = words.copy()
        
        # Make at most allowedGuesses attempts
        for _ in range(10):  # We can adjust this based on allowedGuesses
            if not possible_words:
                break
            
            # Choose a word from the remaining possible words
            word_to_guess = self._choose_best_word(possible_words)
            
            # Guess the word and get the number of matches
            matches = master.guess(word_to_guess)
            
            # If we found the secret word, we're done
            if matches == 6:
                return
            
            # Filter the list of possible words based on the number of matches
            possible_words = [word for word in possible_words 
                              if word != word_to_guess and get_matches(word_to_guess, word) == matches]
    
    def _choose_best_word(self, words: List[str]) -> str:
        """
        Choose the word that has the highest probability of eliminating the most candidates.
        This uses a minimax strategy to minimize the maximum possible remaining words.
        """
        if len(words) <= 2:
            return words[0]  # Just pick the first word if there are only 1 or 2 words left
        
        # For larger sets, use a more sophisticated strategy
        best_word = None
        min_max_group_size = float('inf')
        
        for word in words[:min(len(words), 10)]:  # Limit to first 10 words for efficiency
            # Count how words would be grouped by match count
            groups = {}
            for other_word in words:
                if other_word == word:
                    continue
                matches = get_matches(word, other_word)
                groups[matches] = groups.get(matches, 0) + 1
            
            # Find the maximum group size after this guess
            max_group_size = max(groups.values()) if groups else 0
            
            # Choose the word that minimizes the maximum group size
            if max_group_size < min_max_group_size:
                min_max_group_size = max_group_size
                best_word = word
        
        return best_word if best_word else words[0]
    
def main():
    words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    master = Master("eiowzz")
    solution = Solution()
    solution.findSecretWord(words, master)

if __name__ == '__main__':
    main()
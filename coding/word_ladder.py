from collections import deque, defaultdict
from typing import List, Optional, Dict, Set


def build_pattern_graph(word_list: List[str]) -> Dict[str, Set[str]]:
    """
    Build a pattern-based graph for quick word neighbor lookups.
    For each word, create patterns with '*' at each position and group words by pattern.
    """
    patterns = defaultdict(set)
    # For each word, generate all possible patterns by replacing one character with '*'
    for word in word_list:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            patterns[pattern].add(word)
    return patterns

def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> Optional[int]:
    """
    Find the minimum number of operations needed to transform beginWord into endWord
    using bidirectional BFS and pattern-based neighbor finding.
    """
    # Handle edge cases
    if end_word not in word_list or begin_word not in word_list:
        return None
    if begin_word == end_word:
        return 0

    # Build pattern graph for quick neighbor lookups
    pattern_graph = build_pattern_graph(word_list)
    
    # Setup for bidirectional BFS
    begin_queue = deque([(begin_word, 1)])
    end_queue = deque([(end_word, 1)])
    begin_visited = {begin_word: 1}
    end_visited = {end_word: 1}
    
    def find_neighbors(word: str) -> Set[str]:
        """Find all neighboring words using pattern matching."""
        neighbors = set()
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            neighbors.update(pattern_graph[pattern])
        neighbors.discard(word)  # Remove self from neighbors
        return neighbors
    
    # Bidirectional BFS
    while begin_queue and end_queue:
        # Expand from begin side
        current_word, begin_dist = begin_queue.popleft()
        for neighbor in find_neighbors(current_word):
            if neighbor in end_visited:  # Found intersection
                return begin_dist + end_visited[neighbor] - 1
            if neighbor not in begin_visited:
                begin_visited[neighbor] = begin_dist + 1
                begin_queue.append((neighbor, begin_dist + 1))
        
        # Expand from end side
        current_word, end_dist = end_queue.popleft()
        for neighbor in find_neighbors(current_word):
            if neighbor in begin_visited:  # Found intersection
                return begin_visited[neighbor] + end_dist - 1
            if neighbor not in end_visited:
                end_visited[neighbor] = end_dist + 1
                end_queue.append((neighbor, end_dist + 1))
    
    return None

# Test cases
def test_word_ladder():
    # Test case 1
    assert word_ladder('hit', 'cog', ["hit", "hot", "dot", "dog", "cog"]) == 4
    
    # Test case 2
    assert word_ladder('word', 'word', ['word', 'ward']) == 0
    
    # Test case 3
    assert word_ladder('hit', 'cog', ["hit", "hot", "dot", "dog"]) == None
    
    # Test case 4: Larger example
    assert word_ladder('cat', 'dog', ['cat', 'cot', 'cog', 'dog']) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_word_ladder() 
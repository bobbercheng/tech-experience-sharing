from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # Maps val -> frequency
        self.group = defaultdict(list)  # Maps frequency -> list of elements with that frequency
        self.max_freq = 0  # Current maximum frequency
        
    def push(self, val: int) -> None:
        # Increment the frequency of val
        self.freq[val] += 1
        freq = self.freq[val]
        
        # Add val to the list of elements with current frequency
        self.group[freq].append(val)
        
        # Update max_freq if needed
        self.max_freq = max(self.max_freq, freq)
        
    def pop(self) -> int:
        # Get the most frequent element (closest to the top if tie)
        val = self.group[self.max_freq].pop()
        
        # Decrement its frequency
        self.freq[val] -= 1
        
        # If there are no more elements with the current max_freq, decrement max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return val

# Example usage:
if __name__ == "__main__":
    freqStack = FreqStack()
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    print(freqStack.pop())  # return 5
    print(freqStack.pop())  # return 7
    print(freqStack.pop())  # return 5
    print(freqStack.pop())  # return 4

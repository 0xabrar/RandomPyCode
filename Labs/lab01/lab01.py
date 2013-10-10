# Authors: Abrar Hussain, Tianran Liu

class KeyWords:
    """
    A class used to maintain key words of a text file within a collection.
    
    operations:
        -topN: find words that occur with n minimum frequency
        -remove_common: compare the key words of two collections, to remove from both collections the words they have in common
        -track_frequency: put key words into a collection and track frequency
    
    attributes:
        -_file_name 
        -_word_list: list containing all words in text file
        -_key_words: dictionary with key words as keys as frequency as value
    
    """
    
    def __init__(self: object, file_name: str) -> None:
        """
        Create a list to keep track add all words from file and call track_frequency to keep track of key words.
        
        >>> key = KeyWords('sample1.txt')
        
        """
        
        self._file = file_name
        self._word_list = []
        
        
        with open(self._file) as f:
            line = f.read().splitlines()
            for x in line:
                word = x.split(' ')
                self._word_list.extend(word) 
                
        self.track_frequency()    
        
        
    def track_frequency(self: object) -> None:
        """
        Create a dictionary which maintains the frequency of keys words. 
        Note: ' ' is included in the dictionary.
        
        >>> keys = KeyWords('sample1.txt')
        --- track_frequency called from __init___
        
        """
        
        self._key_words = {}
        for x in self._word_list:
            if (str(x) in self._key_words):
                self._key_words[str(x)] += 1
            else:
                self._key_words[str(x)] = 1 
                
                
    def topN(self: object, frequency: int) -> dict:
        
        """
        Return the words within the text file that have higher than n frequency.
        
        >>> keys = KeyWords('text.txt')
        >>> keys.topN(30)
        '{word: 40, ten: 33, wow: 31}'
        
        """
        
        higher_n_words = {}
        
        #add all words with higher than n frequency dictionary just created
        for key, value in self._key_words.items():
            if (int(value) >= frequency):
                higher_n_words [key] = value
        
        return higher_n_words
        
    def remove_common (self: object, other_file: 'KeyWords') -> None:
        
        """
        Compare the key words of two collections. Remove from both collections the words they have in common. If words are removed, will make the previous _word_list outdated.
        
        >>> keys = KeyWords('sample1.txt')
        >>> keys2 = KeyWords('sample2.txt') 
        >>> keys.remove_common(keys2)
        
        """
        
        #list of words that will be removed
        remove_words = []
        
        for key in self._key_words.items():
            if (key in other_file._key_words.items()):
                remove_words.extend(key)
                
        #cannot del keys from dictionary while iterating through it
        for x in remove_words:
            self._key_words.pop(x, None)
            other_file._key_words.pop(x, None)
        
            
        
            
'''
    Frame object class.
'''

class Frame():
    '''
        Counts how many frames have passed.
        count       Current count
        max_count   Max count, at which current frame count is reseted.
    '''
    def __init__(self, max):
        self.reset()
        self.max_count = max

    def reset(self):
        '''
            Resets counter.
        '''
        self.count = 0

    def add(self, n = 1):
        '''
            Increases counter by n.
        '''
        self.count += n

    def maxReached(self):
        '''
            Checks if max frame count has been reached.
        '''
        if self.count >= self.max_count:
            self.reset()
            return True
        return False
    
    def print(self, fullData = True):
        '''
            Prints out current values.
            fullData    If true, prints out both count and max_count. Otherwise function prints out only the counter value.
        '''
        if fullData:
            print(self.count, '/', self.max_count)
            return
        print(self.count)
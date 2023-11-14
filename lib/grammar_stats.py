class GrammarStats:
    def __init__(self):
        self.right_count=0
        self.wrong_count=0
        pass
  
    def check(self, text):
        punctuation_list=['!','.','?']
        if text[0].isupper() and text[-1] in punctuation_list:
            self.right_count+=1
            return True
        else:
            self.wrong_count+=1
            return False
  
    def percentage_good(self):
        total = self.right_count+self.wrong_count
        return (self.right_count/total)*100
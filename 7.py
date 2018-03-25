VOWELS = "aeiouAEIOU"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
NUMBERS = "0123456789"
class FileInfo(object):
    def __init__(self,i,o):
        self.input_file_name = i
        self.output_file_name = o
    def process(self):
        line_count=0
        word_count=0
        total=0
        consonant_count=0
        vowel_count=0
        number_count=0
        special_count=0
        with open(self.input_file_name,'r') as rf:
            with open(self.output_file_name,"w") as wf:
                for line in rf:
                    line_count+=1
                    for word in line.split():
                        word_count+=1
                        for c in word:
                            total+=1
                            if c in VOWELS:
                                vowel_count+=1
                            elif c in CONSONANTS:
                                consonant_count+=1
                            elif c in NUMBERS:
                                number_count+=1    
                special_count=total-consonant_count-vowel_count-number_count
                wf.write("line_count :"+str(line_count)+" word_count :"+str(word_count)+" total :"+str(total)+" consonant_count :"+str(consonant_count)+" vowel_count :"+str(vowel_count)+" number_count :"+str(number_count)+" special_count :"+str(special_count))
                
        

obj = FileInfo("demo.txt","demo_copy_copy")
obj.process()     

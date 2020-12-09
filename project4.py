'''
Project 4 - Text Analysis - Fall 2020
Author: <Nicholas Rooks rooksn>

<analyze files containing english>

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Nicholas Rooks>
'''

def read_text(t):
    with open(t) as file:
        text = file.read()
        return text
        
def clean_text(text):
    text = text.lower()
    punc = [',',';',':','?','!','[',']','(',')','/','\'','\"','*','.','-']
    not_punc = ''
    for char in text:
        if char in punc:
             text = text.replace(char, not_punc)
    return text

def numb_words(cleaned_text):
    number_of_words = cleaned_text.split()
    return len(number_of_words)-1

def numb_sent(text):
    total_sent = 0
    total_sent += text.count('.') + text.count('?') + text.count('!')
    return total_sent

def get_word_frequencies(cleaned_text):
    word_dict = {}
    for word in cleaned_text:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    return word_dict

def get_unique_words(word_freq):
    word_freq_length = len(word_freq)
    return word_freq_length-1

def average_word_per_sentence(word_number, sent_number):
    word = word_number
    sent = sent_number
    avg = word/sent
    return round(avg,1)

def count_syllables(word):
    ''' Estimates and returns the number of syllables in
    the specified word. '''
    syllables = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            syllables += 1
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le'):
        syllables += 1
    if syllables == 0: 
        syllables = 1
    return syllables

def count_all_syllables(cleaned_text):
    cleaned_text = cleaned_text.split(' ')
    count = 0
    for word in cleaned_text:
        count += count_syllables(word)
    return count

def syllables_per_word(all_syll, word_number):
    count = 0.0
    count = all_syll/word_number
    return round(count,1)

def flesch_reading_ease(avg_word_sent,all_syll,word_number):
    part_a = 206.835
    part_b = -1.015*(avg_word_sent)
    part_c = all_syll/word_number
    part_d = -84.6*(part_c)
    ease = part_a + part_b + part_d
    return round(ease,1)
    
def kincaid_grade_level(avg_word_sent,all_syll,word_number):
    part_a = .39*(avg_word_sent)
    part_b = all_syll/word_number
    part_c = 11.8*part_b
    level =part_a+part_c-15.59
    return round(level,1)
    
def top_twenty_words(word_freq):
    ky = []
    val = []
    frog = 20
    for words in sorted(word_freq, key=word_freq.get, reverse=True):
        ky.append(words)
    for i in range(20): 
        val.append(word_freq[ky[i]])
        print(val[i], ky[i])
        
def main():
    t = input('Name of file to analyze? ')
    text = read_text(t)
    cleaned_text = clean_text(text)
    word_number = numb_words(cleaned_text)
    sent_number = numb_sent(text)
    word_freq = get_word_frequencies(cleaned_text.split())
    uni_word = get_unique_words(word_freq)
    avg_word_sent = average_word_per_sentence(word_number,sent_number)
    all_syll = count_all_syllables(cleaned_text)
    syl_word = syllables_per_word(all_syll, word_number)
    read_ease = flesch_reading_ease(avg_word_sent,all_syll,word_number)
    grade_level = kincaid_grade_level(avg_word_sent,all_syll,word_number)
    print('Number of sentences:', sent_number)
    print('Number of words:', word_number)
    print('Number of unique words:', uni_word)
    print('Average words per sentence:', avg_word_sent)
    print('Average syllables per word:',syl_word)
    print('Reading-ease score:',read_ease )
    print('U.S. grade level:', grade_level)
    print('The 20 most common words:')
    top_twenty_words(word_freq)
if __name__ == '__main__':
    main()
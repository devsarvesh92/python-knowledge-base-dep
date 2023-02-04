from collections import Counter
import logging
import math

####################
logging.basicConfig(
    filename='exer.log',
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO
)

###################
def logger(func):
    def wrapper(*args,**kwargs):
        logging.info(f"[START] {func.__name__} with {args=} and {kwargs=}")
        result = func(*args,**kwargs)
        logging.info(f"[END] {wrapper.__name__}")
        return result
    return wrapper
###################

def arrange_sentense(sentence):
    arranged_words = []
    for word in sentence.split():
        for ch in word:
            if ch.isdigit():
                arranged_words.insert(int(ch),word.replace(ch,"").strip())
    return " ".join(arranged_words) 

def cnt_ind_consonant(sentense):
    count=0
    consonant_str=""
    for word in sentense.split():
        for ch in word:
            if ch.isalpha() and ch.lower() not in ['a','e','i','o','u']:
                consonant_str+=ch
    
    return Counter(consonant_str)

@logger
def sum_of_prime_numbers(numbers:list[int]):
    def is_prime(number):
        for num in range(2,int(math.sqrt(number))+1):
            if number % num == 0:
                return False
        return True
    numbers.sort(reverse=True)
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            if len(prime_numbers)<3:
                prime_numbers.append(num)
            else:
                break
    return sum(prime_numbers)

def count_vowel(sentense):
    return sum([sum([1 for ch in word if ch.isalpha() and ch.lower() in ['a','e','i','o','u']])for word in sentense.split()])

def remove_vowels(sentense):
    return "".join([ch for ch in sentense if ch.lower() not in ['a','e','i','o','u']])

def find_word(sentense:str,find:str):
    sentense.find(find)



if __name__ == "__main__":
    print(remove_vowels("Hello 1 World 2"))
   
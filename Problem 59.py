from collections import Counter

def timer(func):
    def wrapper(*args, **kwargs):
      import time
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print('{} ran in : {} sec'.format(func.__name__, end-start))
      return result
    return wrapper

def xor(text, key):
  return text ^ key

def check_ascii(text):
  return 32 <= ord(text) <= 122

def decode(text, key):
  text, key = text, ord(key)
  char = chr(xor(text, key))
  if check_ascii(char):
    return char
  return 0

def get_key(coded_ascii_text):
  return [chr(Counter(coded_ascii_text[i::3]).most_common(1)[0][0] ^ 32) for i in range(3)]

def read_file():
  with open('p059_cipher.txt', 'r') as f:
    coded_ascii_text = f.read().split(',')
  return [int(i) for i in coded_ascii_text]

@timer
def main():
  coded_ascii_text = read_file()
  key = get_key(coded_ascii_text)
  decoded_text, decoded_text_sum = '', 0
  for k,text in enumerate(coded_ascii_text):
    char = decode(text, key[k%3])
    try:
      decoded_text += char
      decoded_text_sum += ord(char)
    except TypeError:
      pass
  return decoded_text, decoded_text_sum, key

if __name__ == '__main__':
  decoded_text, decoded_text_sum, key = main()
  print(decoded_text)
  print(key)
  print(decoded_text_sum)
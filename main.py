def main():
  book_path = './books/frankenstein.txt'
  text = get_text(book_path)
  word_count = count_words(text)
  char_count = count_chars(text)

  char_count_sorted = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  for char in char_count_sorted:
    print(f"The '{char}' character was found {char_count[char]} times")
  print("--- End report ---")

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_counts = dict()
  for c in text.lower():
    if not c.isalpha():
      continue
    if c not in char_counts:
      char_counts[c] = 0
    char_counts[c] += 1
  return char_counts

def get_text(file_path):
  with open(file_path) as f:
    return f.read()

main()
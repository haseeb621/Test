# 2. ⁠Write program that reads a text file and prints the total number of words in the file.
def count_words_in_file(file_path):
 with open(file_path, 'r') as file:
  text = file.read()
  words = text.split()
 return len(words)



file_path = "C:/Users/HASHMI/OneDrive/Desktop/count.txt"
print("Total number of words:", count_words_in_file(file_path))
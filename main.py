# Read the story
with open("story.txt", "r") as f:
  story=f.read()
# Initalize the words
words = set()
start_of_word=-1
target_start="<"
target_end=">"
# Loop through the words
for i, char in enumerate(story):
  if char == target_start:
    start_of_word = i

  if char == target_end and start_of_word !=-1:
      word = story[start_of_word:i+1]
      words.add(word)
      start_of_word = -1
# get all words from the user
answers={}
for word in words:
   answer=input("Enter a word for "+ word + ":")
   answers[word]=answer

# Print the final story
for word in words:
   story=story.replace(word,answers[word])
print(story)
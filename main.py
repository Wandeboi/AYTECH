# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


with open('story.txt') as f:
    contents = f.read()
    print(contents)
    counts = dict()
    
    words = contents.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


    for key in list(counts.keys()):
     print(key, ":", counts[key])
    

   

    
    
  

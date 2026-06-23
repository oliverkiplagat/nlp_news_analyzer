#========================================================
# AUTHOR: Oliver Kiplagat.
# PROJECT: News Article Text Analyser.
#========================================================

# WHAT THIS PROGRAM DOES:
# Reads a news article and performs 5 text analysis tasks:
# (i): Count a specific word,
# (ii): Find the most common word,
# (iii): Calculate the average word length,
# (iv): Count paragraphs,
# (v): Count sentences.

#==========================================================
# 1.System tools and anti-crash file importation.
#==========================================================

import re

# We set up a global variable placeholder first.
article_text = ""

"""
What happens: (with open()) goes into your project folder and cracks open article.txt.
The 'r' tells your laptop, "We are only here to read the text, don't change anything.
" The .read() command takes every paragraph, space, sentence, and symbol, turns it into
one gigantic string, and locks it inside a temporary memory safe labeled article_text.
"""

try:
    with open ("article.txt" , "r" , encoding = "utf-8") as file:
        article_text = file.read()
    print ("The 'article.txt' located and read successfully into RAM.")

except FileNotFoundError:
    # This is our ultimate enginnering safety incase the file vanishes.
    print("System Warning: 'article.txt' missing from folder. Activating backup!!")

    article_text = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""

#===================================================
# 2. Function Architecture.
#===================================================
# Function(i): Count Specific Word.
#===================================================

# STRUCTURED PSEUDOCODE SOLUTON:
#   CREATE FUNCTION count_specific_word(text, word)
#       - - IF text or word is completely empty, RETURN 0.
#       - - FORCIBLY lower-case the input text content string.
#       - - FORCIBLY lower-case the input search word string.
#       - - SHIELD the search word using re.escape to ignore formatting symbols.
#       - - WRAP the shielded word inside regex word boundary anchors (\b).
#       - - EXTRACT all perfectly isolated matches into a list bucket.
#       - - CALCULATE the total quantity of items in the bucket.
#       - - RETURN that total integer count.
#   END FUNCTION

def count_specific_word(text , word):
    #This acts as a guard against empty inputs.
    if not text or not word:
        return 0

    #Case normalization - (formatting all letters to lower)
    clean_text = text.lower()
    clean_word = word.lower()

    #Neutralizing punctuation symbols so they dont break regex patterns
    shielded_word = re.escape(clean_word)

    #creating the pattern stencil string with boundary anchors
    regex_pattern = r'\b' + shielded_word + r'\b'  #the \b keeps my matches from bleeding to other symbols.

    #running the matching algorithm engine
    match_bucket = re.findall(regex_pattern , clean_text)

    #computing the final list length and sending the integer value back
    final_count = len(match_bucket)
    return final_count

#END of Function!!.
#=====================================================
# Function(ii): Find Most Common Word.
#=====================================================

# PSEUDOCODE SOLUTION.
# CREATE FUNCTION find_most_common_word(text)
#    - - - If the input text string is empty or None, return an empty string and 0.
#    - - - Forcibly lowercase the entire text block to eliminate capital letter tracking errors.
#    - - - Deploy an alphabetic regex stencil (\b[a-z]+\b) to extract only words, completely leaving punctuation behind.
#    - - - If the extraction pool is completely empty, return an empty string and 0.
#    - - - Create an empty word frequency dictionary container.
#    - - - Loop through every isolated word in the extraction pool:
#            - (a) If the word is already inside our dictionary keys, increment its count value by 1.
#            - (b) If the word is missing, register it into the dictionary with an initial baseline value of 1.
#    - - - Search the dictionary to find the key containing the absolute maximum count value.
#    - - - Return a tuple pair containing the champion word and its total frequency count.
#END FUNCTION

def find_most_common_word(text):
    #Guarding against null or empty string arguments.
    if not text:
        return ("" , 0)

    #standardizing the case
    clean_text = text.lower()

    #Extracting letters [a-z]
    word_pool = re.findall(r'\b[a-z]+\b' , clean_text) #This ensures puntuation symbols are entirely ignored

    #cheking if no words were extracted
    if not word_pool:
        return ("" , 0)

    #intializing counting dictionary(our mini-database)
    frequency_data = {}

    #Executing the distribution calculation loop
    for word in word_pool:
        if word in frequency_data:
            frequency_data[word] += 1   #Adding to existing tally.
        else:
            frequency_data[word] = 1    #set up new entry with 1 count.

    #Locating the most common word.
    champion_word = max(frequency_data, key=frequency_data.get)
    champion_count = frequency_data[champion_word]

    #final output
    return champion_word , champion_count
#END OF FUNCTION!


#===========================================
# Function(iii): Average Word Length.
#===========================================
"""
PSEUDOCODE SOLUTION.
CREATE FUNCTION calculate_average_word_length(text)
    - - - Safety Check.If the text is completely empty, stop immediately and return 0
    - - - Clean the text and pull out only the actual words using our regular expression.
            Put them all into a list.
    - - - Measurement.Counting the absolute grand total of letters across all words combined.
            Count the total number of words sitting inside the basket.
    - - -  Final Math
            Divide (Grand Total of Letters) by (Total Number of Words).
            Return that final decimal number.
END FUNCTION
"""

def calculate_average_word_length(text):
    #Safety check
    if not text:
        return 0.0   #must return a float.

    #standardizing the text to lower.
    clean_text = text.lower()
    word_pool = re.findall(r'\b[a-z]+\b' , clean_text)

    #second security guard to check if the text contains only numbers or symbols.
    if not word_pool:
        return 0.0

    #Measuring the grand total of all letters combined
    total_letters = sum(len(word) for word in word_pool)

    #store volume of total words.
    total_words = len(word_pool)

    #Executing division to compute the true mathematical average.
    average_length = total_letters / total_words

    #Delivering the clean float value back.
    return average_length

#======================================================
# Function(iv): Count Paragraphs.
#======================================================
"""
PSEUDOCODE SOLUTION
CREATE FUNCTION count_paragraphs(text)

    - - - Safety Check
            If the text box is totally empty, stop immediately and return 0.

    - - - Gap Splitter
            Cut the entire text block into pieces wherever there is a  line break.
            Store these raw chunks in a list

    - - - Ghost Filter
            Create a clean list called "clean_paragraphs".
            Loop through our raw chunks and drop them into the clean list only if they
            contain actual real words or letters (ignoring blank lines).

    - - - The Final Count
            Count how many real items made it into our clean list.
            Return that final whole integer number.

END FUNCTION
"""
def count_paragraphs(text):
    #Safety check
    if not text:
        return 0

    #cutting text into blocks at every double line break
    raw_chunk_texts = text.split("\n\n")

    #empty list to store and hold valid , real paragraphs.
    clean_paragraphs = []

    #Ghost filter loop to filter every chunk text and filter out sneaky empty lines.
    for chunk in raw_chunk_texts:
        if chunk.strip():
            clean_paragraphs.append(chunk)

    #Measuring the length of our clean list and return whole integer.
    final_paragraph_count = len(clean_paragraphs)
    return final_paragraph_count
#END of Function!!


#=====================================================
# Function(v): Count Sentences.
#=====================================================
"""
PSEUDOCODE SOLUTION.
CREATE FUNCTION count_sentences(text)

    - - - Safety Check
            If the text is completely blank, stop immediately and return 0.

    - - - Sentence Slicer
            Use a regex split command to slice the text into separate pieces
            wherever a period (.), question mark (?), or exclamation mark (!) appears.
            Store these raw pieces in a list called "raw_sentences".

    - - - Empty Filter
            Create a clean list. Loop through our raw pieces
            and keep them only if they contain actual characters (ignoring empty spaces).

    - - - Final Math
            Count how many real sentences made it into our clean list.
            Return that final total number.

END FUNCTION
"""
def count_sentences(text):
    #safety check to protect against empty null strings
    if not text:
        return 0

    #Protection layer: Neutralize abbreviation periods do they dont trick the splitter
    safe_text = text.replace("Inc." , "Inc").replace("Dr." , "Dr")
    #slicing the text at every terminal punctuation mark.
    raw_sentences = re.split(r'[.!?]+' , safe_text)

    #empty list to hold valid sentences
    clean_sentences =  []

    #Filtering out trailing spaces and empty remnants.
    for sentence in raw_sentences:
        if sentence.strip():
            clean_sentences.append(sentence.strip())

    #Quantifying the total sentence volume and hand back integer metric.
    final_sentence_count = len(clean_sentences)
    return final_sentence_count
#END OF FUNCTION!

#Executing structure.


#=======================================================
# FINAL STRUCTURE : Interactive Menu Loop.
#=======================================================
"""
PSEUDOCODE SOLUTION.
CREATE FUNCTION display_menu()
    PRINT "=== NEWS ARTICLE TEXT ANALYSER ==="
    PRINT "1. Count a specific word"
    PRINT "2. Find the most common word"
    PRINT "3. Calculate average word length"
    PRINT "4. Count total paragraphs"
    PRINT "5. Count total sentences"
    PRINT "6. Exit Program"
END FUNCTION

# MAIN INTERACTIVE LOOP CONTEXT
SET running = True

WHILE running IS True:
    CALL display_menu()
    PROMPT user for input choice

    IF choice EQUALS "1":
        PROMPT user for the specific target word
        CALL count_specific_word(article_text, target_word)
        PRINT the resulting count matching that word

    ELSE IF choice EQUALS "2":
        CALL find_most_common_word(article_text)
        PRINT the champion word and its breakdown frequency

    ELSE IF choice EQUALS "3":
        CALL calculate_average_word_length(article_text)
        PRINT the formatted average character length

    ELSE IF choice EQUALS "4":
        CALL count_paragraphs(article_text)
        PRINT the total paragraph count metric

    ELSE IF choice EQUALS "5":
        CALL count_sentences(article_text)
        PRINT the total sentence count metric

    ELSE IF choice EQUALS "6":
        PRINT a closing exit message
        SET running = False (Breaks the loop)

    ELSE:
        PRINT an error warning for invalid inputs
"""

def display_menu():
    print ("\n" + "=" * 60)
    print ("             NEWS ARTICLE TEXT ANALYSER MENU            ")
    print ("=" * 60)
    print ("  [1] Count how many times a specific word appears")
    print ("  [2] Find the absolute most common word used")
    print ("  [3] Calculate the average length of all words")
    print ("  [4] Count the total number of real paragraphs")
    print ("  [5] Count the total number of sentences")
    print ("  [6] Exit Program and close connection")
    print ("=" * 60)

    #setting up our loop control condition state variable.
is_running = True

while is_running:
    display_menu() #calling presentation layer layout

    #capture user interface navigation decision
    user_choice = input ("Enter your selection choice (1-6): ").strip()
    print ("-" * 60)

    #conditional Decision tree
    if user_choice == "1":
        search_word = input("Enter the specific word you want to search for: ").strip()
        if search_word:
            appearance = count_specific_word(article_text , search_word)
            print(f"RESULT: The word '{search_word}' , appears {appearance} times.")
        else:
            print ("System Error : You must enter a valid word to execute search.")

    elif user_choice == "2":
        most_common , frequency = find_most_common_word(article_text)
        if most_common:
            print (f"RESULT: The most common word is '{most_common}' (used {frequency} times.)")
        else:
            print ("System Error")

    elif user_choice == "3":
        avg_length = calculate_average_word_length(article_text)
        print (f"RESULT: the average word length is {avg_length:.2f} characters.")

    elif user_choice == "4":
        paragraphs = count_paragraphs(article_text)
        print (f"Analysis Result: Detected total of {paragraphs} paragraphs.")

    elif user_choice == "5":
        sentences = count_sentences(article_text)
        print (f"RESULT: Detected a total of {sentences} sentences.")

    elif user_choice == "6":
        print ("Shutting down text analyzer goodbye!")

        is_running = False

    else:
        #security shield incase of accidental wrong typing.
        print("Invalid Selection! Please enter a single digit intger from 1 to 6")

print ("=" * 60 + "\n")
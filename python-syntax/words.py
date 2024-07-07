# def print_upper_words(words):
#     """prints words from list(words) in all caps"""


#     for word in words:
#         print(word.upper())


# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

# def print_upper_words(words):
#     """prints words from list(words) that start with "e" in all caps"""


#     for word in words:
#         if word.startswith("e") or word.startswith("E"):
#             print(word.upper())


# print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "ello"])

def print_upper_words(words, must_start_with):
    """
    prints words from list(words) that start with letters defined in must_start_with parameter
    """


    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


# print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "excited"])

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})


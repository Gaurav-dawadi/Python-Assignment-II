"""Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text."""


inputParagraph = input("Enter text for checking anagrams: ")

inputSorted = sorted(inputParagraph)

print("The Anagrams is ", ''.join(inputSorted))
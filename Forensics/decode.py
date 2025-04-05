def decode(message_file):
  """
  Decodes a message from a text file with line format "number word".

  Args:
      message_file (str): Path to the text file containing the encoded message.

  Returns:
      str: The decoded message.
  """

  # Initialize variables
  decoded_message = ""
  word_dict = {}  # Dictionary to store number: word pairs

  # Read the file line by line
  with open(message_file, "r") as file:
    for line in file:
      number, word = line.strip().split()  # Split line and remove whitespace
      number = int(number)  # Convert number to integer
      word_dict[number] = word  # Add number-word pair to dictionary

  # Find maximum number of words in a line based on dictionary size
  max_words = len(word_dict)

  # Iterate through pyramid levels
  for level in range(1, max_words + 1):
    # Get the word at the end of the current level
    end_of_level = level * (level + 1) // 2
    if end_of_level in word_dict:
      decoded_message += word_dict[end_of_level] + " "  # Add word with space

  return decoded_message.strip()  # Remove trailing space from decoded message

# Example usage
message_file = "./coding_qual_input.txt"  # Replace with your file path
decoded_message = decode(message_file)
print(decoded_message)
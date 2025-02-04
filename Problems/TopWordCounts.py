"""
Write a Python program to read a file and count the number of words in the file. It should show the 10 most common words in the file.
"""

        
def top_word_counts(file_path: str) -> list:
    word_counts = {}
    punctuations = """,./?;:'"\|~!@#$%^&*(){}[]-_"""

    try:
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = ''.join([char.lower() if char not in punctuations else ' ' for char in line])
                words = cleaned_line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_counts[:10]

    except FileNotFoundError:
        print(f"Input file at path {file_path} was not found.")
        return []
    except IOError:
        print(f"Error occurred while reading the file {file_path}.")
        return []



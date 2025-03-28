def get_num_words(book_content: str) -> int:
    words = book_content.split()
    return len(words)

def get_num_letter(book_content: str) -> dict[str, int]:
    result = {}

    words = book_content.split()
    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if not lower_letter in result:
                result[lower_letter] = 0

            result[lower_letter] += 1

    return result

def sort_letter_dict(letter_dict: dict[str, int]) -> list[dict[str, str]]:
    result = []

    for letter in letter_dict:
        dict = {
            "character": letter,
            "count": letter_dict[letter] 
        }
        result.append(dict)

    result.sort(key=lambda i: -i["count"])
    return result
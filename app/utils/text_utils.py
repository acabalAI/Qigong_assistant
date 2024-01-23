# app/utils/text_utils.py

def split_text_into_chunks(text, chunk_size=500, overlap=50):
    """
    Split a text into smaller chunks with optional overlap.

    :param text: The text to be split.
    :param chunk_size: The size of each chunk.
    :param overlap: The number of overlapping characters between chunks.
    :return: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start = end - overlap  # Overlap the chunks
    return chunks

def sanitize_text(text):
    """
    Sanitize text by removing unwanted characters or formatting.

    :param text: The text to be sanitized.
    :return: Sanitized text.
    """
    # Example: Replace newlines with spaces, remove excessive whitespace
    return ' '.join(text.replace('\n', ' ').split())

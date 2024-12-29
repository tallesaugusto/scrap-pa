import re
import unicodedata


def clean_and_upper_text(text):
    # Normalize the text to decompose special characters into base characters + accents
    normalized = unicodedata.normalize('NFD', text)
    # Remove accents by discarding non-spacing marks (e.g., diacritics like accents)
    without_accents = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    # Remove non-alphanumeric characters except spaces, and convert to uppercase
    cleaned = re.sub(r'[^A-Za-z0-9 ]', '', without_accents).upper()
    # Replace multiple spaces with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

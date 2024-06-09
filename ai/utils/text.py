""" Text processing utilities """


# Create your utils here.
def clean_output(text: str) -> str:
    """Clean the output of the model."""

    return text.strip().replace(" . ", ". ").replace(" .", ".")

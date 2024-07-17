import stanfordnlp

# Specify the language code for Hindi model download
lang_code = "hi"

nlp = stanfordnlp.Pipeline(lang=lang_code)

text = "यह एक उदाहरण वाक्य है।"  # Hindi text - "This is an example sentence."

doc = nlp(text)

# Access tokens (words) in the sentence
tokens = [token.text for token in doc.sentences[0].tokens]

print(tokens)

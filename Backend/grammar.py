import language_tool_python 

tool = language_tool_python.LanguageTool("en-US") #This is an NLP tool that detects grammar and spelling errors.

def check_grammar(text):
    matches = tool.check(text) #Scans the text and returns a list of errors (matches).
    corrected_text = text

    for match in reversed(matches):   # Start fixing from the last error
        if match.replacements:  # Ensure there is a suggested replacement
            corrected_text = (
                corrected_text[:match.offset] +
                match.replacements[0] +
                corrected_text[match.offset + match.errorLength:]
            )

    return corrected_text

# error_parser.py

def suggest_fix(error_log):
    suggestions = []

    if "ModuleNotFoundError" in error_log:
        lines = error_log.split("\n")
        for line in lines:
            if "ModuleNotFoundError" in line:
                module = line.split("'")[1]
                suggestions.append(f"Try installing the module: pip install {module}")

    if "SyntaxError" in error_log:
        suggestions.append("Check for missing colons, brackets, or incorrect indentation.")

    if "IndentationError" in error_log:
        suggestions.append("Check for inconsistent indentation. Use spaces or tabs consistently.")

    if "NameError" in error_log:
        suggestions.append("You might be using a variable/function that hasn't been defined.")

    if "TypeError" in error_log:
        suggestions.append("Check if the right data types are used in operations.")

    if "AttributeError" in error_log:
        suggestions.append("Check if the object has that attribute or method.")

    if "ImportError" in error_log:
        suggestions.append("Check if the module or file exists and is correctly named.")

    return suggestions if suggestions else ["No suggestions found. Try checking Stack Overflow."]

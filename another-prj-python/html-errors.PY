def get_html_error_solution(error_code):
    """
    Provides solutions for common HTML errors.

    Parameters:
    - error_code: A string describing the HTML error.

    Returns:
    - A solution or guidance for the provided error.
    """
    solutions = {
        "missing-doctype": "Ensure the first line of your HTML file is: <!DOCTYPE html>",
        "unclosed-tag": "Check if all HTML tags are properly closed. For example, <div> should have a matching </div>.",
        "missing-alt-attribute": "Add an 'alt' attribute to all <img> tags to improve accessibility.",
        "invalid-attribute": "Verify that the attribute you used is valid for the specific HTML element.",
        "nested-form": "HTML does not allow one <form> inside another. Reorganize your forms.",
        "nonexistent-element": "Ensure that all referenced elements (e.g., in IDs or classes) exist in the document.",
        "deprecated-tag": "Avoid using tags that are no longer supported, such as <font>. Use CSS for styling.",
    }
    
    return solutions.get(error_code, "Error not recognized. Please check your HTML and try again.")

# Example usage
if __name__ == "__main__":
    print("Common HTML Errors:")
    print("1. missing-doctype")
    print("2. unclosed-tag")
    print("3. missing-alt-attribute")
    print("4. invalid-attribute")
    print("5. nested-form")
    print("6. nonexistent-element")
    print("7. deprecated-tag")

    error = input("Enter the error code or description (e.g., 'missing-doctype'): ").strip()
    solution = get_html_error_solution(error)
    print(f"Solution: {solution}")

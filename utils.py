import re

def extract_question_answer(message):
    # Regular expression to match the expected format
    pattern = r"^(.*\?) - (.+)$"

    match = re.match(pattern, message)

    if match:
        question = match.group(1).strip()  # Extract the question part
        answer = match.group(2).strip()    # Extract the answer part
        data = (question, answer)
        return data
    else:
        # If the message doesn't match the expected format, handle the error
        raise ValueError("Invalid format. Please use the format 'Question? - Answer'.")

# # Example usage:
# message = "How am I managing my stress? - I meditate every morning, I do yoga, cardio, and breathing exercises 4 times every week."
# try:
#     question, answer = extract_question_answer(message)
#     print("Question:", question)
#     print("Answer:", answer)
# except ValueError as e:
#     print("Error:", e)

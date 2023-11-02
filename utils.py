import re
import os


class Utilities:

    def extract_question_answer(self, message):
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
        
    def delete_cv_file(self, local_path):

        # Check if the file exists before attempting to delete it
        if os.path.exists(local_path):
            try:
                os.remove(local_path)  # Delete the file
                print(f"File at '{local_path}' has been deleted.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"File '{local_path}' does not exist.")

# # Example usage:
# message = "How am I managing my stress? - I meditate every morning, I do yoga, cardio, and breathing exercises 4 times every week."
# try:
#     question, answer = extract_question_answer(message)
#     print("Question:", question)
#     print("Answer:", answer)
# except ValueError as e:
#     print("Error:", e)

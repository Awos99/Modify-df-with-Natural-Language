from openai import OpenAI

def generate_dataframe_modif_code(df, objective):
    # Initialize OpenAI API
    client = OpenAI()
    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system", 
            "content": '''As a proficient Python developer, your task is to design a script that meticulously customizes a DataFrame to meet specific user-defined criteria. This script is intended for a single execution.

                Key requirements for the script include:
                1. Simplicity and Clarity: Keep the code streamlined, while carefully considering the types of values within the DataFrame.
                2. Handling Missing Values: Efficiently manage any missing (NA) values in the DataFrame.
                3. Precise Customization: Accurately implement the modifications requested by the user.
                4. Final Output: Ensure the script returns the altered DataFrame.

                Enclose your solution in a function named modify_dataframe(df). This function should be complete, self-contained, and executable as provided. Deliver the Python code in a clean format, strictly containing the code with no additional comments or usage examples.

                Make certain your implementation precisely conforms to the specifications, ensuring accuracy in every aspect of the user's request, such as manipulating the exact number of rows or applying the correct data transformations.'''
        },
        {
            "role": "user", 
            "content": f"Here are the first 10 rows of the dataframe: {df.head(10)}. Here is the instruction: {objective}."
        }
    ]

    )
    
    return completion.choices[0].message.content.replace("```", '').replace("python", '')

import os
# import google.generativeai as genai
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# client = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# # model = genai.GenerativeModel("gemini-2.0-flash")
# # model = genai.GenerativeModel("gemini-1.5-flash")
#
print("Gemini model ready!")


def generate_answer(query, ranked_results):
    # Generate an answer from retrieved chunks using Gemini"""

    # Combine top chunks into context
    context = "\n\n".join([result["text"] for result in ranked_results])

    # print('CONTEXT : ', context)
    # exit(0)

    # Create prompt
    prompt = f"""You are a UK insolvency law expert. Based on the context provided below, 
    answer the user's question in a clear and detailed way.

    Context:
    {context}

    Question: {query}

    Provide a helpful and informative answer based on the context above. 
    If the context only partially answers the question, provide what you can from the context."""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

# from google import genai
#
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
#
# response = client.models.generate_content(
#     model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
# )
# print(response.text)

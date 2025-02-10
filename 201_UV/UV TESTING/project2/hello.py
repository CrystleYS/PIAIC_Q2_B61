from litellm import completion

import os
os.environ["GEMINI_API_KEY"] = "AIzaSyAs76QVKnrG1b1H1KAUQmBuKXAosASQPdg"

def gemini1() ->None:
    print("gemini1")
    result = completion(
        model="gemini/gemini-1.5-flash-exp"
        messages = [{"content": "Who is the founder of piaic?" 
                     "role": "user"}]
    )

    print (result ['choices'] [0] ['message'] ['content'])
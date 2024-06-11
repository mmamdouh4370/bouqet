from flask import Flask, request, jsonify
from flask_cors import CORS
import os, json
import requests
from openai import OpenAI

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

app = Flask(__name__)
CORS(app)

print("weee")

def searchImage(query):
    print("imgs")
    api_key = os.environ.get("GI_api_key")
    cx = os.environ.get("GI_cx")
    
    search_type = "image"
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&searchType={search_type}&q={query}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            return data["items"][0]["link"]
    return None

@app.route("/api/gen", methods=["POST"])

def gen():
    print("hit route")
    data = request.get_json()
    userInput = data.get('prompt')

    if not userInput:
        return jsonify({"error" : "No prompt provided"}), 400

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type" : "json_object"},
        messages=[
            {"role": "system", "content": 
            """You are an assistant who will recommend flowers based on a user's input for a bouquet in a json format. 
            Relate the flowers in meaning and symbolism to the input. 
            Make sure the flower combinations are aesthetic and meaningful. 
            Make sure to always refer to flowers as plural.
            Be sure to recommend 4-7 flowers.
            Every message you respond with must STRICTLY follow this json format, do not add on anything extra 
            (adjust for number of flowers remembering a minimum of 4 and maximum of 7): 
            "numOfFlowers": "",
            "flower1Name": "", 
            "flower2Name": "",
            (etc for every flower)
            "flower1Desc": "Explanation of flower 1's meaning and symbolism, keep it general and NOT related to the prompt",
            "flower2Desc": "Explanation of flower 2's meaning and symbolism, keep it general and NOT related to the prompt"
            (etc for every flower)

            If the user input does not make sense, return "Please try again."
            """},
            {"role": "user", "content": userInput}
            
        ]
    )

    responseMessage = response.choices[0].message.content
    responseMessageDict = json.loads(responseMessage)
    numFlowers = int(responseMessageDict["numOfFlowers"])
    print(numFlowers)

    for i in range(1, numFlowers+1): 
        flowerName = responseMessageDict[f"flower{i}Name"]
        searchQuery = f"{flowerName} flower"
        responseMessageDict[f"flower{i}Img"] = searchImage(searchQuery)

    print(json.dumps(responseMessageDict))
    return jsonify(json.dumps(responseMessageDict))
    


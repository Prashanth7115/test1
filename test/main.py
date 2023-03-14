from flask import Flask, jsonify, request
import openai
import os

app = Flask(__name__)

openai.api_key = "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"

model_engine = "text-davinci-003"

def remove_special_characters(str):
    return str.replace("[^\w\s#]", '')

@app.route('/model-output', methods=['POST'])
def model_output_post():
    data = request.json
    title = data.get('title', '')
    desc = data.get('desc', '')
    prompt = data.get('prompt', '')
    p = ""

    # Check if prompt is requesting programming language or code as output
    if any(x in prompt for x in ["Java", "Python", "C++", "Ruby", "JavaScript"]):
        # Extract the first class definition from the generated output
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.7,
            max_tokens=834,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        output_text = response.choices[0].text.strip()
        first_class = ""
        for line in output_text.splitlines():
            if line.startswith("class "):
                first_class = line.split()[1].split("(")[0]
                break

    else:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.7,
            max_tokens=834,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        output_text = response.choices[0].text.strip()

    return remove_special_characters(output_text)

if __name__ == '__main__':
    app.run()

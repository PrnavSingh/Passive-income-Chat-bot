from flask import Flask, render_template, request, jsonify
import together


together.api_key = "18627d5d2d3d1b6ce22a77c8d9fc24db6faf1be2ddd00425e0599f2f272210c0"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        # LLaMA-style prompt format using [INST] ... [/INST]
        full_prompt = f"[INST] You are a helpful advisor for passive income. {user_message} [/INST]"

        response = together.Complete.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            prompt=full_prompt,
            max_tokens=300,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )

        reply = response['choices'][0]['text'].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

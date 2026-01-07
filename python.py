from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    temp = float(data["temperature"])
    mode = data["mode"]

    if mode == "cToF":
        result, unit = (temp * 9/5) + 32, "°F"
    elif mode == "fToC":
        result, unit = (temp - 32) * 5/9, "°C"
    elif mode == "cToK":
        result, unit = temp + 273.15, "K"
    elif mode == "kToC":
        result, unit = temp - 273.15, "°C"
    elif mode == "cToRa":
        result, unit = (temp + 273.15) * 9/5, "°R"
    elif mode == "raToC":
        result, unit = (temp - 491.67) * 5/9, "°C"
    elif mode == "cToRe":
        result, unit = temp * 4/5, "°Ré"
    elif mode == "reToC":
        result, unit = temp * 5/4, "°C"
    elif mode == "cToDe":
        result, unit = (100 - temp) * 3/2, "°De"
    elif mode == "deToC":
        result, unit = 100 - (temp * 2/3), "°C"
    elif mode == "cToN":
        result, unit = temp * 33/100, "°N"
    elif mode == "nToC":
        result, unit = temp * 100/33, "°C"
    elif mode == "cToRo":
        result, unit = (temp * 21/40) + 7.5, "°Rø"
    elif mode == "roToC":
        result, unit = (temp - 7.5) * 40/21, "°C"
    else:
        return jsonify({"error": "Invalid conversion"})

    return jsonify({
        "result": round(result, 2),
        "unit": unit
    })

if __name__ == "__main__":
    app.run(debug=True)

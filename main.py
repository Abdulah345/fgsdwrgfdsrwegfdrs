from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-id', methods=['GET'])
def get_id():
    # Get the client IP
    client_ip = request.headers.get('x-real-ip', request.remote_addr)

    # Log the IP address for debugging
    print(f"Client IP: {client_ip}")

    # Check if the IP starts with "128.16"
    if client_ip.startswith("128.166"):
        id_value = "0x622C03769C8F"  # Replace with your actual ID generation logic
        return jsonify({"id": id_value}), 200
    else:
        return jsonify({"ip": client_ip, "message": "IP does not match."}), 200

if __name__ == "__main__":
    app.run()

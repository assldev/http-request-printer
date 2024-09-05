from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return respond_with_request_details(request)

@app.route('/<path:path>')
def catch_all(path):
    print(f"Received request for path: {path}")
    return respond_with_request_details(request)

def respond_with_request_details(request):
    # Get details from the request
    method = request.method
    path = request.path
    headers = dict(request.headers)  # Convert headers to a dictionary
    data = request.data.decode('utf-8')

    # Prepare response data
    request_details = {
        "method": method,
        "path": path,
        "headers": headers,
        "data": data
    }

    # Return JSON response
    return jsonify(request_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
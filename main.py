from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {}
user_id_counter = 1

# CREATE
@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()
    user_id = user_id_counter
    users[user_id] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "designation": data.get("designation"),
        "company": data.get("company"),
        "ctc": data.get("ctc"),
        "experience": data.get("experience")
    }
    user_id_counter += 1
    return jsonify({"id": user_id, "message": "User created"}), 201

# READ ALL
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# READ ONE
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# UPDATE
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.update({
        "name": data.get("name", user["name"]),
        "age": data.get("age", user["age"]),
        "designation": data.get("designation", user["designation"]),
        "company": data.get("company", user["company"]),
        "ctc": data.get("ctc", user["ctc"]),
        "experience": data.get("experience", user["experience"])
    })
    return jsonify({"message": "User updated", "user": user})

# DELETE
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


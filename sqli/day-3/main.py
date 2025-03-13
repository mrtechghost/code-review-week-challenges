from flask import Flask, request, jsonify
import sqlite3
import re
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guestpass')")
    conn.commit()

def search_users(query):
    sql_query = f"SELECT * FROM users WHERE username LIKE '%{query}%'" 
    cursor.execute(sql_query)
    results = cursor.fetchall()
    return [{"id": row[0], "username": row[1]} for row in results]

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("user", "")

    # Remove spaces
    query = query.replace(" ", "")

    # Block common SQL injection keywords 
    forbidden_keywords = ["union", "select", "from"]
    for keyword in forbidden_keywords:
        query = re.sub(keyword, "", query, flags=re.IGNORECASE)

    app.logger.info(f"Query: {query}")

    results = search_users(query)
    return jsonify({"users": results})

if __name__ == "__main__":
    init_db() 
    app.run(host="0.0.0.0", port=5000, debug=True)

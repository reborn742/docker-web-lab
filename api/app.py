import os
import time
import psycopg
from flask import Flask, jsonify, request

app = Flask(__name__)

def connect_db():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.getenv("DB_NAME", "tasks"),
        user=os.getenv("DB_USER", "taskuser"),
        password=os.getenv("DB_PASSWORD", "taskpass")
    )

def init_db():
    for attempt in range(15):
        try:
            with connect_db() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        completed BOOLEAN NOT NULL DEFAULT FALSE
                    )
                """)
            return
        except psycopg.OperationalError:
            if attempt == 14:
                raise
            time.sleep(2)

@app.route("/health")
def health():
    try:
        with connect_db() as conn:
            conn.execute("SELECT 1")
        return jsonify(status="healthy")
    except Exception:
        return jsonify(status="unhealthy"), 503

@app.route("/tasks", methods=["GET"])
def list_tasks():
    with connect_db() as conn:
        rows = conn.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id"
        ).fetchall()
    return jsonify([
        {"id": r[0], "title": r[1], "completed": r[2]} for r in rows
    ])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify(error="Title is required"), 400
    with connect_db() as conn:
        row = conn.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, completed",
            (title,)
        ).fetchone()
    return jsonify(id=row[0], title=row[1], completed=row[2]), 201

@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def complete_task(task_id):
    data = request.get_json(silent=True) or {}
    with connect_db() as conn:
        row = conn.execute(
            """UPDATE tasks SET completed = %s WHERE id = %s
               RETURNING id, title, completed""",
            (bool(data.get("completed", True)), task_id)
        ).fetchone()
    if row is None:
        return jsonify(error="Task not found"), 404
    return jsonify(id=row[0], title=row[1], completed=row[2])

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    with connect_db() as conn:
        result = conn.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    if result.rowcount == 0:
        return jsonify(error="Task not found"), 404
    return "", 204

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

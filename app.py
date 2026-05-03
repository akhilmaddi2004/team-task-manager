from flask import Flask, request, render_template, redirect
from models import db, User, Project, Task

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret123'

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("login.html")

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.form

    # 🔍 Check if email already exists
    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return "❌ Email already exists. Try a different email."

    # ✅ Create new user
    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return redirect("/")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.form

    user = User.query.filter_by(
        email=data["email"],
        password=data["password"]
    ).first()

    if user:
        return redirect(f"/dashboard/{user.id}")
    else:
        return "❌ Invalid email or password"

# ---------------- DASHBOARD ----------------
@app.route("/dashboard/<int:user_id>")
def dashboard(user_id):
    total = Task.query.count()
    completed = Task.query.filter_by(status="Completed").count()
    pending = Task.query.filter_by(status="Pending").count()

    projects = Project.query.all()
    tasks = Task.query.all()

    return render_template(
        "dashboard.html",
        total=total,
        completed=completed,
        pending=pending,
        projects=projects,
        tasks=tasks,
        user_id=user_id
    )

# ---------------- CREATE PROJECT ----------------
@app.route("/create_project/<int:user_id>", methods=["POST"])
def create_project(user_id):
    data = request.form

    if not data["name"]:
        return "❌ Project name required"

    project = Project(
        name=data["name"],
        created_by=user_id
    )

    db.session.add(project)
    db.session.commit()

    return redirect(f"/dashboard/{user_id}")

# ---------------- CREATE TASK ----------------
@app.route("/create_task/<int:user_id>", methods=["POST"])
def create_task(user_id):
    data = request.form

    if not data["title"]:
        return "❌ Task title required"

    task = Task(
        title=data["title"],
        description=data["description"],
        status="Pending",
        deadline=data["deadline"],
        assigned_to=data["assigned_to"],
        project_id=data["project_id"]
    )

    db.session.add(task)
    db.session.commit()

    return redirect(f"/dashboard/{user_id}")

# ---------------- UPDATE TASK ----------------
@app.route("/update_task/<int:id>/<int:user_id>")
def update_task(id, user_id):
    task = Task.query.get(id)

    if not task:
        return "❌ Task not found"

    task.status = "Completed"
    db.session.commit()

    return redirect(f"/dashboard/{user_id}")

# ---------------- RUN ----------------
# if __name__ == "__main__":
#     app.run(debug=True)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
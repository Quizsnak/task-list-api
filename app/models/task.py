from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable= False)
    description = db.Column(db.Text, nullable= False)
    completed_at = db.Column(db.DateTime, nullable= True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"))
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        return_dict = {}
        return_dict["id"] = self.task_id
        return_dict["title"] = self.title
        return_dict["description"] = self.description
        if self.completed_at:
            return_dict["is_complete"] = True
        if not self.completed_at:
            return_dict["is_complete"] = False
        if self.goal_id:
            return_dict["goal_id"] = self.goal_id
        return return_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            description = data_dict["description"],
            completed_at = data_dict.get("completed_at")
        )
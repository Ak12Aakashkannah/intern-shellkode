import json
import os
from datetime import datetime


# ── Task class ─────────────────────────────────────────────

class Task:
    def __init__(self, task_id, title, done=False, created_at=None):
        self.task_id = task_id
        self.title = title
        self.done = done
        self.created_at = created_at or datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["done"],
            data["created_at"]
        )

    def __str__(self):
        status = "Done" if self.done else "Not Done"
        return f"[{status}] #{self.task_id} - {self.title}"


# ── TaskManager class ──────────────────────────────────────

class TaskManager:

    FILE = "tasks.json"

    def __init__(self):

        # Hash Map
        # Key   -> task position / task ID
        # Value -> Task object
        self.tasks = {}

        self._load()

    # ── Load tasks ─────────────────────────────────────────

    def _load(self):

        if os.path.exists(self.FILE):

            try:

                with open(self.FILE, "r") as file:

                    data = json.load(file)

                    self.tasks = {
                        task_data["task_id"]:
                        Task.from_dict(task_data)

                        for task_data in data
                    }

                    # Ensure IDs are sequential
                    self._reorder_tasks()

            except (
                json.JSONDecodeError,
                KeyError
            ):

                print(
                    "Warning: Could not read tasks file."
                )

                self.tasks = {}

    # ── Save tasks ─────────────────────────────────────────

    def _save(self):

        with open(self.FILE, "w") as file:

            json.dump(
                [
                    task.to_dict()
                    for task in self.tasks.values()
                ],
                file,
                indent=2
            )

    # ── Get next available position ────────────────────────

    def _next_id(self):

        return len(self.tasks) + 1

    # ── Reorder tasks ──────────────────────────────────────
    # This removes gaps after deleting a middle task.

    def _reorder_tasks(self):

        new_tasks = {}

        # Sort tasks by current ID
        sorted_tasks = sorted(
            self.tasks.values(),
            key=lambda task: task.task_id
        )

        # Assign new sequential positions
        for new_id, task in enumerate(
            sorted_tasks,
            start=1
        ):

            task.task_id = new_id

            new_tasks[new_id] = task

        self.tasks = new_tasks

    # ── Add task ───────────────────────────────────────────

    def add(self, title):

        title = title.strip()

        if not title:

            raise ValueError(
                "Title cannot be empty."
            )

        task_id = self._next_id()

        task = Task(
            task_id,
            title
        )

        # Add to Hash Map
        self.tasks[task_id] = task

        self._save()

        return task

    # ── Find task using Hash Map ───────────────────────────

    def _find(self, task_id):

        if task_id not in self.tasks:

            raise ValueError(
                f"No task with ID #{task_id}."
            )

        # O(1) average lookup
        return self.tasks[task_id]

    # ── Remove task ────────────────────────────────────────

    def remove(self, task_id):

        task = self._find(task_id)

        # Remove directly from Hash Map
        del self.tasks[task_id]

        # Shift remaining tasks up
        #
        # Example:
        # Before: {1: A, 2: B, 3: C}
        #
        # Remove #2
        #
        # After deletion: {1: A, 3: C}
        #
        # After reorder: {1: A, 2: C}

        self._reorder_tasks()

        self._save()

        return task

    # ── Mark task as done ──────────────────────────────────

    def mark_done(self, task_id):

        task = self._find(task_id)

        if task.done:

            raise ValueError(
                f"Task #{task_id} is already done."
            )

        task.done = True

        self._save()

        return task


# ── Helper Functions ───────────────────────────────────────

def get_int(prompt):

    while True:

        value = input(prompt).strip()

        if value.isdigit():

            return int(value)

        print(
            "Please enter a valid number."
        )


def show_tasks(tasks):

    print("\n" + "-" * 35)

    if not tasks:

        print("No tasks yet.")

    else:

        pending = [
            task
            for task in tasks.values()
            if not task.done
        ]

        completed = [
            task
            for task in tasks.values()
            if task.done
        ]

        if pending:

            print("\nPENDING")

            for task in pending:

                print(task)

        if completed:

            print("\nCOMPLETED")

            for task in completed:

                print(task)

    print("-" * 35)


# ── Main Program ───────────────────────────────────────────

def main():

    manager = TaskManager()

    print("=" * 35)
    print("      TO-DO LIST MANAGER")
    print("=" * 35)

    print(
        f"{len(manager.tasks)} task(s) loaded."
    )

    while True:

        print("\n1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")

        choice = get_int(
            "\nChoice (1-5): "
        )

        # ── View tasks ──────────────────────

        if choice == 1:

            show_tasks(
                manager.tasks
            )

        # ── Add task ─────────────────────────

        elif choice == 2:

            title = input(
                "Task title: "
            )

            try:

                task = manager.add(
                    title
                )

                print(
                    f"Added: {task}"
                )

            except ValueError as error:

                print(
                    f"Error: {error}"
                )

        # ── Mark task as done ─────────────────

        elif choice == 3:

            show_tasks(
                manager.tasks
            )

            task_id = get_int(
                "Enter task ID to mark done: "
            )

            try:

                task = manager.mark_done(
                    task_id
                )

                print(
                    f"Marked done: {task}"
                )

            except ValueError as error:

                print(
                    f"Error: {error}"
                )

        # ── Remove task ───────────────────────

        elif choice == 4:

            show_tasks(
                manager.tasks
            )

            task_id = get_int(
                "Enter task ID to remove: "
            )

            try:

                task = manager.remove(
                    task_id
                )

                print(
                    f"Removed: #{task.task_id} - "
                    f"{task.title}"
                )

            except ValueError as error:

                print(
                    f"Error: {error}"
                )

        # ── Exit ──────────────────────────────

        elif choice == 5:

            print(
                "\nGoodbye! Tasks saved to tasks.json"
            )

            break

        else:

            print(
                "Invalid choice. Enter 1-5."
            )


# ── Run Program ────────────────────────────────────────────

if __name__ == "__main__":

    main()
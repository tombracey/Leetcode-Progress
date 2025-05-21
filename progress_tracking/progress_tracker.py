import os
import json
from datetime import datetime

def count_problems():
    problem_count = 0
    for root, dirs, files in os.walk("problems"):
        problem_count += len(files)
    return problem_count

def append_to_json(count):
    today = datetime.today().strftime('%Y-%m-%d')
    entry = {"date": today, "total_solved": count}

    with open("progress_tracking/progress.json", "w") as f:
        data = json.load(f)
        data.append(entry)

if __name__ == "__main__":
    count = count_problems()
    append_to_json(count)
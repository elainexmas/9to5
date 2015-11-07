import time
import git as gp
from random import randint

def _modify_one_commit(commit):
    current_hour = time.localtime(commit.committed_date).tm_hour
    if current_hour > 17 or current_hour < 9:
        # pick random hour in 9am-5pm
        random_hour = randint(9, 17)
        diff = current_hour - random_hour
        commit.committed_date - diff*3600

    assert time.localtime(commit.committed_date).tm_hour >= 9 and time.localtime(commit.committed_date).tm_hour <= 17

    return commit

def fix_times(path, branch = "master"):
    # cd into the path of the repo
    repo = gp.repo(path)

    # grab last commit
    last_commit = repo.heads[branch].commit

    # make changes
    repo.heads[branch].commit = _modify_one_commit(last_commit)


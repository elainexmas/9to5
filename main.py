import argparse
import time
import git as gp
from random import randint

def _modify_one_commit(commit):
    copy = commit
    current_hour = time.localtime(copy.committed_date).tm_hour
    if current_hour > 17 or current_hour < 9:
        # pick random hour in 9am-5pm
        random_hour = randint(9, 17)
        diff = current_hour - random_hour
        copy.committed_date -= diff*3600

    assert time.localtime(copy.committed_date).tm_hour >= 9 and time.localtime(copy.committed_date).tm_hour <= 17
    return copy

def fix_times(path, branch = "master"):

    # create Repo object using path
    repo = gp.Repo(path)

    # make changes to a commit list
    [ _modify_one_commit(c) for c in repo.iter_commits(branch) ]


def main():
    parser = argparse.ArgumentParser("Modify git commit timestamps")
    parser.add_argument('path', type = str, help = 'path to repo')
    parser.add_argument('--branch', type = str, help = 'branch name', default = 'master')
    args = parser.parse_args()
    fix_times(args.path, args.branch)

if __name__ == "__main__":
    main()


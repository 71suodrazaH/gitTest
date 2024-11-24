
# gitTest
A set of steps and commands to get started with GIT
```
Git Test Project/
├── simulate.py
├── inputs/
│   └── test_vectors.txt
├── outputs/
│   └── results.txt
├── reference/
│   └── expected_results.txt
└── README.md
```
## FPGA Verification Project (Dummy project)

This project simulates a basic FPGA verification workflow:
1. Generates test vectors.
2. Simulates processing.
3. Compares output with expected results.

## Usage

Run the Python script:

1. Create a virtual environment and activate it.
2. Navigate to repo.
3. Run simulate.py script using:
```
python3 simulate.py
```

## Generating an SSH key

Follow the steps @ https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

a. To generate a new key

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

keep pressing enter for file name and passphrase.

## Git Commands

1. Clone directory

```
git clone <Clone link to repository>
```

2. Pushing code to Git

```
git add .
git commit -m "<Type you commit message within>"
git push
```

3. Pulling new code
```
git fetch
git pull
```

4. Create a new branch
```
git branch <new_branch_name>
```

5. Switch to a different branch

Before switching to a new branch ensure that there are no changes you made to you local branch. However, before you do that, note that if your working directory or staging area has uncommitted changes that conflict with the branch you’re checking out, Git won’t let you switch branches. It’s best to have a clean working state when you switch branches.
```
git status

```
If you made no changes, you're good to switch branch
```
git checkout -b <branch_name>
```

6. If you made changes to your local branch and still want to switch to a new branch you can either add and commit your changes or stash and change branch to basically give up all the changes made.

Here's how to stash and change branch (note: in this mehtod ):

```
git stash
git checkout -b <branch_name>
```

7. Undo Changes

a. Unstage changes

```
git reset <file>
```

b. Reset branch to a specific commit

```
git reset --hard <commit_hash>
```

8. Merge Branch

Let's assume that you would like to merge your "NewFeature" branch into the "Master" branch.
Here's how you can do it.
Note: Pay close attention to the order of the commands and branch names. Reversing the order would merge Master branch into NewFeature branch instead.

```
git checkout Master
git merge NewFeature
```

8. Delete Branch

You can delete the branch with the following command (if the branch is already pushed to the remote branch (github / bitbucket / etc.))
It might be a good idea to switch to a different branch before deleting.

```
git branch -d <name_of_branch_to_be_deleted>
```

Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.

## Requirements
- Python 3.x installed.
- No additional dependencies.

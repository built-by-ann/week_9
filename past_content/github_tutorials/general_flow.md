# Git Workflow: Working on a Project

Every time you work on a project, follow these steps to get the latest changes, work on your own branch, and save your progress to GitHub.

## Step 1: Pull the Latest Changes

Before starting your work, make sure you have the latest version of the project.

```bash
git switch main
git pull origin main
```

- `git switch main` switches to the main branch.
- `git pull origin main` downloads the latest changes from GitHub.

## Step 2: Switch to Your Own Branch

If you are creating your branch for the first time:

```bash
git switch -c your-name
```

If you already have a branch:

```bash
git switch your-name
git merge main
```

- `git switch` moves you to your branch.
- `git merge main` brings the latest updates from main into your branch.

**Important:** Do all your work on your own branch, not on `main`.

## Step 3: Make Your Changes

Now you can start coding!

- Open your files in VS Code.
- Make your changes.
- Save your files.
- Run your code to make sure everything works.

## Step 4: Add and Commit Your Changes

Once you've finished working, save your progress using Git.

```bash
git status
git add .
git commit -m "Describe what you changed"
```

- `git status` shows which files you changed.
- `git add .` prepares your changes to be saved.
- `git commit` creates a checkpoint of your work.

**Note:** Make sure private files like `.env` are excluded by `.gitignore` before using `git add .`.

Try to write a commit message that describes what you actually did.

For example:

```bash
git commit -m "Added reset command to chatbot"
```

## Step 5: Push Your Changes to GitHub

If this is your first time pushing your branch:

```bash
git push -u origin your-name
```

After that, you can simply use:

```bash
git push
```

This uploads your commits to GitHub.

---

## Quick Reference

**Pull → Branch → Code → Add → Commit → Push**

```bash
# 1. Get the latest changes
git switch main
git pull origin main

# 2. Switch to your branch
git switch your-name
git merge main

# 3. Make your changes in VS Code!

# 4. Save your changes
git status
git add .
git commit -m "Describe your changes"

# 5. Upload your changes
git push
```

### Important Reminders

- Always work on your own branch.
- Commit your changes regularly.
- Never commit API keys, passwords, or `.env` files.
- Make sure your work is committed before switching branches.
- If Git reports a merge conflict, ask for help before continuing.
- Remember: **Commit saves your work locally. Push uploads it to GitHub.**

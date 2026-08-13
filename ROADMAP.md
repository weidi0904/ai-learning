# ROADMAP

## Current Phase

- Initial repository setup for GitHub upload.

## Completed

- Added type annotations and basic type validation to `add` in `main.py`.

## In Progress

- Prepare local Git repository and connect it to GitHub.

## Todo

- Push the initial commit to `https://github.com/weidi0904/ai-learning.git` after confirmation.

## Blockers

- None.

## Recent Verification

- `python -c "from main import add; print(add(1, 2)); print(add(1.5, 2))"` passed.
- `python -c "from main import add; add('1', 2)"` raised the expected `TypeError`.


# Contributing 👫

## Following our standards with git hooks 🌲

In this repository, we're following some python/git conventions that all commits should follow:

* Since 05/04/2022 we're following
  the [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/) and all the pull requests
  that we merge should be in that format.
* Since 06/04/2022 we're following the [PEP8 python standard](https://peps.python.org/pep-0008/) with flake8 and black,
  and all the pull requests that we merge should be in that format.

For making it easier to work with this restrictions, we added git hooks for making sure that every commit follows this
standards. For installing the tools you should do:

```
cd .github
pip install -r dev-requirements.txt
npm install -g @commitlint/{config-conventional,cli}
pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```

And now you will be following the standard on each commit! 😇

## Issues 🚩

Issues are very valuable to this project.

- Ideas are a valuable source of contributions others can make
- Problems show where this project is lacking
- With a question you show where contributors can improve the user
  experience

Thank you for creating them.

## Pull Requests ❤️

Pull requests are, a great way to get your ideas into this repository.

When deciding if I merge in a pull request I look at the following
things:

### Does it state intent

You should be clear which problem you're trying to solve with your
contribution.

For example:

> feat(login): add css to login page

Doesn't tell me anything about why you're doing that

> feat(login): add css to login page because the current colors
> make a contrast that isn't easy to read.

Tells me the problem that you have found, and the pull request shows me
the action you have taken to solve it.

### Is it of good quality

- There are no spelling mistakes
- It reads well
- For english language contributions: Has a good score on
  [Grammarly](https://www.grammarly.com) or [Hemingway
  App](https://www.hemingwayapp.com/)

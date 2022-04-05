# Contributing 👫

## Install git hooks
In this repository, we're following some python/git conventions that all commits should follow:
 * Since 05/04/2022 we're following the [conventional commits specification](https://www.conventionalcommits.org/en/v1.0.0/) and all the pull requests that we merge should be in that format.
 * Since 06/04/2022 we're following the [PEP8 python standard](https://peps.python.org/pep-0008/) with flake8 and black, and all the pull requests that we merge should be in that format.
 
For making it easier to work with this restrictions, we added git hooks for making sure that every commit follows this standards. For installing the tools you should do:

```
    $ pip install -r dev-requirements.txt
    $ npm install -g @commitlint/{config-conventional,cli}
    $ pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```

And now you will be following the standard on each commit! 😇

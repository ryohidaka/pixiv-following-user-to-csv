# pixiv-following-user-to-csv

Output the list of following users on Pixiv to CSV.

## Overview

This is a Python project that uses [pixivpy](https://github.com/upbit/pixivpy) to get a list of users you are following and output it to a CSV file.

## Notes

pixivpy is an unofficial API client. Please use it at your own risk. We do not take any responsibility for any damages caused by the use of this tool. Please use it with the understanding of the above.

## Installation

### Install the dependency packages

```zsh
$ pip install -r requirements.txt
```

### Set environment variables

```zsh
$ cp .env.example .env
```

| Name            | Description                  | Example   |
| --------------- | ---------------------------- | --------- |
| `USER_ID`       | Your Pixiv ID for logging in | `0123456` |
| `REFRESH_TOKEN` | Refresh token for Pixiv      | `***_***` |

### Run

#### Diff Mode (default)

Gets a list of following users that are not recorded in the CSV file. This is faster than checking all users, because it does not check all users. The first time, it takes the same amount of time as the All mode.

```zsh
# Output "public" following users (default)
$ python pixiv-following-user-to-csv/main.py --restrict public --mode diff

# Output "private" following users
$ python pixiv-following-user-to-csv/main.py --restrict private --mode diff
```

#### All Mode (default)

This mode initializes the CSV file and then retrieves all following users. This takes time, but it allows you to reflect the deletion or update of users.

```zsh
# Output "public" following users (default)
$ python pixiv-following-user-to-csv/main.py --restrict public --mode all

# Output "private" following users
$ python pixiv-following-user-to-csv/main.py --restrict private --mode all
```

### Result

The CSV file will be output to the `/output` directory.

## Related

- [pixivpy](https://github.com/upbit/pixivpy)

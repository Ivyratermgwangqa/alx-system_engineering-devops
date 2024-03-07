# Reddit API Project

This project consists of Python scripts that interact with the Reddit API to perform various tasks such as fetching the number of subscribers, retrieving the top posts, and counting occurrences of specific keywords in hot articles.

## Task Descriptions

### 0. Number of Subscribers (0-subs.py)

This script queries the Reddit API and returns the number of subscribers for a given subreddit.

### 1. Top Ten (1-top_ten.py)

This script queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

### 2. Recurse it! (2-recurse.py)

This script implements a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

### 3. Count it! (100-count.py)

This script implements a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

## How to Run

To run each script, follow these steps:

1. Make sure you have Python 3 installed on your system.

2. Install the `requests` library if you haven't already:
   ```
   pip install requests
   ```

3. Navigate to the directory containing the script you want to run.

4. Run the script with Python, passing the required arguments if necessary. For example:
   ```
   python3 0-subs.py programming
   ```

   Replace `programming` with the subreddit you want to query.

## Requirements

- Python 3.4.3 or higher
- `requests` library
- Ubuntu 20.04 LTS (or compatible OS)

## Author

These scripts were written by [Lerato Mgwangqa].

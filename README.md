# Paintify Books

AI-generated art of scenes from books/ text

## Pre-requisites

* OpenAI API key.
* Twitter app: API key, API secret.
* Twitter account: this is the bot account that you will login with. Tweets will be posted on this account.

## Local Setup

Copy the `.env.sample` file into a file named `.env` and update the values of
* `OPENAI_API_KEY`
* `TWITTER_API_KEY`
* `TWITTER_API_SECRET`

Install dependencies:

```bash
cd /path/to/repo
poetry install
poetry install --with dev
```

## Run the script

Generate access tokens:

```bash
poetry run python auth.py
```

Copy the access token and secret printed on the screen into `.env` as the values of `TWITTER_BOT_ACCESS_TOKEN` and `TWITTER_BOT_ACCESS_SECRET`.

Run the script to generate and upload images:

```bash
poetry run python main.py
```

---

Find the PaintifyBooks bot on Twitter [@PaintifyBooks](https://twitter.com/PaintifyBooks). An experiment by [@pradeepcep](https://twitter.com/pradeepcep).

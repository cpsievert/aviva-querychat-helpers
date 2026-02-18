# Querychat helper template

A Shiny for Python dashboard that uses [querychat](https://github.com/posit-dev/querychat) to enable natural-language querying of the Titanic dataset.

## Setup

### Installation

Install via [uv](https://docs.astral.sh/uv/getting-started/installation/) and [venv](https://docs.python.org/3/library/venv.html):

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Credentials 

The app is set up to use OpenAI by default for response generation. 

Therefore, you'll need an `OPENAI_API_KEY` environment variable set for the app to work as expected.

```shell
export OPENAI_API_KEY="<your_key_here>"
```

To learn more about how to use different providers (e.g., Anthropic, Snowflake, etc) and manage credentials, see:

https://posit-dev.github.io/querychat/py/models.html


## Run the app

Once you've installed and set up your credentials correctly, you can run the Shiny app from the command line:

```bash
shiny run --reload app.py
```

Then open <http://localhost:8000> in your browser.

## Custom data sources

QueryChat has rich support for different types of data sources such as polars, ibis, sqlalchemy, etc. 

See here to learn more https://posit-dev.github.io/querychat/py/data-sources.html


## Further learning

- More shiny examples: https://posit-dev.github.io/querychat/py/build.html
- In-depth blogpost: https://shiny.posit.co/blog/posts/querychat-python-r/
- Connect to Snowflake: https://github.com/sol-eng/snowflake_demo/tree/main/apps/shiny-python-querychat
- Main querychat website (R & Python): https://posit-dev.github.io/querychat/

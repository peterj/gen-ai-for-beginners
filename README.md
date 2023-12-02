# Generative AI for beginners

This repo contains examples from the [Generative AI for beginners course](https://github.com/microsoft/generative-ai-for-beginners) I went through in 3 YouTube live streams:

1. [Part 1: Generative AI for beginners](https://www.youtube.com/watch?v=Irk9ANcurbM&list=PLy0Gle4XyvbFyFCv73X1BTKKWM98uCGRf&index=2&t=1s)
2. [Part 2: Generative AI for beginners](https://www.youtube.com/watch?v=PHMq-pFjMOM&list=PLy0Gle4XyvbFyFCv73X1BTKKWM98uCGRf&index=2)
3. [Part 3: Generative AI for beginners](https://www.youtube.com/watch?v=eZEqZxhZTGk&list=PLy0Gle4XyvbFyFCv73X1BTKKWM98uCGRf&index=3)

## Prerequisites

You'll need OpenAI API key - you can set it as an environment varaible (`OPENAI_API_KEY`) before running the scripts or create a `.env` file and add the API key there.

You'll also need Python - I was using Python 3.11.6. There will be other requirements such as `openai`, `numpy`, `pyyaml`, `requests`, `dotenv`, and others, but you can install them with `pip install <library name>`.

## Running the scripts

You can run the scripts with `python <script name>`. The scripts are:

- `embed.py` - shows how to create embeddings from text and use cosine similarity to compare one embedding with another one.

- `funcs.py` - shows how to define tools (functions) and pass them to the chat completion call. OpenAI can then extract the needed information (function arguments) from the prompt, so you can invoke the function.

- `imagegen.py` - shows how to use Dall-E 3 to generate images from prompts, how to do image editing (i.e. you have to provide an input image with transparent areas that Dall-E can fill out), and how to create image variants (i.e. you can provide an input image and Dall-E creates a variant of that image).

- `textgen.py` - shows the chat/completions API and how to use it to generate text from prompts.

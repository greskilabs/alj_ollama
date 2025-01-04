# alj_ollama Repository

Create a local Ollama chat agent and access it through a Python script.

## Required Components

The local agent requires a local installation of [Ollama](https://ollama.com), the python libraries `langchain`, 
`langchain-ollama` and `ollama`.

## Setup 

1. From a web browser, navigate to [Ollama.com](https://ollama.com) and download the version of Ollama that is appropriate for your operating system.<br>
2. From your operating system, run the downloaded install executable to install the Ollama engine on your computer.<br>
3. From a terminal window on the local computer, run Ollama to have it download a model file: e.g. `run ollama ollama3.2` which will start Ollama and download a 2Gb model file. Verify the installation by asking Ollama a question, such as "what is democracy?" <br>
4. Exit Ollama with the `/bye` command. <br>
5. Login to [Github](https://github.com) and fork the [greskilabs/alj_ollama]() Github repository to your Github account so you can edit the Python script.<br>
6. Clone the Github repository to your local computer. <br>
7. Start your Python IDE, edit the `myOllamaLocal.py` script, and run the script to activate the Ollama bot. 

## Notes

A list of commands that are valid for the terminal interface for Ollama is accessible via the `/?` or `/help` command.<br><br>
The Ollama Model Library, including parameter counts and file sizes is accessible from the [Ollama Github README](https://github.com/ollama/ollama?tab=readme-ov-file#model-library). <br><br>

The Python script can only access models that have already been downloaded to the local computer via the `ollama pull` command. 


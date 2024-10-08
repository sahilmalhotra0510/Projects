[Location Projects for OpenWebUI](../)

# Open WebUI Setup

<!--Pinecone -->

View our **[Quick local setup without Docker](guides)**. More detailed steps below.

If you already have an "open-webui" Docker container, your OpenWebUI server may already be running at [localhost:3000](http://localhost:3000) (since Docker restarts it when you start your computer). You can now [train with a web page](train).

Alternatively, use the local [Docker Setup](docker) for an even quicker install using Ollama to load models. The page also includes experiments in which we extract backend files to edit in a Webroot. We're not sure if the pre-build frontend files can reside in the Docker container images.

Our [Google Cloud deployment notes](google-cloud) - includes cost comparison.
<br>

# Install for Building Locally (without Docker)

### Use our conda-start.sh script to install with one step for Linux/MacOS

These steps are for programmers planning to edit and build locally. Visit [localhost:8080](http://localhost:8080) if you've already install.  
After the initial one hour or more install, it only takes a minute to restart the server using the same conda-start.sh command below.

If you machine needs updates, our [node, python and conda upgrade page](https://model.earth/io/coders/python) is helpful.  
If you're not planning to edit, you can install faster using a [local Docker instance](docker).

You can use GitHub Desktop to pull [our fork](https://github.com/earthscape/open-webui-earthscape/) to your computer, or you can clone with a command:

<!--
    git clone https://github.com/modelearth/projects.git
    cd projects/
-->

    git clone https://github.com/earthscape/open-webui-earthscape.git
    cd open-webui-earthscape

Check that you have cmd apps available, including a 3.11 version of python.

    conda --version
    python3.11 --version
    node --version
    npm --version

You can add python 3.11 without reverting your current version.
See the [pyenv install links](/io/coders/python/) on our python notes page, then run:

    pyenv install 3.11
    pyenv local 3.11

**On Windows**
You can run the "start.bat" steps on [Open WebUI Getting Started](https://docs.openwebui.com/getting-started/). We've documented how to deploy the [Windows steps with conda](guides)

**On Mac and Linux**
Run the following in the root of the "projects" folder. Our [conda-start.sh](https://github.com/ModelEarth/projects/blob/main/location/setup/script/conda-start.sh) script invokes python3.11 so you might need [pyenv](https://model.earth/io/coders/python).
bash location/setup/script/conda-start.sh

That's it. Wait an hour or two to finish, then view the site here:

[http://localhost:8080](http://localhost:8080)

## Run a local Build

Now you can build to apply changes from "src" and "backup".

    npm run build

"npm run build" seems to break secure https 0.0.0.0:8080 hosting.  
(Perhaps because the test included the external localsite.js file.)

<b><span style="color:red">Don't use</span></b> `npm run dev` it only hosts the frontend and you'll get a message that the backend did not build.  
Instead, use `npm run format:backend` &nbsp;(More info below in "Building Branches Locally")<!-- need to confirm that works -->

### Related Notes

As of July 2024, OpenWebUI has issues with python 3.12, so we use python 3.11 in conda-start.sh. Here are our notes of checking [your local python version and install nvm](../../../io/coders/python/) to host multiple version of python.

Check that you have npm installed. If not, [install node project manager](../../../io/coders/python/)

    npm -v

View a list of your conda environments.
If none are found, [download from Anaconda.com](https://www.anaconda.com/download)

    conda env list

The conda-start.sh script uses commands from [Open WebUI Getting Started](https://docs.openwebui.com/getting-started/) for building locally.

The commands include the following - also [see with Conda](guides)

    # Building Frontend Using Node
    npm i
    npm run build

    # Serving Frontend with the Backend
    cd ./backend
    pip install -r requirements.txt -U

    bash start.sh

We created conda-start.sh because `bash start.sh` above fails when Llama is not available - since it uses the settings config file.  
On Windows, run `start.bat` for the last line above.

Our conda-start.sh runs the backend in a virtual environment.  
You could optionally run the following first too. We haven't confirmed the install works when running this first. [Get pyenv](/io/coders/python/)

    pyenv install 3.11
    pyenv local 3.11
    python3.11 -m venv env
    source env/bin/activate

On windows the last line above is `.\env\Scripts\activate`

<!--
### RAM error when running Ollama on a 5-year old Mac

A RAM error shut down the local site: [1 leaked semaphore](https://github.com/lllyasviel/Fooocus/discussions/2690)
The CPU was not running hot when this occurred.
-->

<!--
The following restarted the frontend at [localhost:5173](http://localhost:5173/)
After a couple minutes you'll see "Open WebUI Backend Required"

	npm run dev
-->
<!--
Running the pre-existing bash start.sh results in:

Loading WEBUI_SECRET_KEY from file, not provided as an environment variable.
Loading WEBUI_SECRET_KEY from .webui_secret_key
start.sh: line 23: ${USE_OLLAMA_DOCKER,,}: bad substitution
start.sh: line 25: ${USE_CUDA_DOCKER,,}: bad substitution
start.sh: line 52: exec: uvicorn: not found

Is there a fast way to reopen the conda instance?
-->

**Starting your server**

Restarting the server only takes a couple minutes. Use the same command as above (Mac).  
Choose the existing conda environment by saying "no" when asked to reinstall.

Mac/Linux:

    bash location/setup/script/conda-start.sh

Windows (not yet confirmed):

    start.bat

More [documentation on building locally](https://docs.openwebui.com/getting-started/)

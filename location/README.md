[Active Projects](../)

# Open WebUI - Location Projects

[Our Google Cloud experiments](setup/google-cloud) aim to use only API pipelines so we can avoid CPU use locally.

If you're contributing code, here are our steps to [install and build locally](setup/guides) and [more detailed setup notes](setup).  
Work in the "modelearthbranch" so the version number does not need to be incremented.  
If you're NOT contributing code while building locally, use the faster [local Docker install](setup/docker) instead.  

To build and contribute locally, you'll skip the local Docker install. Fork one of our forks:

**“Actions” tabs from our two forks:** 
A. [datascape/open-webui](https://github.com/datascape/open-webui/actions) - Fresh fork, the least broken<!-- (source of [workflow PR](https://github.com/ModelEarth/projects/pull/7) also applied to projects repo)-->  
B. [earthscape/open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape/actions) - A little broken


## Contribute in our Open WebUI "projects/location" folder

Our [customize.py script](setup/customize) is used to add our custom code.
Our [sync.py script](setup/customize) removes custom code so we can sync with the parent.

To avoid merge errors, if you're making updates in the "src" and "backend" folders,
append "-team" to the names of the files you've copied and customized.


TO DO: The html we added in this "projects" fork is breaking the GitHub Docker build.  
Instead try simple edits in our [open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape) fork. (Write loren to be added as a contributor.)

## Our OpenWebUI Projects

For both Datascape and Earthscape, clicking the initial Docker build in Actions was successful.  
Maybe because nothing had changed yet, so it didn't run a memory-consuming build of Ollama.

TO DO: Try using the techniques in “Building Branches Locally” below to eliminate the Actions tab errors.

TO DO: Figure out how to load localsite.js within our clean [Datascape fork](https://github.com/datascape/open-webui/) without generating these [Github Action errors](https://github.com/datascape/open-webui/actions)

    <script type="text/javascript" src="https://model.earth/localsite/js/localsite.js?showheader=true&showsearch=true"></script>

TO DO: Use Flask in a [projects/backend/location](https://github.com/ModelEarth/projects/tree/main/backend) folder and interact with our Supabase REST API - Nanden

TO DO: Create an example of running [Run-Models-bkup.ipynb](https://github.com/ModelEarth/RealityStream/tree/main/models) saved from our [RealityStream CoLab](../../RealityStream/).

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [Supabase International Trade Flow](../../OpenFootprint/prep/sql/supabase/) data.

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [superthermal evaporation](../../evaporation-kits/) page and related articles.

<!--TO DO: Activate hosting using Cloudflare.-->

TO DO: Provide a means to upload a list of members from a Google Sheet link.

DONE: Provide a button for admins to export the list of members as a CSV file. (In [ModelEarthBranch](https://github.com/ModelEarth/projects/tree/ModelEarthBranch)) - Yuxin

TO DO: Update our Readme in localsite.js to one that supports [NOTE], [WARNING], [TIP]


[Install for Building Locally](setup)

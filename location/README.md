[Active Projects](../)

# Location Projects for Open WebUI

GETTING STARTED

If you're contributing code, use our [Install for Building Locally](setup) steps.  
To build locally, you'll skip the local Docker install. Fork our [projects](https://github.com/ModelEarth/projects/) repo, which is a fork of open-webui.
[Install and Build Locally](setup/guides) (or [detailed steps](setup)) and view [Our Google Cloud deployment](setup/google-cloud)  

If you're NOT contributing code while building locally, use the faster [local Docker install](setup/docker) instead.


## Contribute in our Open WebUI "projects/location" folder

The "projects/location" folder is where we add extras - we're still perfecting [building locally for deployment](setup).  

To avoid merge errors, if you're making updates in the "src" and "backend" folders,
append "-team" to the names of the files you've copied and customized.
Update our [setup customization](setup/customize) to add and remove code to support our mods.

TO DO: The html we added in this "projects" fork is breaking the GitHub Docker build.  
Instead try simple edits in our [open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape) fork. (Write loren to be added as a contributor.)

## Our OpenWebUI Projects

**“Actions” tabs from our three forks:**
A. [modelearth/projects](https://github.com/ModelEarth/projects/actions) - Massively broken (our repo for documentation)  
B. [earthscape/open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape/actions) - Fresh fork, a little broken
C. [datascape/open-webui](https://github.com/datascape/open-webui/actions) - Fresh fork, the least broken (source of [workflow PR](https://github.com/ModelEarth/projects/pull/7) also applied to projects repo)

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

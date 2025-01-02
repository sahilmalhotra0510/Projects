
<!--
medium.com subscription needed

	How to install Open WebUI without Docker
	https://bhavikjikadara.medium.com/how-to-install-open-webui-without-docker-33eedbda9b96
-->


<!--
- [Observable Data Commons](/data-commons/) - [Open WebUI](location/) - [Storyboard Generator](/data-pipeline/research) - [Moonshots](/community/projects/)
-->

<!--
**Timely Projects**

- [Activate Ollama on a different server](https://docs.openwebui.com/) for use with our [Docker Setup](/projects/location/setup/docker/)


	Full-Stack Cloudflare SaaS kit
	https://github.com/Dhravya/cloudflare-saas-stack


Create a developer account in [Omdena.com](https://omdena.com) and help us create [team panels](/panels) using the 

- [Document adding Flask as our optional python webroot](../localsite/start/steps/)
-->

# Active Projects

Our weekly meetup are every [Thursday at 7pm ET](/io/coders/).

Select an area of interest and choose a TO DO to contribute. Add your first name below and [send a PR](https://github.com/ModelEarth/projects/blob/main/active.md).

Also [install related repos locally](../localsite/start/steps/). 


## Everybody's Home Page

[For Everybody's Home Page](../home) we'll be pulling GitHub image feeds into [our FeedPlayer](https://model.earth/feed).

TO DO: Add a field called #gitrepo on our [home repo dev page](../home/repo) for pasting a Github account and repo name.  

Set the default repo to: [https://github.com/modelearth/requests](https://github.com/modelearth/requests)

Include an alert if the URL does not contain github.com (or another git provider), an account and a repo name.  

## Planet Javascript AI

TO DO: Using [Langchain's Chat Model Interface](https://python.langchain.com/docs/concepts/chat_models/), send a page from any repo to an AI API like OpenAI.

Add the javascript to our [Planet repo](https://github.com/modelearth/planet/) to provide Retrieval Augmented Generation (RAG) using [LangChain.js](https://api.js.langchain.com) javascript. 

Integrate [our API storage in javascript](/localsite/tools/storage/api/) to store API keys locally.

<!--See also: DataStax Astra DB-->

## Langchain Python

TO DO: Move Python Langchain into main branch

[Our Python Langchain Repo](https://github.com/modelearth/langchain/) <!--Dhananjay and Pranathi  -->

**Python Retrieval Augmented Generation (RAG)**
[Conversational RAG for 10 LLMs](https://python.langchain.com/docs/tutorials/qa_chat_history/) - Pradeep and Pranoy  

Pradeep: Pinecone on AWS free 2 GB max
Pranoy: DocArray in memory Vecto Store (database)

[Google Notebook LM](https://notebooklm.google)

We can also [remove LangChain to simplify](https://www.octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents)

Content prep for RAG: [Innovations in Water Purification](/evaporation-kits/innovations/) - Hyper Desalination

**Retrieval-Interleaved Generation (RIG)**  
Using [Google Data Commons DataGemma AI](https://ai.google.dev/gemma/docs/datagemma) - For RIG, Zihan found that a paid Google plan was needed to avoid storage/memory errors/timeouts. Here's our [RIG CoLab](https://colab.research.google.com/drive/1eLtHOR6e3lAUVijUJ56VMaiTU6hA9enc?usp=sharing).



## RealityStream ML

[Run Models Colab](/RealityStream/)

TO DO: Send URL hash # parameters to our [Run Models CoLab](/RealityStream) using a [webhook on Google Cloud (ChatGPT)](https://chatgpt.com/share/670e7002-85fc-8003-a466-9b682012f3ea) - Abhishek L

**Anvil with our CoLabs:**
[Anvil Extras](https://anvil-extras.readthedocs.io/en/latest/guides/index.html) and [Anvil](https://anvil.works/learn/tutorials/data-science#connecting-notebooks) and [AnvilScope CoLab](https://colab.research.google.com/drive/1rlOPfOxRnfm4pTGSn3gk_MvmVF65iidF?usp=sharing) using Plotly - Soham


<!--
- [StreamLit hosting within Open WebUI](https://github.com/streamlit/streamlit/issues/969)
-->

## Google Data Commons Timelines

IN PROGRESS: [Javascript Timelines from Google Data Commons API](/data-commons/docs/data/) - Priyanka, Mehul, Aishwrya, Vishnupriya
IN PROGRESS: [Python pull from Google Data Commons API](/data-commons/docs/data/) - Zihan, Bhavna and Abhishek L. for our [Location Map Filters](/localsite/info/data/map-filters/)

<!--
**More Data Commons Visualization Projects**
[Observable with Data Commons](/data-commons/) - [Data Loaders How-To](/data-commons/dist/air/)

[Python CoLabs for GDC timeline automation - Air and Climate](/data-commons/dist/air)

[Kargil's notes](https://github.com/modelearth/Observables-DataLoader/tree/master/docs)

[Observable Framework Dashboard for UN Goals](https://observablehq.com/framework/) - with our .csv timelines and DuckDB Parquet impact files

TO DO: [Hosting DataCommons locally with Flask](/localsite/info/data/datacommons) - Vishnupriya and our GDC team
-->

## International Trade Flow

TO DO: Processing Exiobase in CoLabs, displaying with javascript

Contributors: Gary, Satya, Himanshu, Sahil

[International Trade Flow SQL Data Prep](/OpenFootprint/trade) - Exiobase Colab and charts

[Our little trade flow Sankey](/OpenFootprint/trade/) - [Big Sankey](https://sankey.theshiftproject.org/) - [Our Fork with python 3.10](https://github.com/ModelEarth/Mapping-global-ghg-emissions) and [bug resolved](https://github.com/baptiste-an/Mapping-global-ghg-emissions/issues/2)

TO DO: [Chord Chart Data Prep](/io/charts/chord/) <!-- Poorna and everyone interested -->

TO DO: [Python to pull Harmonized Code (HS) lookups into Supabase](/OpenFootprint/harmonized-system/) - Initial work by Wenjie (and Chen)

TO DO: [Sankey Industry eChart](/OpenFootprint/charts/echarts/sankey-nodeAlign-left.html) - eCharts uses a common echarts.min.js file which we'll load in [Feed Viewer](/feed/view)

TO DO: [Python - Finalize our All the Places data by State and Zip](/places)

## Exiobase and Flask

For our [International Trade Flow](/openfootprint/trade/) we can integrate our [Exiobase-Global-Trade GitHub Repo](https://github.com/modelearth/exiobase-global-trade) and a new [Comtrade API pull](https://github.com/ModelEarth/exiobase-global-trade/tree/main/comtrade)

## US EPA State Impacts

TO DO: Pull into SQL DuckDB

[Javascript updates for US EPA impact reports](/useeio.js/footprint/)  
[React Team - Mosaic column checkboxes](/io/charts)  
[React Team - Commodity Totals](/localsite/info/data/totals/) in [Jobs Reports](/localsite/info/#indicators=JOBS)
[Impact Label Pipeline](/apps/impact) - Starting point for duplicating US EPA RStudio in python

## Open Footprints YAML Display

[Open Footprints](/food/) - [Product Impact API](/OpenFootprint/products/), Add javascript tp [Feed View](/feed/view/)  

[Food Nutrition Labels](/data-commons/docs/food) - Shali and Wenwei (Stella)

**BuildingTransparency and Open Footprint labels**

Bhavna, Yash

- [Use our state map filter](#geoview=country) with colors for [new USEEIO reporting maps](https://figshare.com/collections/USEEIO_State_Models_v1_0_-_Supporting_Figures/7041473)
- [BuildingTransparency - Product Impact Profiles by State and Zip](/io/template/feed/) - TO DO <!--Ronan-->
- [BuildingTransparency - API Aggregates of States and Countries](/io/template/product/) - Initially Luwei
- [BuildingTransparency - JSON file pull for impact templates](/io/template/product/)


## OpenWebUI LLM Location Data

IN PROGRESS - Dhananjay

[OpenWebUI](/projects/location/setup/customize/) - Reactivates Ollama for Sync, Docker and location addons

[Open WebUI (Projects)](location/) with Python and [Retrieval Augmented Generation (RAG)](https://docs.openwebui.com/tutorial/rag/)
for "context window" recency<!-- Next: Text to Action / Nividia Kuda is their advantage = code library that interacts with chip -->

[Earthscape NextJS Chatbot UI](/earthscape/app/) - React, Supabase and [NextJS Hosting using GitHub Pages](https://www.freecodecamp.org/news/how-to-deploy-next-js-app-to-github-pages/)

[Add localsite.js to OpenWebUI](/projects/location/) - Use our [Building Branches Locally](/projects/location/setup/) techniques within our [Datascape fork](https://github.com/datascape/open-webui/actions)



## Team Tools

- [Building and documenting webhook](/webhook) - Sends Word Doc from Google Form  - Arnab
- [Discord API](https://discord.com/developers/docs/intro) - Team bios in our Feed Player  
- Odoo on Google Cloud for [Modules and Templates](https://www.odoo.com/documentation/master/developer/tutorials/website.html) and [Owl](https://www.cybrosys.com/blog/an-overview-of-the-owl-component-lifecycle) with the [Owl Github repo](https://github.com/odoo/owl)


## Feed Player React

- [Feed Player](../feed/dist) - Video and Images from API feeds and Google Sheet lists
- [NASA Feed Viewer](../feed/view/#feed=nasa) - JSON, YAML, CSS, RSS - [Address Lookup](/feed/view/#feed=311)
- [Feed Player Visuals initially](/feed/dist/) - Restore display of BigBunny images and video, or show NASA images.

<!--
- [Add Datawrapper.de](https://www.datawrapper.de/) using "link external dataset"

- [Pull from Supabase (or backup file) into databricks SQL](https://chatgpt.com/share/d610d3e6-ce5f-4e7f-ba9e-4c74ec23abd4) - Apurva, Soham
- [View DuckDB from Javascript](/OpenFootprint/prep/sql/duckdb/) - Kelly, Gary
-->



<!--
- [Datausa.io](https://datausa.io) - Add API and embeddable visualizations to Feed Player
- [Restack.io](https://www.restack.io/docs/supabase-knowledge-supabase-rust-sdk-guide) - for Supabase with Rust and Streamlit


openai
Docker path: https://chat.openai.com/share/61b0997f-ea9b-49f7-9bcb-12fa0519a2d1

Matthew Berman list of true Agents:
https://youtu.be/_AOA6M9Ta2I?si=Bh8SMhyD3GmuCLks&t=378


CSV Files to use for Timelines, Observable, and AI Training at: [industries/naics/US/counties](https://github.com/ModelEarth/community-data/tree/master/industries/naics/US/counties)
Pre-processed data for county industry levels, based on employment, establishments and payroll.-->

## ML with Python and Google Data Commons

- [RealityStream](/RealityStream/) - Machine Learning Classification Models - Ivy, Kelvin and many more - TO DO
- [Process Industry NAICS by Zip Code](/community-zipcodes/mail) - DONE Yunbo
- [ML for Community Forecasting Timelines](../data-pipeline/timelines/) - Zip code pipeline TO DO
- [Open Data Panels - YAML Display](/OpenFootprint) - Microsoft Plug and Play - TO DO

- [Top Commodities by State (hide sort columns)](/data-pipeline/research/economy) - Dinesh
- [State Regions using Sets of Counties](/community-data/us/edd/) - Dinesh
- [USEEIO matrix files with clustering](/machine-learning/python/cluster/) - <!--Honglin-->Rupesh

<!--
- [CrewAI+Ollama integration](https://lightning.ai/lightning-ai/studios/ai-agents-powered-by-crewai) within our [Open WebUI fork](location)
- [Flowsa RStudio - API to JSON](/localsite/info/data/flowsa/)
-->

- [Update Farm Fresh Data pull](/community-data/process/python/farmfresh/) - Bhavna - DONE
- [Push EPA date to Google Data Commons API](https://docs.datacommons.org/api/)

## Storyboard Generator

Images and Videos from .CSV prompts 
for Interactive presentation backgrounds, Request Visualization

- [AI Requests Visualization](/requests/) - for Storyboards, Meal Planning and Project Visualization  
- [Music for Data Science](https://github.com/DreamStudioCode/music) - for [home/repo](/home/repo)

- [Image Gallery (JQuery) and Video (Leonardo)](/data-pipeline/research/stream)
- [Our Storyboard Generator](/data-pipeline/research/)
- [Open Webui image generation](https://docs.openwebui.com/tutorial/images/) - Integrate our image .csv process
  <!-- [Kishor's Repo](https://github.com/mannurkishorreddy/streamlit-replicate-img-app)-->
  <!--- [Image Gallery (React)](/react-gallery/view/) - Anthony -->


## Tabulator, Industry Timelines, SQLite in Browser

- [Tabulator - Merge in industry year rows using Javascript (1-3)](/data-pipeline/timelines/tabulator/) - DONE<!--Rupesh, Vadlamudi-->
- [Tabulator - Merge in titles using Javascript (4)](/data-pipeline/timelines/tabulator/) - DONE <!--Dinesh, Fanyi, Rupesh-->
- [Steps for SQLite in Browser](/data-pipeline/timelines/sqlite/phiresky/) - [Example (Runs SQL)](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)


<!-- - [React Team - Impact Side Navigation](/io/charts/inflow-outflow/#set=prosperity&indicators=VADD,JOBS) -->

## Moonshot Challenges

Our most challenging projects - [Take the leap](/community/projects/)
<br>

<div id="activeDivLoaded"></div>

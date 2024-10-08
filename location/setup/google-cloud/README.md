[Setup](../)
# Google Cloud Guide

We opted for Hosting with Pipeline Features (#2)

You can turn off a project to save costs. Add a [lien to prevent deletion after 30 days](https://cloud.google.com/resource-manager/docs/project-liens#:~:text=To%20place%20a%20lien%20on,See%20more%20code%20actions.&text=Replace%20the%20following%3A,project%20the%20lien%20applies%20to.).

<!--
This was our url prior to turning off.  It didn't work after turning back on.
[test-me-open-webui...](https://test-me-open-webui-oqhgx572oq-uc.a.run.app/auth/)
-->

#### Turn on a lien so you can deactivate a project for more than a month

You might need to fist created an API key for the above to work. (try skipping)
https://console.cloud.google.com/apis/credentials?project=openwebui-projects1

To turn on the lien, use the online Google cloud SDK shell to enable the cloud resource manage API access:

    gcloud services enable cloudresourcemanager.googleapis.com

Then create the lien with. Your role will need to have create lien permission.

    gcloud alpha resource-manager liens create \
      --project="openwebui-projects1" \
      --restrictions="resourcemanager.projects.delete" \
      --reason="On-Hold" \
      --origin="my-lien"

Check the lien list to confirm it's beed added:

    gcloud alpha resource-manager liens list


<!-- Turn off with "Shut Down" under Settings
https://console.cloud.google.com/iam-admin/settings?authuser=2&project=openfootprint
-->

## Cost Comparison and Deployment Steps

1. Hosting Ollama and Open WebUI together.
   ![image](./pics/gce-wOllama-cost.png)

2. Hosting with [pipeline](https://docs.openwebui.com/pipelines/) features. This allows the application connecting to external model apis other than OpenAI and Ollama. It requires the developers to build pipeline themselves. See [example](https://github.com/open-webui/pipelines/tree/main/examples/pipelines). Additional API fees might apply based on the provider.

    Since Ollama is increases the cost unnecessarily when installed with external pipelines, we're preparing 
    [customize.py](../customize) to comment out Ollama, and sync.py to restore Olama.

    ![Alt text](./pics/gce-wPipelines-cost.png)

3. Hosting with OpenAI API endpoints only. Cost should be similar to above. Additional API fees might apply based on the provider.

## Deployment on GCR (cloud run)

### Step 1: Upload Docker image container to Google Artifact Registry

The open-webui, open-webui-pipeline and modelearth-open-webui images are already uploaded to the org's registry. If you are interested how to do it, you could check out this [guide](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).

#### Reference Steps

1. Open the **Repositories** page in the [Google Cloud console](https://console.cloud.google.com/welcome?project=openwebui-projects1&authuser=2).

[Open the Repositoies page](https://console.cloud.google.com/artifacts) - You will enable "Artifact Registry API"
2. Click Create Repository
3. Specify `open-webui` as the repo name
4. Choose **Docker** as the format and **Standard** as mode
5. Choose **Region** as the Location Type and **us-central1** as the location
6. Click Create
7. Open Google Cloud Shell. Config it correctly. Checkout gcloud config documentation if needed.
8. Run the following:

   ```shell
   gcloud auth configure-docker us-central1-docker.pkg.dev
   docker pull ghcr.io/open-webui/open-webui:main
   docker images # check image id
   docker tag 79aef8c7e645 us-central1-docker.pkg.dev/openwebui-projects1/open-webui/open-webui-image:0.1
   docker push us-central1-docker.pkg.dev/[PROJECT_ID]/open-webui/open-webui-image:0.1
   ```

Repeat the step for pipeline images.

### Step 2: GCR

1.) Grant Cloud Run Developer, Service Account User, Artifact Registry Reader, Artifact Registry Writer IAM roles:

&nbsp;&nbsp;&nbsp;<img src="pics/gcr-roles.png" style="max-width:600px">
&nbsp;&nbsp;&nbsp;<img src="pics/artifact-roles.png" style="max-width:600px">

2.) Follow [Deploying a service with sidecar containers](https://cloud.google.com/run/docs/deploying#sidecars).

3.) Mount volume to the container

&nbsp;&nbsp;&nbsp;&nbsp;A. Under Container(s), Volumes, Networking, Security, select VOLUMES, ADD VOLUME
&nbsp;&nbsp;&nbsp;&nbsp;<img src="pics/gcr-add-volume.png" style="max-width:600px">
&nbsp;&nbsp;&nbsp;&nbsp;B. create new volume and then go to Containers Tab
&nbsp;&nbsp;&nbsp;&nbsp;<img src="pics/gcr-new-volume.png" style="max-width:600px">
&nbsp;&nbsp;&nbsp;&nbsp;C. Under Volume Mounts:
&nbsp;&nbsp;&nbsp;&nbsp;<img src="pics/gcr-vmount.png" style="max-width:600px">

&nbsp;&nbsp;&nbsp;&nbsp;For the pipeline image, change the **mount path** to `app/pipelines`.

4.) Then follow [Adding Pipelines Features](https://docs.openwebui.com/pipelines/) steps.

5.) You're good to go!

<!-- ## Deployment on GKE

A quick start [guide](https://www.youtube.com/watch?v=vIKy3pDz3jM) for a toy project.

## Deployment on GCE

1. Create an instance on GCE. Disk storage set to `40GB`
2. ssh the VM instance just created
3. make a working directory `mkdir webui-projects` and navigate to it `cd webui-projects`

**The following steps are for Ollama installation. You should alter it to suit your needs.**
4. pull Ollama by

    sudo bash
    curl -fsSL https://ollama.com/install.sh | sh


5. test if Ollama is intalled and start

    ```bash
    service ollama start
    ollama list
    ```

6. install a preferred model from Ollama

    ```bash
    ollama run mistral
    ```

1. Follow [Create Your Project](https://cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project) till Step 5
2. Run the following in your terminal

    ```bash
    gcloud config configurations create [CONFIG_NAME] --activate
    gcloud config configurations list # check if its created
    gcloud config set project [PROJECT_ID]
    gcloud config set account [YOUR_ACCOUNT]
    gcloud auth login
    gcloud config configurations list # check if the setting is correct
    gcloud app create
    ``` -->

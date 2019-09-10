# Serverless deployment using Azure Functions

#### Prerequisites

- [Install latest functions core tools](https://github.com/Azure/azure-functions-core-tools)
    - `npm i -g azure-functions-core-tools --unsafe-perm true`

- Create Azure Function App
    - Linux | Python | Dedicated Plan

- Create Azure SignalR Service
    - Free Tier

#### Steps

- Create Function App Locally

    - `func init --worker-runtime python`

    - `func new --template AzureQueueStorageTrigger --name classifyimage`

- Install Azure SignalR extension

    - `func extensions install -p Microsoft.Azure.WebJobs.Extensions.SignalRService -v 1.0.0`

- Install Python packages after updating the requirements file

    - `pip install --no-cache-dir -r requirements.txt`

- Start Debugging Locally

    - `func start`

    - Add a new message in storage queue with the url of the image

- Setup SignalR Service in Serverless Mode as per the [documentation](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-concept-serverless-development-config) or see sample negotiate function in this repo.

- Deploy Function App to Azure

    - Add the App Settings for `AzureSignalRConnectionString`

    - `func azure functionapp publish <FUNCTION_APP_NAME> -b remote`

- [Deploy Status Page as Static website on Azure Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host)

- [Enable CORS on Azure Function App](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-concept-serverless-development-config#azure-functions-configuration)

    - `az resource update --name web --resource-group MLFunctionTrials --namespace Microsoft.Web --resource-type config --parent sites/<FUNCTION_APP_NAME> --set properties.cors.allowedOrigins="['https://<STORAGE-ACCOUNT-NAME>.z22.web.core.windows.net']" --set properties.cors.supportCredentials=true`


# Additional Resources

- [Azure Functions development and configuration with Azure SignalR Service](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-concept-serverless-development-config#azure-functions-configuration)

- [Large-Scale Serverless Machine Learning Inference with Azure Functions](https://anthonychu.ca/post/serverless-machine-learning-inference-azure-functions/)


# Sign Language Gesture Recognition on the Intelligent Edge using Azure Cognitive Services

For this walkthrough we will use the [Vision AI Dev Kit](https://azure.github.io/Vision-AI-DevKit-Pages/) as the Intelligent Edge device. The goal is to show how we can quickly create image recognition models using [Custom Vision Service](https://www.customvision.ai/) and export it to consume it offline at the Edge.

![Sign Language](https://raw.githubusercontent.com/jomit/sign-langauge-recognition/master/images/signs.png)

#### Setup

- Download [dataset.zip](https://github.com/jomit/sign-langauge-recognition/blob/master/dataset.zip?raw=true) file and extract it
    - Original dataset can be found [here](https://www.kaggle.com/datamunge/sign-language-mnist/version/1)

#### Create Sign Language Recognition ML Model

- Sigin to [Custom Vision Service](https://www.customvision.ai/) using your Azure Account

- Create New Project with following configuration:
    - Project Types: **Classification**
    - Classification Types: **Multiclass**
    - Domains: **General (compact)**
    - Export Capabilties: **Vision AI Dev Kit**

- Upload all images from **dataset\A** folder with Tag **A**

- ***Repeat** above step for all alphabets in the dataset...*

- Click the **Train** button at top to start training the model

- Once the training is complete use the **Quick Test** button to upload a new image and test it.

    ![Custom Vision Service](https://raw.githubusercontent.com/jomit/sign-langauge-recognition/master/images/customvisionservice.png)


#### Export the ML Model

- Under **Performance** tab click **Export**

- Select **Vision AI Dev Kit** and download the zip file


#### Deploy the ML Model to your device

- Once you have completed the [intial setup](https://azure.github.io/Vision-AI-DevKit-Pages/docs/quick_start/), follow the instructions [here](https://azure.github.io/Vision-AI-DevKit-Pages/docs/Tutorial-HOL_Using_the_VisionSample/#deploy-your-custom-model-to-your-device) to deploy your custom vision model to your device.




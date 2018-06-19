# Sign Language Gesture Recognition on the Intelligent Edge using Azure Cognitive Services

For this walkthrough we will use an Android Phone/Tablet as the Intelligent Edge device. The goal is to show how we can quickly create image recognition models using [Custom Vision Service](https://www.customvision.ai/) and export it to consume it offline at the Edge.

If you just want to test the app you can download the APK file from [here](https://github.com/jomit/AITrials/blob/master/sign-language-recognition/sign-recognizer.apk?raw=true).

![Sign Language](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/signs.png)

#### Setup

- [Install Android Studio](https://developer.android.com/studio/index.html)

- Download [dataset.zip](https://github.com/jomit/AITrials/blob/master/sign-language-recognition/dataset.zip?raw=true) file and extract it
    - Original dataset can be found [here](https://www.kaggle.com/datamunge/sign-language-mnist/version/1)

#### Create Sign Language Recognition ML Model

- Sigin to [Custom Vision Service](https://www.customvision.ai/) using your Azure Account

- Create New Project with Domains as **General (compact)**

- Upload all images from **dataset\A** folder with Tag **A**

- ***Repeat** above step for all alphabets in the dataset...*

- Click the **Train** button at top to start training the model

- Once the training is complete use the **Quick Test** button to upload a new image and test it.

    ![Custom Vision Service](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/customvisionservice.jpg)


#### Export the ML Model

- Under **Performance** tab click **Export**

- Select **Android (Tensorflow)** and download the zip file

- Extract the zip file and verify that it contains **model.pb** and **labels.txt** file


#### Create the Android App

- Clone [cognitive-services-android-customvision-sample](https://github.com/Azure-Samples/cognitive-services-android-customvision-sample) repo as a template or you can use the [android-mobileapp](https://github.com/jomit/AITrials/tree/master/sign-language-recognition/android-mobileapp) code from this repo.

- Replace both **model.pb** and **labels.txt** files in `app\src\main\assets\`

- Open the project in Android Studio

- *Make any updates to UI / Labels as necessary*

#### Deploy the Android App on the device

- First enable Developer Mode + USB Debugging on the Android device
    - See instructions for Samsung Galaxy S7 [here](https://www.androidcentral.com/how-enable-developer-mode-galaxy-s7)

- Connect your device to laptop via USB

- Click **Run** and select the **app**

- Select the **Connected Device**

    - For first time you need to allow the camera and other permissions and run it again.


#### Testing

![Test 1 - Y](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/test1.jpg)

![Test 2 - P](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/test2.jpg)

![Test 3 - W](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/test3.jpg)

![Test 4 - V](https://raw.githubusercontent.com/jomit/AITrials/master/sign-language-recognition/images/test4.jpg)




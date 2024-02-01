# Indian_language_detector_using-ML-and-Deep-Learning
An Indian Language detector model based on various Machine Learning algorithms and deep learning algorithm, capable of detecting 10 most popular languages in india

# Dataset Used
This is a massive dataset of audio samples of 10 different Indian languages. Each audio sample is of 5 seconds duration. This dataset was created using regional videos available on YouTube. None of the audio samples/source videos are owned by me, and the dataset must not be used to create any proprietary applications.

This is constrained to Indian Languages only but could be extended.

Languages present in the dataset -
Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Punjabi, Tamil, Telugu, Urdu.

The dataset and the description was taken from Kaggle. (https://www.kaggle.com/datasets/hbchaitanyabharadwaj/audio-dataset-with-10-indian-languages)

The 10 languages files are in audio format(.mp3 format).The relevant feature from each audio is extracted with the help of librosa library and then it is saved into a csv file.
20001 audios from each language, resulting in 200010 rows of data in the csv file were used as dataset.

# Methodologies Used:
Various ML algorithms like "LogisticRegression", "RidgeClassifier", "KNeighborsClassifier", "SupportVectorClassifer", "DecisionTreeClassifier", "RandomForestClassifier", "AdaBoostClassifier" were used to cpmapre the performance of each.

Also Deep learning Algorithms are also deployed to know how the deep learning performs over machine learning. 


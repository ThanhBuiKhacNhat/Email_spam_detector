# Email Detector Spam


## Introduction
This is a Python project for detecting spam emails using the Naive Bayes classification algorithm. It includes modules for training the model on a dataset of spam and non-spam (ham) emails, and then testing the model on a separate dataset of emails to evaluate its performance.

## Guide

Here is a detailed step-by-step instruction to run this project on your local machine.

### Clone the project

Through HTTPS:

```bash
git clone https://github.com/ThanhbknAI/Email_spam_detector.git
```

Through SSH:

```bash
git clone git@github.com:ThanhbknAI/Email_spam_detector.git
```

Or you can also download the zip file.

### Download the dataset

You can download the dataset and paper here: [EmailWord](https://fptuniversity-my.sharepoint.com/:f:/g/personal/hainhde170683_fpt_edu_vn/EqsOqSf3G0NCmTJzthxiv2YBcqnE6xqg4y0mLNDuOgzopw?e=fGTYwm). 



In the above link, you can download the zip file named `train.zip` for training and `text.zip` for testing.

After downloading, extract the zip file and put it in the project directory. The directory structure must look like this:

``` bash
Email_detector_spam
├── dataset
│   ├── train
│   ├── test
├── export
│   ├── evaluation.txt
│   ├── model.txt
│   ├── result.txt
├── models
│   ├── train.py
│   ├── test.py
├── modules
│   ├── init.py
│   ├── email_counter.py
│   ├── email_parser.py
│   ├── evaluation.py
│   ├── model_builder.py
│   ├── result_builder.py
├── main.py
└── requirements.txt
```
### Create virtual environment

The version of your python should be 3.6 or higher.

```bash
python3 -m venv env
```

### Activate virtual environment

For Linux:

```bash
source env/bin/activate
```

For Windows:

```bash
.\env\Scripts\activate
```

Note:
- In Windows, if you get an error like this: `cannot be loaded because running scripts is disabled on this system`, you can run this command in your terminal: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` and then type `Y` to accept.
- If you want to deactivate the virtual environment, just type `deactivate` in your terminal.

### Install required libraries

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python3 RUNME.py
```

Or you can also click the 'run' button in your IDE.


### Update the new version

To update to a new version of the project, run the script:

```bash
git pull
```

<h2> :books: References</h2>
<ul>
  <li><p>Jonathan Lee, 'Notes on Naive Bayes Classifiers for Spam Filtering'. [Online].</p>
      <p>Available: https://courses.cs.washington.edu/courses/cse312/18sp/lectures/naive-bayes/naivebayesnotes.pdf</p>
  </li>
  <li><p>Wikipedia.org, 'Naive Bayes Classifier'. [Online].</p>
      <p>Available: https://en.wikipedia.org/wiki/Naive_Bayes_classifier</p>
  </li>
  <li><p>Youtube.com, 'Naive Bayes for Spam Detection'. [Online].</p>
      <p>Available: https://www.youtube.com/watch?v=8aZNAmWKGfs</p>
  </li>
  <li><p>Youtube.com, 'Text Classification Using Naive Bayes'. [Online].</p>
      <p>Available: https://www.youtube.com/watch?v=EGKeC2S44Rs</p>
  </li>
  <li><p>Manisha-sirsat.blogspot.com, 'What is Confusion Matrix and Advanced Classification Metrics?'. [Online].</p>
      <p>Available: https://manisha-sirsat.blogspot.com/2019/04/confusion-matrix.html</p>
  </li>
  <li><p>Pythonforengineers.com, 'Build a Spam Filter'. [Online].</p>
      <p>Available: https://www.pythonforengineers.com/build-a-spam-filter/</p>
  </li>
</ul>

Have the best experience with our project!

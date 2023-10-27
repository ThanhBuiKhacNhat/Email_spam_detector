import os

class email_counter:
    def __init__(self, train_path):
        self.train_path = train_path

    # Returns the number of all emails (train files) 
    def number_of_all_emails(self):
        counter = 0
        for directories, subdirectories, files in os.walk(self.train_path):
            for filename in files:
                counter += 1
        return counter
    # Returns the number of spam emails (train files) 
    def number_of_spam_emails(self):
        counter = 0
        for directories, subdirectories, files in os.walk(self.train_path):
            for filename in files:
                if "spam" in filename:
                    counter += 1
        return counter
    # Returns the number of ham emails (train files)
    def number_of_ham_emails(self):
        counter = 0
        for directories, subdirectories, files in os.walk(self.train_path):
            for filename in files:
                if "ham" in filename:
                    counter += 1
        return counter

import os
import pandas as pd
import pickle

cwd = os.getcwd()
VOiCES_devkit = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir, "VOiCES_devkit", "VOiCES_devkit"))
references = os.path.abspath(os.path.join(VOiCES_devkit, "references", ))
list_file_ref = os.listdir(references)
filenameTranscripts = 0
speakerBookChapter = 1
speakerGenderDataset = 2
testSetSpeakers = 3
testIndex = 4
timeValues = 5
trainIndex = 6

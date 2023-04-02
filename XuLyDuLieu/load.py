import os
import pandas as pd
import pickle

cwd = os.getcwd()
parent_data_dir = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir, "VOiCES_devkit", "VOiCES_devkit"))
refer_dir = os.path.abspath(os.path.join(parent_data_dir, "references", ))
list_file_ref = dict()
for i in os.listdir(refer_dir):
    if ".tbl" in i:
        list_file_ref[i] = pd.read_csv(os.path.abspath(os.path.join(refer_dir, i)), delimiter=" ")
    else:
        list_file_ref[i] = pd.read_csv(os.path.abspath(os.path.join(refer_dir, i)))
file_name = 'csv_pandas_obj.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(list_file_ref, file)
    print(f'Object successfully saved to "{file_name}"')


if __name__ == "__main__":
    # print(parent_data_dir)
    # print(refer_dir)
    # print(list_file_ref)
    # print(filename_transcripts)
    # with open(file_name, 'rb') as file:
    #     l = pickle.load(file)
    #     print(f'Object successfully saved to "{file_name}"')


    pass

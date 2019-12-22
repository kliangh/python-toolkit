import pandas as pd


def read_csv_file(file_path, csv_headers):
    return pd.read_csv(file_path, header=None, names=csv_headers)


def read_csv_files(directory_path, csv_headers):
    files = list(directory_path.rglob('*.csv'))
    return merge_files_into_dataframe(files, csv_headers)


def merge_files_into_dataframe(files, headers):
    dataframes = []

    for file in files:
        df = pd.read_csv(file, header=None, names=headers)
        dataframes.append(df)
    print("Loaded files: " + repr(files))
    return pd.concat(dataframes, axis=0, ignore_index=False)


def export_csv_file(input_dataframe, filename_with_path):
    input_dataframe.to_csv(filename_with_path, index=True, header=True)

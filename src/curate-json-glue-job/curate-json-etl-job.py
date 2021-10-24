import json
import re
import pandas as pd

def dequote_string(record):
    """
    If a raw data record has quotes around it, remove them.
    If a matching pair of quotes is not found, return the record unchanged.
    for e.g. "{"postcode":"3000"}" -> {"postcode":"3000"}
    """
    if record.startswith('"') and record.endswith('"'):
        record = record[1:-1]
    return record

def dequote_json_elements(record):
    """
    If a JSON string elements have extra double quotes around it, remove them.
    So, that the raw data blob can be parsed as valid JSON
    for e.g. {""postcode"":""3000""} -> {"postcode":"3000"}
    """
    record = re.sub('""','"',record)
    return record

def flatten_json_record(record):
    """
    This function flattens objects with embedded arrays
    inspired from https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
    """
    dic = json.loads(record)
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            # print("x->",x)
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x
    flatten(dic)
    return out

def extract(file_path):
    """
    Recieves a file path for the raw input json file
    Fixes known data quality problems in source file (if any)
    Unmarshals the raw JSON into python native dictionary
    """
    jsonDict = []
    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            line = dequote_string(line)
            line = dequote_json_elements(line)
            jsonDict.append(flatten_json_record(line))
    return jsonDict

def transform(dic):
    """
    Transforms json dictionary to panda DF as per required structure
    """
    df = pd.DataFrame.from_dict(dic)
    df = df.explode('search_params_brand_ids')
    return df

def load(df, output_prefix, file_name):
    """
    Loads final flat structured df to required location
    """
    df.to_csv(output_prefix+file_name, index=False)

if __name__ == "__main__":
    input_key = 'src/curate-json-glue-job/test_files/input_json_blob.dat'
    output_prefix = 'src/curate-json-glue-job/test_files/'
    file_name = 'output_flat_file.dat'

    raw_dic = extract(input_key)
    curated_df = transform(raw_dic)
    load(curated_df, output_prefix, file_name)
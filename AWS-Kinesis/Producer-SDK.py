from astropy.io import fits
from astropy.table import Table
import boto3
import os
import json
import numpy as np

# your directory of all raw '.fits' data.
directory_path = "/raw_data"
fits_files = [file for file in os.listdir(directory_path) if file.endswith(".fits")]
# control randomization.
np.random.seed(len('Simon Chen is a great data engineer'))

# standardize the 'flux'
def standardize_list(input_list):
    np_array = np.array(input_list)
    mean_value = np.mean(np_array)
    stdev_value = np.std(np_array)
    standardized_array = (np_array - mean_value) / stdev_value

    # Convert the NumPy array back to a list 
    standardized_list = standardized_array.tolist()

    return standardized_list

# operate each .fits file. This step is to stimulate real-data production in astronomical observatory.
for fits_file in fits_files:
    fits_file_path = os.path.join(directory_path, fits_file)
    with fits.open(fits_file_path) as hdul:
        data = hdul[1].data
        data_table = Table(data)
        
        observatory_id = int(np.random.choice([1,2,3])) # simulates astronomical observatory id.
        flux = standardize_list(list(data_table['flux']))
        flux = [ float(x) for x in flux]
        loglam = [ float(x) for x in data_table['loglam']]
        and_mask = [ float(x) for x in data_table['and_mask']]
        or_mask =[ float(x) for x in data_table['or_mask']]
        sky = [ float(x) for x in data_table['sky']]
        wdisp = [ float(x) for x in data_table['wdisp']]
        ivar =[ float(x) for x in data_table['ivar']]
    
    hashmap = {'spectrum_id':fits_file,'flux':flux,'loglam':loglam,'and_mask':and_mask,'or_mask':or_mask}
    record = json.dumps(hashmap)

    # replace to your key_id, key, region
    aws_access_key_id = 'your_access_key_id'
    aws_secret_access_key = 'your_secret_access_key'
    region_name = 'your_region'

    # replace to your kinesis stream
    stream_name = 'your_first_kinesis_stream'


    kinesis_client = boto3.client('kinesis', aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key, region_name=region_name)


    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=record,
        PartitionKey=str(observatory_id))

    print(response)

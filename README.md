# TCA-GCN
The code will be open source soon...
# Prerequisites

- Python = 3.8.8
- PyTorch = 1.10.0
- Run `pip install -e torchlight` 

# NTU RGB+D 60 and 120 and NW-UCLA

1.Download the raw data from the website and place it in the appropriate directory of the './data' file
2.Generate NTU RGB+D 60 and NTU RGB+D 120 dataset:  python get_raw_skes_data.py,  python get_raw_denoised_data.py,  python seq_transformation.py
3. Place the processed data file into the data_path parameter inside the './config'

# Training & Testing

### Training

# Example: training TCAGCN on NTU RGB+D 120 cross subject, the training setup parameters for the other datasets are set under the './config' file 
python main.py --config config/nturgbd120-cross-subject/default.yaml 


### Testing

- To test the trained models saved in <work_dir>:
python main.py --config <work_dir>/config.yaml --work-dir <work_dir>  --weights <work_dir>/.pt 


- To ensemble the results of different streams
python ensemble.py 

# Pretrained Models

We provide individual stream weighting files for the relevant dataset
# Acknowledgements
This repo is manly based on [CTR-GCN](https://github.com/Uason-Chen/CTR-GCN). 
Many thanks to the authors for their work and to the original authors involved for giving me an opportunity to learn from them.

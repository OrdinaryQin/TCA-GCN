# TCA-GCN
We are constantly improving the program
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

 Example: training TCAGCN on NTU RGB+D 120 cross subject, the training setup parameters for the other datasets are set under the './config' file 
python main.py --config config/nturgbd120-cross-subject/default.yaml 


### Testing

- To test the trained models saved in <work_dir>:
python main.py --config <work_dir>/config.yaml --work-dir <work_dir>  --weights <work_dir>/.pt 


- To ensemble the results of different streams
python zhenghe.py 

# Pretrained Models

We provide individual stream weighting files for the relevant dataset
# Acknowledgements
This repo is manly based on [CTR-GCN](https://github.com/Uason-Chen/CTR-GCN). 
Many thanks to the authors for their work and to the original authors involved for giving me an opportunity to learn from them.
# Please cite the paper if you find it useful:

@misc{https://doi.org/10.48550/arxiv.2205.15936,
  doi = {10.48550/ARXIV.2205.15936},
  url = {https://arxiv.org/abs/2205.15936},
  author = {Wang, Shengqin and Zhang, Yongji and Wei, Fenglin and Wang, Kai and Zhao, Minghao and Jiang, Yu},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Skeleton-based Action Recognition via Temporal-Channel Aggregation},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution Non Commercial No Derivatives 4.0 International}
}

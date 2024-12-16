<div align=center>
<img src="https://github.com/Leikrit/FSCIL-Toolkit/blob/main/FSCILTOOLKIT.png" width="900" height="135">

![Github stars](https://img.shields.io/github/stars/Leikrit/FSCIL-Toolkit.svg)
[![GitHub license](https://img.shields.io/github/license/Leikrit/FSCIL-Toolkit)](https://github.com/Leikrit/FSCIL-Toolkit/blob/master/LICENSE)

---
</div>

# FSCIL-Toolkit

First things first, please allow us to highlight the significant previous works. Our toolkit is based on <a href="https://github.com/icoz69/CEC-CVPR2021">CEC</a>, <a href="https://github.com/zhoudw-zdw/CVPR22-Fact">FACT</a>, <a href="https://github.com/jayatejak/s3c">S3C</a>, <a href="https://github.com/Zoilsen/CLOM">CLOM</a>, <a href="https://github.com/annusha/LCwoF">LCwoF</a> and <a href="https://github.com/Yang-Bob/DSN">DSN</a>. 

## Relevant Repositories

- <a href='https://github.com/icoz69/CEC-CVPR2021'>CEC</a> ![Github stars](https://img.shields.io/github/stars/icoz69/CEC-CVPR2021.svg)
- <a href='https://github.com/zhoudw-zdw/CVPR22-Fact'>FACT</a></a> ![Github stars](https://img.shields.io/github/stars/zhoudw-zdw/CVPR22-Fact.svg)
- <a href='https://github.com/jayatejak/s3c'>S3C</a> ![Github stars](https://img.shields.io/github/stars/jayatejak/s3c.svg)
- <a href='https://github.com/Zoilsen/CLOM'>CLOM</a> ![Github stars](https://img.shields.io/github/stars/Zoilsen/CLOM.svg)
- <a href='https://github.com/annusha/LCwoF'>LCwoF</a> ![Github stars](https://img.shields.io/github/stars/annusha/LCwoF.svg)
- <a href='https://github.com/Yang-Bob/DSN'>DSN</a> ![Github stars](https://img.shields.io/github/stars/Yang-Bob/DSN.svg)

## Introduction

Few-shot Class-incremental Learning (FSCIL) is an emerging paradigm that addresses the challenge of learning new classes over time without forgetting previously learned ones. To streamline the development and deployment of FSCIL solutions, we introduce the Few-shot Class-incremental Learning Toolkit (FSCIL-Toolkit). This toolkit serves as a comprehensive platform for researchers and practitioners to experiment with and develop FSCIL strategies, offering a suite of classical FSCIL algorithms, a variety of datasets for thorough performance assessment.

FSCIL-Toolkit currently contains:

- 4 FSCIL methods
- 3 available datasets
- and more to be updated

## How to start

```shell
git clone https://github.com/Leikrit/FSCIL-Toolkit.git
```

```shell
cd FSCIL-Toolkit
```

### Environment & Requirements

Our toolkit is developed under the environment of:
- Python 3.9
- PyTorch 2.5.1 (any version >= 1.8 is okay)
- tqdm

There is no more packages to install.

### Dataset Preparation

You should firstly prepare the dataset following <a href="https://github.com/icoz69/CEC-CVPR2021">CEC</a>. Just leave the folder `data` in the same directory with `fsciltoolkit.py`.

### Training

For each method, please refer to their original Github repository, following the command.

Here, we provide some examples for you:

```shell
python fsciltoolkit.py [xxx]
```
Where [xxx] is the original command for each method, for example:

```shell
python fsciltoolkit.py -project base -dataset cifar100  -base_mode 'ft_cos' -new_mode 'avg_cos' -gamma 0.1 -lr_base 0.1 -lr_new 0.1 -decay 0.0005 -epochs_base 100 -schedule Milestone -milestones 60 70 -gpu 0,1,2,3 -temperature 16
```

```shell
python fsciltoolkit.py -project fact -dataset cub200 -base_mode 'ft_cos' -new_mode 'avg_cos' -gamma 0.25 -lr_base 0.005 -lr_new 0.1 -decay 0.0005 -epochs_base 400 -schedule Milestone -milestones 50 100 150 200 250 300 -gpu '3,2,1,0' -temperature 16 -dataroot YOURDATAROOT -batch_size_base 256 -balance 0.01 -loss_iter 0  >>CUB-FACT.txt 
```
> Remember to change YOURDATAROOT into yours, or you might encounter some errors.

## Citation

If you find FSCIL-Toolkit helpful, please cite us.

```bibtex
@software{Li_FSCIL-Toolkit_2024,
author = {Li, Jinyi and Yao, Yiyang and Li, Yulong},
month = dec,
title = {{FSCIL-Toolkit}},
version = {1.0.0},
year = {2024}
}
```

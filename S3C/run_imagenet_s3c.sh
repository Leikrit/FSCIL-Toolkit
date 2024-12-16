Method=both_stochastic_self_sup_aggregation_expts_imagenet
mkdir -p S3C_logs/imagenet_log_dir/${Method}/

python S3C/train.py -project s3c -dataset mini_imagenet  -base_mode 'ft_cos' \
-new_mode 'avg_cos' -gamma 0.1 -lr_base 0.1 -lr_new 0.01 -decay 0.0005 \
-epochs_base 100 -epochs_new 100 -schedule Milestone -milestones 40 70 \
-lamda_proto 1 \
-gpu 4 -temperature 16 --Method ${Method} \
2>&1 | tee ./S3C_logs/imagenet_log_dir/${Method}/log_imagenet.txt
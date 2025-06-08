nohup python openfunctions_evaluation.py --model qwen3-8b --temperature 0.6 --num-threads 10 --test-category 'simple' 'parallel' 'multiple' 'parallel_multiple' 'live_irrelevance' 'live_multiple' 'live_parallel' 'live_parallel_multiple' 'live_relevance' 'live_simple' 'multi_turn_base' 'multi_turn_miss_func' 'multi_turn_miss_param' 'multi_turn_long_context' >> /mnt/pfs-guan-ssai/nlu/wangjianing1/bfcl_work/qwen3-8b.log 2>&1 &

# 'exec_simple' 'exec_parallel' 'exec_multiple' 'exec_parallel_multiple' 'simple' 'parallel' 'multiple' 'parallel_multiple' 'irrelevance' 'java' 'javascript' 'live_irrelevance' 'live_multiple' 'live_parallel' 'live_parallel_multiple' 'live_relevance' 'live_simple' 'multi_turn_base' 'multi_turn_miss_func' 'multi_turn_miss_param' 'multi_turn_long_context'

# [
#     "exec_simple",
#     "exec_parallel",
#     "exec_multiple",
#     "exec_parallel_multiple",
#     "simple",
#     "irrelevance",
#     "parallel",
#     "multiple",
#     "parallel_multiple",
#     "java",
#     "javascript",
#     "rest",
#     "live_simple",
#     "live_multiple",
#     "live_parallel",
#     "live_parallel_multiple",
#     "live_irrelevance",
#     "live_relevance",
#     "multi_turn_base",
#     "multi_turn_miss_func",
#     "multi_turn_miss_param",
#     "multi_turn_long_context",
# ]

# 如果是带<think>标签的推理模型，需要后处理一下result结果，去掉<think>内容
python update_result_file.py --model qwen3-8b


nohup python bfcl/eval_checker/eval_runner.py --model qwen3-8b --test-category 'simple' 'parallel' 'multiple' 'parallel_multiple' 'irrelevance' 'java' 'javascript' 'live_irrelevance' 'live_multiple' 'live_parallel' 'live_parallel_multiple' 'live_relevance' 'live_simple' 'multi_turn_base' 'multi_turn_miss_func' 'multi_turn_miss_param' 'multi_turn_long_context' >> /mnt/pfs-guan-ssai/nlu/wangjianing1/bfcl_work/qwen3-8b.log 2>&1 &
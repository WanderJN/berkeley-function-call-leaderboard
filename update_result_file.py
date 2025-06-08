import os
import re
import json
import jsonlines


def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 跳过空行
            if line.strip():
                data.append(json.loads(line))
    return data


def remove_think_tags(datas):
    for data in datas:
        # 如果data['result']是列表，对应多轮任务
        if isinstance(data['result'], list):
            for i in range(len(data['result'])):
                for j in range(len(data['result'][i])):
                    data['result'][i][j] = re.sub(r'<\s*think\s*>.*?<\s*/\s*think\s*>', '', data['result'][i][j], flags=re.DOTALL).strip()
        
        # 如果data['result']是字符串
        elif isinstance(data['result'], str):
            data['result'] = re.sub(r'<\s*think\s*>.*?<\s*/\s*think\s*>', '', data['result'], flags=re.DOTALL).strip()
    return datas


def save_to_jsonl(data, output_path):
    with jsonlines.open(output_path, 'w') as writer:
        writer.write_all(data)  # 直接写入所有数据


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="更新文件，删掉<think>标签")
    parser.add_argument("--model", type=str, required=True)
    # 解析命令行参数
    args = parser.parse_args()

    # 先给原文件夹改名加上_old
    folder_path = "/mnt/pfs-guan-ssai/nlu/wangjianing1/gorilla/berkeley-function-call-leaderboard/result/" + args.model
    os.rename(folder_path, folder_path + "_old")
    folder_path = folder_path + "_old"

    new_folder_path = "/mnt/pfs-guan-ssai/nlu/wangjianing1/gorilla/berkeley-function-call-leaderboard/result/" + args.model
    if not os.path.exists(new_folder_path):
        # 创建文件夹（包括所有必要的父文件夹）
        os.makedirs(new_folder_path)

    all_path = os.listdir(folder_path)

    for path in all_path:
        # 示例使用
        data = read_jsonl(folder_path + '/' + path)
        data = remove_think_tags(data)

        save_to_jsonl(data, new_folder_path + '/' + path)


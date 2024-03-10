import ijson
import json
import csv

problem_dict = {}

# 打开JSON文件并使用ijson进行解析
with open('student-problem-middle.json', 'r') as json_file, open('student-problem-middle-problem.json', 'r') as problem_json_file:
    parser = ijson.parse(json_file)
    for line in problem_json_file:
        try:
            item = json.loads(line)
            problem_dict[item['problem_id']] = item['cognitive_dimension']
        except json.JSONDecodeError:
            continue

    user_id = None
    skill_id = None
    is_correct = None
    cognitive_dimension = None
    # 创建一个TSV文件来写入数据
    with open('output_middle.tsv', 'w', newline='') as tsv_file:
    # with open('output_coarse.tsv', 'w', newline='') as tsv_file:
        fieldnames = ['num', 'student', 'skill', 'right', 'cognitive_level']
        tsv_writer = csv.DictWriter(tsv_file, fieldnames=fieldnames, delimiter='\t')
        # tsv_writer = csv.writer(tsv_file, delimiter='\t')
        # 写入列名
        tsv_writer.writeheader()
        num = 1
        for prefix, event, value in parser:
            # 检查当前键是否是需要的字段
            if prefix.endswith('.user_id'):
                user_id = value
            elif prefix.endswith('.skill_id'):
                skill_id = value
            elif prefix.endswith('.is_correct'):
                is_correct = value
            elif prefix.endswith('.problem_id'):
                problem_id = value
                cognitive_dimension = problem_dict.get(problem_id)

            # 当所有字段都准备好时，写入到TSV文件
            if user_id is not None and skill_id is not None and is_correct is not None and cognitive_dimension is not None:
                # 写入数据到TSV文件
                tsv_writer.writerow({'num': num, 'student': user_id, 'skill': skill_id, 'right': is_correct, 'cognitive_level': cognitive_dimension})

                # 重置字段值以准备下一个记录
                user_id = None
                skill_id = None
                is_correct = None
                cognitive_dimension = None
                num += 1
print("Data has been written to output.tsv.")

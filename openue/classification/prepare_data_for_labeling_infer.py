import os
import sys

def get_latest_model_predict_data_dir(new_epochs_ckpt_dir=None):
    def new_report(test_report):
        lists = os.listdir(test_report)  
        lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn)) 
        file_new = os.path.join(test_report, lists[-1]) 
        return file_new
    if new_epochs_ckpt_dir is None:
        input_new_epochs = os.path.join(
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../output")), "predicate_infer_out")
        new_ckpt_dir = new_report(input_new_epochs)
        input_new_epochs_ckpt = os.path.join(input_new_epochs, new_ckpt_dir)
        new_epochs_ckpt_dir = new_report(input_new_epochs_ckpt)
    return new_epochs_ckpt_dir

def replace_empty_infer_predicate_to_three_possible_values(predicate_score_value):
    label_list = ['丈夫', '上映时间', '专业代码', '主持人', '主演', '主角', '人口数量', '作曲', '作者', '作词', '修业年限', '出品公司', '出版社', '出生地', '出生日期',
              '创始人', '制片人', '占地面积', '号', '嘉宾', '国籍', '妻子', '字', '官方语言', '导演', '总部地点', '成立日期', '所在城市', '所属专辑', '改编自',
              '朝代', '歌手', '母亲', '毕业院校', '民族', '气候', '注册资本', '海拔', '父亲', '目', '祖籍', '简称', '编剧', '董事长', '身高', '连载网站',
              '邮政编码', '面积', '首都']
    predicate_score_value_list = predicate_score_value.split(" ")
    predicate_score_name_value_list = [(label, value) for label, value in zip(label_list, predicate_score_value_list)]
    predicate_score_name_value_sort_list = sorted(predicate_score_name_value_list, key=lambda x: x[1], reverse=True)
    name_value_three_items = predicate_score_name_value_sort_list[:10]
    three_predicate_list = [name for name, value in name_value_three_items]
    return three_predicate_list


def prepare_data_for_subject_object_labeling_infer(predicate_classifiction_input_file_dir,
                                                   predicate_classifiction_infer_file_dir, out_file):
    """
    Converting the predicted results of the multi-label classification model
    into the input format required by the sequential label model
    :param predicate_classifiction_input_file_dir: Path of Input file of classification model
    :param predicate_classifiction_infer_file_dir: Path of Predictive Output of Classification Model
    :param out_file: Path of Input file of sequential labeling model
    :return: Input file of sequential labeling model
    """
    text_file = open(os.path.join(predicate_classifiction_input_file_dir, "text.txt"),
                     "r", encoding='utf-8').readlines()
    token_in_file = open(os.path.join(predicate_classifiction_input_file_dir, "token_in.txt"),
                         "r", encoding='utf-8').readlines()
    token_in_not_UNK_file = open(os.path.join(predicate_classifiction_input_file_dir, "token_in_not_UNK.txt"),
                         "r", encoding='utf-8').readlines()
    new_epochs_ckpt_dir = get_latest_model_predict_data_dir(predicate_classifiction_infer_file_dir)
    predicate_predict_file = open(os.path.join(new_epochs_ckpt_dir, "predicate_predict.txt"),
                                  "r", encoding='utf-8').readlines()
    predicate_score_value_file = open(os.path.join(new_epochs_ckpt_dir, "predicate_score_value.txt"),
                                      "r", encoding='utf-8').readlines()
    output_text_file_write = open(os.path.join(out_file, "text_and_one_predicate.txt"), "w", encoding='utf-8')
    output_token_in_file_write = open(os.path.join(out_file, "token_in_and_one_predicate.txt"), "w", encoding='utf-8')
    output_token_in_not_UNK_file_write = open(os.path.join(out_file, "token_in_not_UNK_and_one_predicate.txt"), "w", encoding='utf-8')
    count_line = 0
    count_empty_line = 0
    count_temporary_one_predicate_line = 0
    for text, token_in, token_in_not_UNK, predicate_predict, predicate_score_value in zip(text_file, token_in_file, token_in_not_UNK_file,
                                                                        predicate_predict_file, predicate_score_value_file):
        count_line += 1
        predicate_list = predicate_predict.replace("\n", "").split(" ")
        if predicate_predict == "\n":
            count_empty_line += 1
            predicate_list = replace_empty_infer_predicate_to_three_possible_values(predicate_score_value)
        for predicate in predicate_list:
            count_temporary_one_predicate_line += 1
            output_text_file_write.write(text.replace("\n", "") + "\t" + predicate + "\n")
            output_token_in_file_write.write(token_in.replace("\n", "") + "\t" + predicate + "\n")
            output_token_in_not_UNK_file_write.write(token_in_not_UNK.replace("\n", "") + "\t" + predicate + "\n")


if __name__=="__main__":
    predicate_classifiction_input_file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../classification/classification_data/"+ sys.argv[1] +"/test"))
    #predicate_classifiction_infer_file_dir = "output/predicate_infer_out/epochs6/ckpt23000"
    predicate_classifiction_infer_file_dir = None 
    out_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../sequence_labeling/sequence_labeling_data/"+ sys.argv[1] +"/test"))
    prepare_data_for_subject_object_labeling_infer(predicate_classifiction_input_file_dir,
                                                   predicate_classifiction_infer_file_dir, out_file)

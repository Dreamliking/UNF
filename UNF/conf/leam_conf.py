#coding:utf-8
"""
data_loader conf解释：
dataset: 配置训练数据和训练数据的格式，提供自动加载的功能
field: 针对每一个域提供一个相应的配置，每一个域的tokenzie，最大长度，是否返回padding长度（LSTM用）等
iterator: 提供迭代的配置，包括每个batch大小，device是cpu还是gpu
"""
#data_loader相关
data_loader_conf = {
    "dataset":{
        "path": "test/test_data/tiktok_music",
        "train": "music_train",
        "validation": "music_valid",
        "test": "music_test",
        "format": "json"
    },
    "fields":[{
        "name":"TEXT",
        "name_cls":"WordField",
        "attrs":{
            "tokenize":"WhitespaceTokenizer",
            }
        },
        {
            "name":"LABEL",
            "name_cls":"LabelField",
        }],
    "iterator":{
        "batch_size":64,
        "shuffle": True,
    }
}

#模型相关
model_conf = [
    {
        "name": "TEXT",
        "encoder_cls": "LEAM",
        "encoder_params": {
            "input_dim": 100,
            "ngram": 6,
            "dropout": 0.1,
            "pretrained": False,
        }
    }
]

#learner相关的
learner_conf = {
    "num_epochs": 10,
    "optimizer": "Adam",
    "optimizer_parmas": {
        "lr": 1e-4
    },
    "device": "cuda:2",
    "loss": "CrossEntropyLoss",
    "serialization_dir": "tiktok_music_leam",
    "label_tag": "__label__1"
}


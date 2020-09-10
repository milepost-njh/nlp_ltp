#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:04:09 2020

@author: nijiahui
"""

# # 1，分句子
# from pyltp import SentenceSplitter
# sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
# print ('\n'.join(sents))



# # 2，分词
# import os
# from pyltp import Segmentor

# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

# segmentor = Segmentor()  # 初始化实例
# segmentor.load(cws_model_path)  # 加载模型
# word1 = segmentor.segment('中信建投证券投资有限公司')  # 分词
# word2 = segmentor.segment('中信今天投资了一款游戏')  # 分词
# print(type(word1))
# print ('\t'.join(word1))
# print ('\t'.join(word2))
# segmentor.release()  # 释放模型


# # 3，分词-外部词典  （只能处理小于5个字的词典）
# import os
# from pyltp import Segmentor

# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

# segmentor = Segmentor()  # 初始化实例
# segmentor.load_with_lexicon(cws_model_path, './substantive_word.txt') # 加载模型，第二个参数是您的外部词典文件路径
# word1 = segmentor.segment('中信建投证券投资有限公司')  # 分词
# word2 = segmentor.segment('中信今天投资了一款游戏')  # 分词
# print ('\t'.join(word1))
# print ('\t'.join(word2))
# segmentor.release() # 释放模型


# # 4，使用个性化分词模型 / 同时也可以使用外部词典
# # (https://ltp.readthedocs.io/zh_CN/v3.3.0/train.html)
# # (http://ltp.ai/docs/ltp3.x/theory.html#id10)
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

# from pyltp import CustomizedSegmentor
# customized_segmentor = CustomizedSegmentor()  # 初始化实例
# customized_segmentor.load_with_lexicon(cws_model_path, '/path/to/your/customized_model', './substantive_word.txt') # 加载模型
# words = customized_segmentor.segment('亚硝酸盐是一种化学物质')
# print ('\t'.join(words))
# customized_segmentor.release()


# # 5，词性标注 - (https://ltp.readthedocs.io/zh_CN/latest/appendix.html)
# import os
# from pyltp import Segmentor

# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

# segmentor = Segmentor()  # 初始化实例
# segmentor.load_with_lexicon(cws_model_path, './substantive_word.txt') # 加载模型，第二个参数是您的外部词典文件路径
# word1 = segmentor.segment('中信建投证券投资有限公司')  # 分词
# word2 = segmentor.segment('中信今天投资了一款游戏')  # 分词
# print ('\t'.join(word1))
# print ('\t'.join(word2))
# segmentor.release() # 释放模型

# ------------------------------------
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

# from pyltp import Postagger
# postagger = Postagger() # 初始化实例
# postagger.load(pos_model_path)  # 加载模型

# word1 = ["中信建投","证券","投资","有限公司"]
# word2 = ["中信","	今天","投资","了","一款","游戏"]

# postags1 = postagger.postag(word1)  # 词性标注
# postags2 = postagger.postag(word2)  # 词性标注

# print ('\t'.join(postags1))
# print ('\t'.join(postags2))

# postagger.release()  # 释放模型


# # 6，词性标注 - 外部词典
# import os
# from pyltp import Segmentor

# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

# segmentor = Segmentor()  # 初始化实例
# segmentor.load_with_lexicon(cws_model_path, './substantive_word.txt') # 加载模型，第二个参数是您的外部词典文件路径
# word1 = segmentor.segment('中信建投证券投资有限公司')  # 分词
# word2 = segmentor.segment('中信今天投资了一款雷人游戏')  # 分词
# print ('\t'.join(word1))
# print ('\t'.join(word2))
# segmentor.release() # 释放模型

# # ------------------------------------
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

# from pyltp import Postagger
# postagger = Postagger() # 初始化实例
# postagger.load_with_lexicon(pos_model_path,"./properties_word.txt")  # 加载模型

# word1 = ["中信建投","证券","投资","有限公司"]
# word2 = ["中信","	今天","投资","了","一款","游戏"]

# postags1 = postagger.postag(word1)  # 词性标注
# postags2 = postagger.postag(word2)  # 词性标注

# print ('\t'.join(postags1))
# print ('\t'.join(postags2))

# postagger.release()  # 释放模型


# # 7，命名实体识别
# # 1）分詞 - 字典
# import os
# from pyltp import Segmentor
#
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
#
# segmentor = Segmentor()  # 初始化实例
# segmentor.load_with_lexicon(cws_model_path, './substantive_word.txt') # 加载模型，第二个参数是您的外部词典文件路径
# word1 = segmentor.segment('中信建投证券投资有限公司今天投资了一款雷人游戏')  # 分词
# word2 = segmentor.segment('中信今天投资了一款雷人游戏')  # 分词
# print ('\t'.join(word1))
# print ('\t'.join(word2))
# segmentor.release() # 释放模型
# # 2）
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
#
# from pyltp import Postagger
# postagger = Postagger() # 初始化实例
# postagger.load_with_lexicon(pos_model_path,"./properties_word.txt")  # 加载模型
#
# postags1 = postagger.postag(word1)  # 词性标注
# postags2 = postagger.postag(word2)  # 词性标注
#
# print ('\t'.join(postags1))
# print ('\t'.join(postags2))
#
# postagger.release()  # 释放模型
# # 3）命名实体识别  - (https://ltp.readthedocs.io/zh_CN/latest/appendix.html)

# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

# from pyltp import NamedEntityRecognizer
# recognizer = NamedEntityRecognizer() # 初始化实例
# recognizer.load(ner_model_path)  # 加载模型

# word1 = ["中信建投","证券","投资","有限公司"]
# word2 = ["中信","今天","投资","了","一款","游戏"]

# postags1  = ["j","n","v","n"]
# postags2 = ["j","nt","v","u","m","n"]

# netags1 = recognizer.recognize(word1, postags1)  # 命名实体识别
# netags2 = recognizer.recognize(word2, postags2)  # 命名实体识别

# print('\t'.join(netags1))
# print('\t'.join(netags2))
# recognizer.release()  # 释放模型


# # 8，依存句法分析 - (https://ltp.readthedocs.io/zh_CN/latest/appendix.html)
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

# from pyltp import Parser
# parser = Parser() # 初始化实例
# parser.load(par_model_path)  # 加载模型

# words = ['中信建投', '证券', '投资', '有限公司',"今天","投资","了","一款","雷人","游戏"]
# postags = ["j","n","v","n","nt","v","u","m","n","n"]
# arcs = parser.parse(words, postags)  # 句法分析

# print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
# parser.release()  # 释放模型

# 9，语义角色标注
# 1）
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

# from pyltp import Parser
# parser = Parser() # 初始化实例
# parser.load(par_model_path)  # 加载模型

# words = ['中信建投', '证券', '投资', '有限公司',"今天","投资","了","一款","雷人","游戏"]
# postags = ["j","n","v","n","nt","v","u","m","n","n"]
# arcs = parser.parse(words, postags)  # 句法分析

# print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
# parser.release()  # 释放模型

# # 2）
# import os
# LTP_DATA_DIR = './ltp_data_v3.4.0'  # ltp模型目录的路径
# srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。

# from pyltp import SementicRoleLabeller
# labeller = SementicRoleLabeller() # 初始化实例
# labeller.load(srl_model_path)  # 加载模型

# words = ['中信建投', '证券', '投资', '有限公司',"今天","投资","了","一款","雷人","游戏"]
# postags = ["j","n","v","n","nt","v","u","m","n","n"]
# # arcs 使用依存句法分析的结果
# roles = labeller.label(words, postags, arcs)  # 语义角色标注

# # 打印结果
# for role in roles:
#     print (role.index, "".join(["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
# labeller.release()  # 释放模型


# coding=utf-8
#!python3

# =======================================================================
"""
来源：
问题：
接口：
说明：
"""
# =======================================================================
# modules section
import pickle

words_txt  = 'others/words.txt'
note_txt   = 'others/note.txt'

# 可以使用任何类型的扩展名
msg_pickle = 'others/msg.pkl'

msg_list = ['Fred', 73, 'Hello there', 99.99e-20]

pickle_file = open(msg_pickle, 'ab')
pickle.dump('msg-1', pickle_file)
pickle.dump(msg_list, pickle_file)
pickle_file.close()

pickle_file = open(msg_pickle, 'rb')
new_list1 = pickle.load(pickle_file)
new_list2 = pickle.load(pickle_file)
pickle_file.close()

print(new_list1)
print(new_list2)

#encoding:utf-8
#import shelve
#import pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle
"""
cPickle 用c语言重写python库文件，速度快
dump(object,file)
dumps(object)->string
load(file)->object
load(string)->object
"""
#保存数据
# hfile1 =open('pickle.txt','w')
# dict1 = {'a':1,'b':2}
# pickle.dump(dict1,hfile1)
# hfile1.close()

#读取数据
hfile1 =open('pickle.txt')
dict2 = pickle.load(hfile1)
print(type(dict2))
print dict2
hfile1.close()

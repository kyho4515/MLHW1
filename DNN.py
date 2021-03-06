import theano
import theano.tensor as T

class Data:
    def __init__(self, filePath):
        self.path = filePath
        self.fin = open(self.path, 'r')
        
    def load_batch(self, batch_num):
        data = []
        for i in range(batch_num):
            line = self.fin.readline()
            if line == '':
                break
            tokenList = line.split()
            data.append(tokenList[1:])
        return data


path = raw_input("Please input the path that contain all the input data(i.e. the folder contain \"MLDS_HW1_RELEASE_v1\"):")
if path[len(path)-1] != '/':
    path += "/"
trainData = Data(path+"MLDS_HW1_RELEASE_v1/fbank/train.ark")

import json as js
import pickle


class JsonPickle:
    def create_pickle(self):
        with open('dummy.json', 'r') as f:
            dummy = js.load(f)
        outfile = open('pickle_data', 'wb')
        pickle.dump(dummy, outfile )
        outfile.close()
        print(outfile)
        return outfile


    def unpickle(self):

        encoder = pickle.load(open('encoder.pkl','rb'))
        #model = pickle.load('model.pkl')
        print(encoder)
        return encoder

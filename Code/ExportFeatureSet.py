import numpy as np
import pandas as pd
from torchtext.legacy.data import BucketIterator

class ExportFeatureSet:
  def _init_(self):
    _features=[]
    _classLabels=[]
    _maxfeatures=0

    def load_data (train_iterator):
        for batch_idx, batch in enumerate(train_iterator):
            data = batch.txt.to(device=device)
                
            targets = batch.lbl.to(device=device)
            
            # print(data)
            # print(targets)

            _t=[]
            for d in data:
                _t.append(d.item())
            
            if(len(_t)>_maxfeatures):
                _maxfeatures=len(_t)

            _features.append(_t)
            _classLabels.append(targets.item())

            return;

    def ExportFile(filename):
        exportFile=pd.DataFrame(_features)
        exportFile['labels']= _classLabels
        exportFile.to_csv('../DataSet/'+filename+'.csv')
        return;
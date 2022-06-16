#Dictionary Creator Class

class DictionaryCreator:

  def replaceSymbols(self,data):
    # print("printing data:")
    # print(data)
    data= ' '.join(data.split())
    if (data.find(',')>-1 ):
      data=data.replace(',',' [comma] ')
    if (data.find('@')>-1 ):
      data= data.replace('@',' [at] ')
    if (data.find('.')>-1 ):
      data = data.replace('.',' [dot] ')
    if (data.find('-')>-1 ):
      data=data.replace('-',' [hyphen] ')
    if (data.find(';')>-1 ):
      data=data.replace(';',' [semicolon] ')
    if (data.find(':')>-1 ):
      data=data.replace(':',' [colon] ')

    # print(data)  
    return data

  def cleaning(self,_t):
    # print("claening")
    soup = BeautifulSoup(_t, "html.parser")
    return soup.text.strip()

  def checkForPattern(self, _line,_pattern):
    # _data = re.findall(_pattern, _line) #if not using compile for regular expression pattern
    _data = _pattern.findall(_line)
    if(len(_data)>0):
      return self.cleaning(_data[0][1]) 
    return ''

  def writeDictionary(self, _token , _pattern,sourceFile):
    _token = self.replaceSymbols(_token)
    w=open(entityDictionaryPath , "a+")
    w.write( _token + ','+ _pattern +','+ sourceFile+'\n')
    w.close()

    return
  

  def CreateDictionary(self,file):
    with codecs.open(file, encoding='utf-8',errors='xmlcharrefreplace') as f:
    
      for line in f:
        for p in patterns.regExpressions.keys():
          value = self.checkForPattern(line, patterns.regExpressions[p])
          if(len(value)>0):
            self.writeDictionary(value, p, file)
            print(value)
    return ''

  def processLabeledData(self):
    files= glob.glob(htmlLabeledDataPath)
    for file in files:
        self.CreateDictionary(file)
    return 'DictionaryCreated'
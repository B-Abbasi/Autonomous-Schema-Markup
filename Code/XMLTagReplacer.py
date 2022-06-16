#XMLTagReplacer Class
class XMLTagReplacer:

  def encodeFilesWithEntityIdentifiers(self,file):
    fileName= file.split('/')[-1]
    outputFile = EntityLabeledDataPath+fileName
    print("Output:" + outputFile)
    w=open(outputFile, "w")
    with codecs.open(file, encoding='utf-8',errors='xmlcharrefreplace') as f:
      for line in f:
        for p in patterns.regExpressions.keys():
          line = patterns.regExpressions[p].sub(patterns.entityIdentifier[p],line)
        w.write(line)
      w.close()

    return ''


  def processLabeledData(self):
    files= glob.glob(htmlLabeledDataPath)
    for file in files:
        print(file)
        self.encodeFilesWithEntityIdentifiers(file)

    return 'Encoding Completed'

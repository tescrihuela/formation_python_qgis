tBrush = {'1':'NoBrush', '2':'SolidPattern', '3':'HorPattern', '4':'VerPattern',
          '5':'BDiagPattern', '6':'FDiagPattern','7':'CrossPattern','8':'DiagCrossPattern',
          '12':'Dense1Pattern', '13':'Dense2Pattern','14':'Dense3Pattern','15':'Dense4Pattern',
          '16':'Dense5Pattern', '17':'Dense6Pattern','18':'Dense7Pattern','19':'HorPattern',
          '20':'HorPattern','21':'HorPattern', '24':'VerPattern','25':'VerPattern','26':'VerPattern','29':'BDiagPattern',
          '30':'BDiagPattern','31':'BDiagPattern', '34':'FDiagPattern','35':'FDiagPattern','36':'FDiagPattern','39':'CrossPattern','40':'CrossPattern',
          '41':'CrossPattern'
         }


def PrintDic(DicGen):
    for key in DicGen.keys():
        if str(key)!="":  print(str(key)+ " : " + str(DicGen[key]))
    

PrintDic(tBrush)

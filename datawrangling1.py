import pandas as po

dmath = {'Student': ['Ice Bear','Panda','Grizzly'],
         'Math': [80,95,79]}
delecs = {'Student': ['Ice Bear','Panda','Grizzly'],
          'Electronics': [85,81,83]}
dgeas = {'Student': ['Ice Bear','Panda','Grizzly'],
          'GEAS': [90,79,93]}
desat = {'Student': ['Ice Bear','Panda','Grizzly'],
          'ESAT': [93,89,88]}

dfmath = po.DataFrame(dmath, columns = ['Student','Math'])
dfelecs = po.DataFrame(delecs, columns = ['Student','Electronics'])
dfgeas = po.DataFrame(dgeas, columns = ['Student','GEAS'])
dfdsat = po.DataFrame(desat, columns = ['Student','ESAT'])

dfme = po.merge(dfmath,dfelecs, on = 'Student')
dfgd = po.merge(dfgeas,dfdsat, on = 'Student')
dfall = po.merge(dfme,dfgd, on = 'Student')

print ("\n",dfall)
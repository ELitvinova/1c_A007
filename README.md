# Задача А007 (третий день)    
Поиск решения реализован с помощью поиска в глубину в дереве состояний. Перед поиском проводятся несколько проверок:     
+ Если сверху всех кучек лежат одинаковые карты, то невозможно сделать первый ход
+ Если все карты какого-то номинала лежат под картами меньшего номинала, то разрешить пасьянс не получится     
Во всех случаях программа выдает соответствующий ответ. Если решение найдено, то будет выдано количество ходов для этого решения (первого найденного).    
## Дальнейшие улучшения: 
+ хранить хеши состояний, а не сами состояния, чтобы использовать меньше памяти и быстрее проверять, что состояние не встречалось на пути обхода
+ использовать обход в ширину, чтобы находить кратчайший путь (а не любой)

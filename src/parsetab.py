
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN RPAREN LCOR RCOR LKEY RKEY COMMA SEMICOLON ID NUMBER STRING_LITERAL PLUS MINUS MULT DIVIDE EQUALS DIFFERENT GT GTE LT LTE MOD UMINUS OR AND NOT ASSIGN PLUSASSIGN MINUSASSIGN MULTASSIGN DIVIDEASSIGN MODASSIGN QMARK COLON IF ELSE WHILE FOR RETURN STRING INT BOOLEAN TRUE FALSE BREAK READ WRITE\n    program : decSeq\n    \n    dec : varDec\n        | ID LPAREN paramList RPAREN LKEY block RKEY\n        | type ID LPAREN paramList RPAREN LKEY block RKEY\n    \n    varDec : type varSpecSeq SEMICOLON\n    \n    varSpec : ID\n            | ID ASSIGN literal\n            | ID LCOR NUMBER RCOR\n            | ID LCOR NUMBER RCOR ASSIGN LKEY literalSeq RKEY\n    \n    type : INT\n         | STRING\n         | BOOLEAN\n    \n    param : type ID\n          | type ID RCOR LCOR\n    \n    block : varDecList stmtList\n    \n    stmt : ifStmt\n         | whileStmt\n         | forStmt\n         | breakStmt\n         | returnStmt\n         | readStmt\n         | writeStmt\n         | assign SEMICOLON\n         | subCall SEMICOLON\n    \n    ifStmt : IF LPAREN exp RPAREN LKEY block RKEY\n           | IF LPAREN exp RPAREN LKEY block RKEY ELSE LKEY block RKEY\n    \n    whileStmt : WHILE LPAREN exp RPAREN LKEY block RKEY\n    \n    forStmt : FOR LPAREN assign SEMICOLON exp SEMICOLON assign RPAREN LKEY block RKEY\n    \n    breakStmt : BREAK SEMICOLON\n    \n    readStmt : READ var SEMICOLON\n    \n    writeStmt : WRITE expList SEMICOLON\n    \n    returnStmt : RETURN SEMICOLON\n               | RETURN exp SEMICOLON\n    \n    subCall : ID LPAREN expList RPAREN\n    \n    assign : var ASSIGN exp\n           | var PLUSASSIGN exp\n           | var MINUSASSIGN exp\n           | var MULTASSIGN exp\n           | var DIVIDEASSIGN exp\n           | var MODASSIGN exp\n    \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp MULT exp\n        | exp DIVIDE exp\n        | exp MOD exp\n    \n    exp : exp EQUALS exp\n        | exp DIFFERENT exp\n        | exp LTE exp\n        | exp GTE exp\n        | exp GT exp\n        | exp LT exp\n    \n    exp : exp AND exp\n        | exp OR exp\n        | NOT exp\n        | UMINUS exp\n    \n    exp : exp QMARK exp COLON exp\n    \n    exp : subCall\n    \n    exp : var\n    \n    exp : literal\n    \n    exp : LPAREN exp RPAREN\n    \n    var : ID\n        | ID LCOR exp RCOR\n    \n    literal : NUMBER\n            | STRING_LITERAL\n            | FALSE\n            | TRUE\n    \n    paramList : paramSeq\n              | empty\n    \n    paramSeq : param\n             | param COMMA paramSeq\n    \n    varDecList : varDec varDecList\n               | empty\n    \n    varSpecSeq : varSpec\n               | varSpec COMMA varSpecSeq\n    \n    decSeq : dec\n           | dec decSeq\n    \n    stmtList : stmt stmtList\n             | empty\n    \n    literalSeq : literal\n               | literal COMMA literalSeq\n    \n    expList : expSeq\n            | empty\n    \n    expSeq : exp\n           | exp COMMA expSeq\n    empty :'
    
_lr_action_items = {'ID':([0,3,4,6,7,8,9,19,23,24,37,43,44,45,46,48,50,52,54,55,56,57,58,59,60,67,68,70,72,76,77,78,79,80,81,82,84,85,89,92,93,94,95,96,97,102,103,104,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,128,135,136,143,163,164,166,169,171,172,176,177,180,181,],[5,5,-2,12,-10,-11,-12,27,-5,36,-85,71,-85,-72,36,-85,-3,71,-16,-17,-18,-19,-20,-21,-22,71,91,71,-71,-23,-24,71,71,91,-29,-32,71,71,71,71,71,71,71,71,71,71,71,-4,-33,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-30,-31,71,71,-85,-85,71,91,-25,-27,-85,-85,-26,-28,]),'INT':([0,3,4,11,20,23,26,37,44,48,50,104,163,164,176,177,],[7,7,-2,7,7,-5,7,7,7,7,-3,-4,7,7,7,7,]),'STRING':([0,3,4,11,20,23,26,37,44,48,50,104,163,164,176,177,],[8,8,-2,8,8,-5,8,8,8,8,-3,-4,8,8,8,8,]),'BOOLEAN':([0,3,4,11,20,23,26,37,44,48,50,104,163,164,176,177,],[9,9,-2,9,9,-5,9,9,9,9,-3,-4,9,9,9,9,]),'$end':([1,2,3,4,10,23,50,104,],[0,-1,-75,-2,-76,-5,-3,-4,]),'LPAREN':([5,12,63,64,65,67,70,71,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,],[11,20,78,79,80,89,89,102,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'RPAREN':([11,15,16,17,18,20,27,28,30,31,32,33,38,47,71,86,87,88,99,100,101,102,107,108,125,126,127,129,130,131,132,133,134,137,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,170,173,],[-85,25,-67,-68,-69,-85,-13,40,-63,-64,-65,-66,-70,-14,-61,-57,-58,-59,-81,-82,-83,-85,141,142,-54,-55,158,-35,-36,-37,-38,-39,-40,160,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-60,-84,-34,-62,-56,175,]),'COMMA':([12,14,18,27,29,30,31,32,33,36,41,47,71,86,87,88,101,106,125,126,139,144,145,146,147,148,149,150,151,152,153,154,155,156,158,160,161,170,],[-6,24,26,-13,-7,-63,-64,-65,-66,-6,-8,-14,-61,-57,-58,-59,136,140,-54,-55,-9,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-60,-34,-62,-56,]),'SEMICOLON':([12,13,14,29,30,31,32,33,35,36,41,61,62,66,67,70,71,83,86,87,88,90,91,98,99,100,101,109,125,126,129,130,131,132,133,134,139,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,160,161,165,170,],[-6,23,-73,-7,-63,-64,-65,-66,-74,-6,-8,76,77,81,82,-85,-61,110,-57,-58,-59,128,-61,135,-81,-82,-83,143,-54,-55,-35,-36,-37,-38,-39,-40,-9,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-60,-84,-34,-62,169,-56,]),'ASSIGN':([12,36,41,69,71,91,161,],[21,21,49,92,-61,-61,-62,]),'LCOR':([12,36,39,71,91,],[22,22,47,103,103,]),'NUMBER':([21,22,67,70,74,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,140,143,166,],[30,34,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'STRING_LITERAL':([21,67,70,74,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,140,143,166,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FALSE':([21,67,70,74,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,140,143,166,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TRUE':([21,67,70,74,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,140,143,166,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'IF':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,63,-85,-72,-85,63,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'WHILE':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,64,-85,-72,-85,64,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'FOR':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,65,-85,-72,-85,65,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'BREAK':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,66,-85,-72,-85,66,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'RETURN':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,67,-85,-72,-85,67,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'READ':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,68,-85,-72,-85,68,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'WRITE':([23,37,43,44,45,48,52,54,55,56,57,58,59,60,72,76,77,81,82,110,128,135,163,164,171,172,176,177,180,181,],[-5,-85,70,-85,-72,-85,70,-16,-17,-18,-19,-20,-21,-22,-71,-23,-24,-29,-32,-33,-30,-31,-85,-85,-25,-27,-85,-85,-26,-28,]),'RKEY':([23,30,31,32,33,37,42,43,44,45,48,51,52,53,54,55,56,57,58,59,60,72,73,75,76,77,81,82,105,106,110,128,135,162,163,164,167,168,171,172,176,177,178,179,180,181,],[-5,-63,-64,-65,-66,-85,50,-85,-85,-72,-85,-15,-85,-78,-16,-17,-18,-19,-20,-21,-22,-71,104,-77,-23,-24,-29,-32,139,-79,-33,-30,-31,-80,-85,-85,171,172,-25,-27,-85,-85,180,181,-26,-28,]),'LKEY':([25,40,49,141,142,174,175,],[37,48,74,163,164,176,177,]),'RCOR':([27,30,31,32,33,34,71,86,87,88,125,126,138,144,145,146,147,148,149,150,151,152,153,154,155,156,158,160,161,170,],[39,-63,-64,-65,-66,41,-61,-57,-58,-59,-54,-55,161,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-60,-34,-62,-56,]),'PLUS':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,111,-57,-58,-59,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,-60,-34,-62,111,111,]),'MINUS':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,112,-57,-58,-59,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,-60,-34,-62,112,112,]),'MULT':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,113,-57,-58,-59,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,-60,-34,-62,113,113,]),'DIVIDE':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,114,-57,-58,-59,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,-60,-34,-62,114,114,]),'MOD':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,115,-57,-58,-59,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,-60,-34,-62,115,115,]),'EQUALS':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,116,-57,-58,-59,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,-60,-34,-62,116,116,]),'DIFFERENT':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,117,-57,-58,-59,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,-60,-34,-62,117,117,]),'LTE':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,118,-57,-58,-59,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,-60,-34,-62,118,118,]),'GTE':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,119,-57,-58,-59,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,-60,-34,-62,119,119,]),'GT':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,120,-57,-58,-59,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,-60,-34,-62,120,120,]),'LT':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,121,-57,-58,-59,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,-60,-34,-62,121,121,]),'AND':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,122,-57,-58,-59,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,-60,-34,-62,122,122,]),'OR':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,123,-57,-58,-59,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,-60,-34,-62,123,123,]),'QMARK':([30,31,32,33,71,83,86,87,88,101,107,108,125,126,127,129,130,131,132,133,134,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,165,170,],[-63,-64,-65,-66,-61,124,-57,-58,-59,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,-60,-34,-62,124,124,]),'COLON':([30,31,32,33,71,86,87,88,125,126,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,170,],[-63,-64,-65,-66,-61,-57,-58,-59,-54,-55,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,166,-60,-34,-62,-56,]),'NOT':([67,70,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'UMINUS':([67,70,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'PLUSASSIGN':([69,71,91,161,],[93,-61,-61,-62,]),'MINUSASSIGN':([69,71,91,161,],[94,-61,-61,-62,]),'MULTASSIGN':([69,71,91,161,],[95,-61,-61,-62,]),'DIVIDEASSIGN':([69,71,91,161,],[96,-61,-61,-62,]),'MODASSIGN':([69,71,91,161,],[97,-61,-61,-62,]),'ELSE':([171,],[174,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'decSeq':([0,3,],[2,10,]),'dec':([0,3,],[3,3,]),'varDec':([0,3,37,44,48,163,164,176,177,],[4,4,44,44,44,44,44,44,44,]),'type':([0,3,11,20,26,37,44,48,163,164,176,177,],[6,6,19,19,19,46,46,46,46,46,46,46,]),'varSpecSeq':([6,24,46,],[13,35,13,]),'varSpec':([6,24,46,],[14,14,14,]),'paramList':([11,20,],[15,28,]),'paramSeq':([11,20,26,],[16,16,38,]),'empty':([11,20,37,43,44,48,52,70,102,163,164,176,177,],[17,17,45,53,45,45,53,100,100,45,45,45,45,]),'param':([11,20,26,],[18,18,18,]),'literal':([21,67,70,74,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,140,143,166,],[29,88,88,106,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,106,88,88,]),'block':([37,48,163,164,176,177,],[42,73,167,168,178,179,]),'varDecList':([37,44,48,163,164,176,177,],[43,72,43,43,43,43,43,]),'stmtList':([43,52,],[51,75,]),'stmt':([43,52,],[52,52,]),'ifStmt':([43,52,],[54,54,]),'whileStmt':([43,52,],[55,55,]),'forStmt':([43,52,],[56,56,]),'breakStmt':([43,52,],[57,57,]),'returnStmt':([43,52,],[58,58,]),'readStmt':([43,52,],[59,59,]),'writeStmt':([43,52,],[60,60,]),'assign':([43,52,80,169,],[61,61,109,173,]),'subCall':([43,52,67,70,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,],[62,62,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,]),'var':([43,52,67,68,70,78,79,80,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,169,],[69,69,87,90,87,87,87,69,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,69,]),'exp':([67,70,78,79,84,85,89,92,93,94,95,96,97,102,103,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,143,166,],[83,101,107,108,125,126,127,129,130,131,132,133,134,101,138,144,145,146,147,148,149,150,151,152,153,154,155,156,157,101,165,170,]),'expList':([70,102,],[98,137,]),'expSeq':([70,102,136,],[99,99,159,]),'literalSeq':([74,140,],[105,162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> decSeq','program',1,'p_program','analisadorSintatico.py',24),
  ('dec -> varDec','dec',1,'p_dec','analisadorSintatico.py',31),
  ('dec -> ID LPAREN paramList RPAREN LKEY block RKEY','dec',7,'p_dec','analisadorSintatico.py',32),
  ('dec -> type ID LPAREN paramList RPAREN LKEY block RKEY','dec',8,'p_dec','analisadorSintatico.py',33),
  ('varDec -> type varSpecSeq SEMICOLON','varDec',3,'p_varDec','analisadorSintatico.py',45),
  ('varSpec -> ID','varSpec',1,'p_varSpec','analisadorSintatico.py',52),
  ('varSpec -> ID ASSIGN literal','varSpec',3,'p_varSpec','analisadorSintatico.py',53),
  ('varSpec -> ID LCOR NUMBER RCOR','varSpec',4,'p_varSpec','analisadorSintatico.py',54),
  ('varSpec -> ID LCOR NUMBER RCOR ASSIGN LKEY literalSeq RKEY','varSpec',8,'p_varSpec','analisadorSintatico.py',55),
  ('type -> INT','type',1,'p_type','analisadorSintatico.py',69),
  ('type -> STRING','type',1,'p_type','analisadorSintatico.py',70),
  ('type -> BOOLEAN','type',1,'p_type','analisadorSintatico.py',71),
  ('param -> type ID','param',2,'p_param','analisadorSintatico.py',78),
  ('param -> type ID RCOR LCOR','param',4,'p_param','analisadorSintatico.py',79),
  ('block -> varDecList stmtList','block',2,'p_block','analisadorSintatico.py',89),
  ('stmt -> ifStmt','stmt',1,'p_stmt','analisadorSintatico.py',96),
  ('stmt -> whileStmt','stmt',1,'p_stmt','analisadorSintatico.py',97),
  ('stmt -> forStmt','stmt',1,'p_stmt','analisadorSintatico.py',98),
  ('stmt -> breakStmt','stmt',1,'p_stmt','analisadorSintatico.py',99),
  ('stmt -> returnStmt','stmt',1,'p_stmt','analisadorSintatico.py',100),
  ('stmt -> readStmt','stmt',1,'p_stmt','analisadorSintatico.py',101),
  ('stmt -> writeStmt','stmt',1,'p_stmt','analisadorSintatico.py',102),
  ('stmt -> assign SEMICOLON','stmt',2,'p_stmt','analisadorSintatico.py',103),
  ('stmt -> subCall SEMICOLON','stmt',2,'p_stmt','analisadorSintatico.py',104),
  ('ifStmt -> IF LPAREN exp RPAREN LKEY block RKEY','ifStmt',7,'p_ifStmt','analisadorSintatico.py',114),
  ('ifStmt -> IF LPAREN exp RPAREN LKEY block RKEY ELSE LKEY block RKEY','ifStmt',11,'p_ifStmt','analisadorSintatico.py',115),
  ('whileStmt -> WHILE LPAREN exp RPAREN LKEY block RKEY','whileStmt',7,'p_whileStmt','analisadorSintatico.py',125),
  ('forStmt -> FOR LPAREN assign SEMICOLON exp SEMICOLON assign RPAREN LKEY block RKEY','forStmt',11,'p_forStmt','analisadorSintatico.py',132),
  ('breakStmt -> BREAK SEMICOLON','breakStmt',2,'p_breakStmt','analisadorSintatico.py',139),
  ('readStmt -> READ var SEMICOLON','readStmt',3,'p_readStmt','analisadorSintatico.py',146),
  ('writeStmt -> WRITE expList SEMICOLON','writeStmt',3,'p_writeStmt','analisadorSintatico.py',153),
  ('returnStmt -> RETURN SEMICOLON','returnStmt',2,'p_returnStmt','analisadorSintatico.py',160),
  ('returnStmt -> RETURN exp SEMICOLON','returnStmt',3,'p_returnStmt','analisadorSintatico.py',161),
  ('subCall -> ID LPAREN expList RPAREN','subCall',4,'p_subCall','analisadorSintatico.py',171),
  ('assign -> var ASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',178),
  ('assign -> var PLUSASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',179),
  ('assign -> var MINUSASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',180),
  ('assign -> var MULTASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',181),
  ('assign -> var DIVIDEASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',182),
  ('assign -> var MODASSIGN exp','assign',3,'p_assign','analisadorSintatico.py',183),
  ('exp -> exp PLUS exp','exp',3,'p_expArithmetic','analisadorSintatico.py',201),
  ('exp -> exp MINUS exp','exp',3,'p_expArithmetic','analisadorSintatico.py',202),
  ('exp -> exp MULT exp','exp',3,'p_expArithmetic','analisadorSintatico.py',203),
  ('exp -> exp DIVIDE exp','exp',3,'p_expArithmetic','analisadorSintatico.py',204),
  ('exp -> exp MOD exp','exp',3,'p_expArithmetic','analisadorSintatico.py',205),
  ('exp -> exp EQUALS exp','exp',3,'p_expComparison','analisadorSintatico.py',221),
  ('exp -> exp DIFFERENT exp','exp',3,'p_expComparison','analisadorSintatico.py',222),
  ('exp -> exp LTE exp','exp',3,'p_expComparison','analisadorSintatico.py',223),
  ('exp -> exp GTE exp','exp',3,'p_expComparison','analisadorSintatico.py',224),
  ('exp -> exp GT exp','exp',3,'p_expComparison','analisadorSintatico.py',225),
  ('exp -> exp LT exp','exp',3,'p_expComparison','analisadorSintatico.py',226),
  ('exp -> exp AND exp','exp',3,'p_expLogic','analisadorSintatico.py',244),
  ('exp -> exp OR exp','exp',3,'p_expLogic','analisadorSintatico.py',245),
  ('exp -> NOT exp','exp',2,'p_expLogic','analisadorSintatico.py',246),
  ('exp -> UMINUS exp','exp',2,'p_expLogic','analisadorSintatico.py',247),
  ('exp -> exp QMARK exp COLON exp','exp',5,'p_expTernary','analisadorSintatico.py',261),
  ('exp -> subCall','exp',1,'p_expSubCall','analisadorSintatico.py',268),
  ('exp -> var','exp',1,'p_expVar','analisadorSintatico.py',275),
  ('exp -> literal','exp',1,'p_expLiteral','analisadorSintatico.py',282),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_expMultParent','analisadorSintatico.py',289),
  ('var -> ID','var',1,'p_var','analisadorSintatico.py',296),
  ('var -> ID LCOR exp RCOR','var',4,'p_var','analisadorSintatico.py',297),
  ('literal -> NUMBER','literal',1,'p_literal','analisadorSintatico.py',307),
  ('literal -> STRING_LITERAL','literal',1,'p_literal','analisadorSintatico.py',308),
  ('literal -> FALSE','literal',1,'p_literal','analisadorSintatico.py',309),
  ('literal -> TRUE','literal',1,'p_literal','analisadorSintatico.py',310),
  ('paramList -> paramSeq','paramList',1,'p_paramList','analisadorSintatico.py',317),
  ('paramList -> empty','paramList',1,'p_paramList','analisadorSintatico.py',318),
  ('paramSeq -> param','paramSeq',1,'p_paramSeq','analisadorSintatico.py',326),
  ('paramSeq -> param COMMA paramSeq','paramSeq',3,'p_paramSeq','analisadorSintatico.py',327),
  ('varDecList -> varDec varDecList','varDecList',2,'p_varDecList','analisadorSintatico.py',337),
  ('varDecList -> empty','varDecList',1,'p_varDecList','analisadorSintatico.py',338),
  ('varSpecSeq -> varSpec','varSpecSeq',1,'p_varSpecSeq','analisadorSintatico.py',346),
  ('varSpecSeq -> varSpec COMMA varSpecSeq','varSpecSeq',3,'p_varSpecSeq','analisadorSintatico.py',347),
  ('decSeq -> dec','decSeq',1,'p_decSeq','analisadorSintatico.py',357),
  ('decSeq -> dec decSeq','decSeq',2,'p_decSeq','analisadorSintatico.py',358),
  ('stmtList -> stmt stmtList','stmtList',2,'p_stmtList','analisadorSintatico.py',368),
  ('stmtList -> empty','stmtList',1,'p_stmtList','analisadorSintatico.py',369),
  ('literalSeq -> literal','literalSeq',1,'p_literalSeq','analisadorSintatico.py',377),
  ('literalSeq -> literal COMMA literalSeq','literalSeq',3,'p_literalSeq','analisadorSintatico.py',378),
  ('expList -> expSeq','expList',1,'p_expList','analisadorSintatico.py',388),
  ('expList -> empty','expList',1,'p_expList','analisadorSintatico.py',389),
  ('expSeq -> exp','expSeq',1,'p_expSeq','analisadorSintatico.py',397),
  ('expSeq -> exp COMMA expSeq','expSeq',3,'p_expSeq','analisadorSintatico.py',398),
  ('empty -> <empty>','empty',0,'p_empty','analisadorSintatico.py',407),
]

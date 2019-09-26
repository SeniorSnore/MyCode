### Translate the following string by moving each character to ASCII places
### For example:
###     K -> M
###     O -> Q
###     E -> G
### String:  g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

### use ord function to get ASCII value

OriginalText="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
  i=0
NewText =""

while i < len(OriginalText):
    if  (ord(OriginalText[i]) < 97) or (ord(OriginalText[i]) > 122):
        charstr = OriginalText[i]
    elif (OriginalText[i] == "y"):
        charstr = "a"
    elif (OriginalText[i] == "z"):
        charstr = "b"
    elif (OriginalText[i] != " "):
        charint = ord(OriginalText[i]) + 2
        charstr = chr(charint)
    else :
            charstr = OriginalText[i]
    i=i+1
    NewText = NewText + charstr
print (NewText)
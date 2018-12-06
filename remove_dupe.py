def remove_dupe(str):
    strlst = list(str)
    str1 = " "
    for letter in strlst:
        if letter not in str1:
            str1 += letter
        
        
    print(str1)
   

remove_dupe("pneumonoultramicroscopicsilicovolcanoconiosis")



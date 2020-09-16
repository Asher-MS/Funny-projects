file=open("Word_list_of_5.txt","a")


alphabet=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for i in range(0,26):
    for j in range(0,26):
        for k in range(0,26):
            for l in range(0,26):
                for m in range(0,26):
                

                 str=alphabet[i]+alphabet[j]+alphabet[k]+alphabet[l]+alphabet[m]
                 print("PLEASE WAITT")
                 file.write(str)
                 file.write("\n")
file.close()

#188&DropDownList2=1' --compressed
f = open ('bihar_parts.txt')
prefix = f.read()
for i in range(243):
    line = prefix.strip('\n') + str(i) + "&DropDownList2=1' --compressed >" + str(i) + '.html'
    filename = 'bihar_curl_' + str(i) + '.sh'
    r = open(filename,'w')
    r.write(line)
    r.close()


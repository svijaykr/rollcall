def p():
    f = open('assam_master_list.txt','r')
    g = open('filenames.txt','r')
    l1 = f.readlines()
    l2 = g.readlines() 
    for i in xrange(len(l1)):
        print "curl '", l1[i].strip('\n'), "' > ", l2[i].strip('\n')

if __name__ == '__main__':
    p()
    

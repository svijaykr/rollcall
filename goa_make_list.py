f = open('goa_master_list.txt','r')
prefix = 'http://ceogoa.nic.in/PDF/EROLL/2015/AC'
suffix1 = '/Part'
suffix2 = '.pdf'
for lines in f:
    (cons_id, last_no) = lines.strip('\n').split()
    for i in xrange(1,int(last_no)):
        print prefix + cons_id + suffix1 + str(i)  + suffix2

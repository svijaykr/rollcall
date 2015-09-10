f = open('goa_seed.txt','r')
prefix = 'http://ceogoa.nic.in/PDF/EROLL/2015/AC'
suffix1 = '/Part'
suffix2 = '.pdf'
for lines in f:
    (cons_id, last_no) = lines.strip('\n').split()
    for i in xrange(1,int(last_no)):
        if i < 10:
            part_no  = '0' + str(i)
        else:
            part_no = str(i)
        print prefix + cons_id + suffix1 + part_no  + suffix2

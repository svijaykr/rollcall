import sys 

def make_chunk(lines,noOfLines,noOfProcesses):
    filesPerProcess = noOfLines / noOfProcesses 
    balance = noOfLines % noOfProcesses
    chunk = []
    chunks = []
    c = 1
    for i in range(noOfLines):
        if c < filesPerProcess:
            chunk.append(lines[i])
            c += 1
        else:
            chunk.append(lines[i])
            chunks.append(chunk)
            chunk = []
            c = 1
    chunks.append(chunk)
    return chunks

def write_chunk(chunk, chunkFileName):
    f = open(chunkFileName,'w')
    for lines in chunk:
        f.write(lines)
    f.close()

def read_master_file(fname):
    f = open(fname,'r')
    return f.readlines()


if __name__ == '__main__':
    print sys.argv
    lines = read_master_file(sys.argv[1])
    noOfProcesses = int(sys.argv[2])
    chunks = make_chunk(lines, len(lines),noOfProcesses)
    for i,chunk in enumerate(chunks):
        write_chunk(chunk,'tmp_chunk'+ str(i) + '.txt')




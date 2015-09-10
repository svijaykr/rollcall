import sys 
import urllib2

def fetch_list(file_name):
    f = open(file_name)
    for line in f:
        line = line.strip('\n')
        contents = fetch_single_file(line)
        if contents is not None:
            file_name = make_output_file_name(line)
            write_single_file(file_name, contents)
            print line, ": DONE"
        else:
            print line, ": FAILED"
    f.close()

def fetch_single_file(url):
    SUCCESS = 200
    f = urllib2.urlopen(url)
    content = f.read()
    code = f.getcode()
    if (code != SUCCESS):
        return None
    return content

def make_output_file_name(url):
    url_parts = url.split('/')
    file_name = url_parts[len(url_parts) - 1]
    return file_name

def write_single_file(file_name,content):
    f = open(file_name,'w')
    f.write(content)
    f.close()

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

def write_chunk(chunk, chunk_file_name):
    f = open(chunk_file_name,'w')
    for lines in chunk:
        f.write(lines)
    f.close()

def read_master_file(fname):
    f = open(fname,'r')
    return f.readlines()

def apportion():
    lines = read_master_file(sys.argv[1])
    noOfProcesses = int(sys.argv[2])
    chunks = make_chunk(lines, len(lines),noOfProcesses)
    out_file_list = []
    for i,chunk in enumerate(chunks):
        out_file_name = 'tmp_chunk'+ str(i) + '.txt'
        write_chunk(chunk,out_file_name)
        out_file_list.append(out_file_name)
    return out_file_list


if __name__ == '__main__':
    out_file_list = apportion()
    fetch_list(out_file_list[0])

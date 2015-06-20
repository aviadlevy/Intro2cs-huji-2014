from sllist import SkipiNode as Node

def refresh(base_list):
    for i in range(len(base_list)):
        base_list[i].skip_back = base_list[i-2] if i>1 else None
        base_list[i].next = base_list[i+1] if i<len(base_list)-1 else None
    return base_list

def data_to_nodelist(datalist):
    return refresh([Node(d) for d in datalist])

def sklist_to_list(skl):
    l = []
    for n in iter_sklist(skl):
        if n in l:
            break
        else:
            l.append(n)
    return l



ctor_tests = [refresh(bl) for bl in [[Node(1)],[Node(1),Node(2)],[Node(1),Node(2),Node(3)],[Node(1),Node(2),Node(3),Node(4)]]]


ctor = ([('SkipiList',[],{},None)] +
        [('SkipiList',[],{'_nlist':t},None) for t in ctor_tests])


data1 = list('abcdefghijklmnopqrstuvwxyz')

data2 = list(range(10))

addseqsets = ([(data[:i],data[i:j]) for data in (data1,data2) for i in range(len(data)-1) for j in range(i+1,len(data))])

addfirst = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[1],'_func':'add_first'},[None]*len(d[1])) for d in addseqsets])

addlast = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[1][::-1],'_func':'add_last'},[None]*len(d[1])) for d in addseqsets])

remseqsets = ([(data[:i],j) for data in (data1,data2) for i in range(1,len(data)) for j in range(1,i)])

removefirst = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[0][:d[1]],'_func':'remove_first'},d[0][:d[1]]) for d in remseqsets])

removelast = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[0][-d[1]:],'_func':'remove_last'},d[0][-d[1]:][::-1]) for d in remseqsets])

remnodesets = ([(data[:i],j) for data in (data1,data2) for i in range(1,len(data)) for j in range(i)])

removenode = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[1],'_func':'remove_node'},[d[0][d[1]]]) for d in remnodesets])

getitemgoodsets = ([(data[:i],j) for data in (data1,data2) for i in range(1,len(data)) for j in range(-i,i)])
getitembadsets = ([(data[:i],j) for data in (data1,data2) for i in range(1,len(data)) for j in list(range(-i-4,-i))+list(range(i,i+4))])

skgetitemg = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[1],'_func':'getitem_g'},[d[0][d[1]]]) for d in getitemgoodsets])
skgetitemb = ([('SkipiList',[],{'_nlist':data_to_nodelist(d[0]),'_argseq':d[1],'_func':'getitem_b'},[]) for d in getitembadsets])

def makedict(l):
    return {name:eval(name) for name in l}

kset = makedict([
        'ctor',
        'addfirst',
        'addlast',
        'removefirst',
        'removelast',
        'removenode',
        'skgetitemg',
        'skgetitemb'
        ])


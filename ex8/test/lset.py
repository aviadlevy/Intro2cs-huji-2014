from operator import attrgetter

from sllist import List,Node

def iter_sllist(sll):
    cur = sll.head
    while cur:
        yield cur
        cur = cur.next

def sllist_to_list(sll):
    l = []
    for n in iter_sllist(sll):
        if n in l:
            break
        else:
            l.append(n)
    return l

def data_to_sllist(iterable):
    temp_node = Node(None)
    cur_node = temp_node
    for data in iterable:
        cur_node.next = Node(data)
        cur_node = cur_node.next
    sll = List()
    sll.head = temp_node.next
    return sll

# following methods modify underlying lists

def refresh_node_list(l):
    for i in range(len(l)-1):
        l[i].next = l[i+1]
    if l:
        l[-1].next = None


def add_cycle(sll,index):
    l = sllist_to_list(sll)
    l[-1].next = l[index]
    return sll

def add_intersection(sll1,sll2,index):
    l1 = sllist_to_list(sll1)
    l2 = sllist_to_list(sll2)
    if l1:
        l1[-1].next = l2[index]
    else:
        sll1.head = l2[index]
    return sll1,sll2

cycle = [('contains_cycle',[List()],{},False),
         ('contains_cycle',[data_to_sllist(['abc'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc','def'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc','def','ghi','jkl','mno'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc','def','abc','def','abc'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc','def','ghi','jkl','mno','pqr'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc','def','abc','def','abc','def'])],{},False),
         ('contains_cycle',[data_to_sllist(['abc']*1000)],{},False),
         ('contains_cycle',[data_to_sllist(['abc']*1001)],{},False),
         ('contains_cycle',[data_to_sllist(['abc']*10000)],{},False),
         ('contains_cycle',[data_to_sllist(['abc']*10001)],{},False),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']),0)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc','def']),0)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc','def']),1)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc','def','ghi','jkl','mno']),1)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc','def','abc','def','abc','def']),4)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1000),0)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1001),0)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1000),999)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1001),1000)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1000),500)],{},True),
         ('contains_cycle',[add_cycle(data_to_sllist(['abc']*1001),500)],{},True),
         ]

pal_data = [[],
            ["abcd"],
            ["abcd","abcd"],
            ["abcd","efgh"],
            ["abcd","efgh","ijkl"],
            ["abcd","efgh","efgh"],
            ["abcd","abcd","efgh"],
            ["abcd","efgh","abcd"],
            ["abcd","abcd","abcd"],
            ["abcd","efgh","ijkl","abcd"],
            ["abcd","efgh","efgh","ijkl"],
            ["abcd","efgh","efgh","abcd"],
            ["abcd","abcd","abcd","abcd"],
            ["abcd","efgh"]*2,
            ["a"]*250+["b"]*500+["a"]*250,
            ["a"]*250+["b"]*250+['a']+["b"]*249+["a"]*250,
            ["a"]*251+["b"]*499+["a"]*250,
            ["a"]*250+["b"]*501+["a"]*250,
            ["a"]*250+["b"]*250+['a']+["b"]*250+["a"]*250,
            ["a"]*250+["b"]*500+["a"]*251,
            ]

palindrome = [('is_palindrome',[data_to_sllist(d)],{},d==d[::-1]) for d in pal_data]

int_no_data = [([],[]),
               ([],["a","b","c","d"]),
               (["a","b","c","d"],[]),
               (["a","b","c","d"],["a","b","c","d"]),
               (["a","b","c","d"],["b","c","d"]),
               (["a"],["a","b","c","d"]),
               (["a"]*100,["a"]*100),
               (["a"]*100,["b"]*200),
               (["a"]*100,["a"]*200),
               ]

int_yes_data = [([],["a","b","c","d"],0),
                ([],["a","b","c","d"],2),
                ([],["a","b","c","d"],3),
                (["a","b","c","d"],["e","f","g","h"],1),
                (["a"],["e","f","g","h"],1),
                (["a"],["e","f","g","h"],3),
               (["a"]*100,["a"]*100,30),
               (["a"]*100,["b"]*200,190),
               (["a"]*100,["a"]*200,20),
                ]

intersect = ([('have_intersection',[List()]*2,{},False),
              ('have_intersection',[data_to_sllist(['a','b','c','d','e'])]*2,{},True),
              ] + 
             [('have_intersection',d,{},False) for d in int_no_data] +
             [('have_intersection',list(add_intersection(data_to_sllist(d[0]),
                                                         data_to_sllist(d[1]),
                                                         d[2])),{},True) for d in int_yes_data])

intersect = ([('have_intersection',[List()]*2,{},False),
              ('have_intersection',[data_to_sllist(['a','b','c','d','e'])]*2,{},True),
              ] +
             [('have_intersection',[data_to_sllist(d[0]),data_to_sllist(d[1])],{},False) for d in int_no_data] +
             [('have_intersection',list(add_intersection(data_to_sllist(d[0]),
                                                         data_to_sllist(d[1]),
                                                         d[2])),{},True) for d in int_yes_data])

rev_data = [data_to_sllist([]),
            data_to_sllist(["hij"]),
            data_to_sllist(["abc","hij"]),
            data_to_sllist(["hij","abc"]),
            data_to_sllist(["a","b","c"]),
            data_to_sllist(["b","c","a"]),
            data_to_sllist(["a"]*250+["b"]*83+["c"]*167+["d"]*500),
            data_to_sllist(["a"]*250+["b"]*83+["c"]*167+["d"]*501),
            data_to_sllist(["d"]*250+["b"]*83+["c"]*167+["a"]*500),
            data_to_sllist(["d"]*250+["b"]*83+["c"]*167+["a"]*501),
            ]

reverse = [('reverse',[d],{'_ans':list(reversed(sllist_to_list(d)))},None) for d in rev_data]

mrg_data = [([],[]),
            ([],["abc","def"]),
            (["abc","def"],[]),
            ([tuple(s) for s in "aa"],[tuple(s) for s in "aa"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "aa"]),
            ([tuple(s) for s in "aa"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "aa"],[tuple(s) for s in "bb"]),
            ([tuple(s) for s in "bb"],[tuple(s) for s in "aa"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "aa"],[tuple(s) for s in "bc"]),
            ([tuple(s) for s in "bc"],[tuple(s) for s in "aa"]),
            ([tuple(s) for s in "ac"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "ac"]),
            ([tuple(s) for s in "bb"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "bb"]),
            ([tuple(s) for s in "bb"],[tuple(s) for s in "ac"]),
            ([tuple(s) for s in "ac"],[tuple(s) for s in "bb"]),
            ([tuple(s) for s in "bc"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "bc"]),
            ([tuple(s) for s in "bc"],[tuple(s) for s in "ac"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "cc"]),
            ([tuple(s) for s in "cc"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "ac"],[tuple(s) for s in "bc"]),
            ([tuple(s) for s in "bc"],[tuple(s) for s in "ad"]),
            ([tuple(s) for s in "cd"],[tuple(s) for s in "ab"]),
            ([tuple(s) for s in "ac"],[tuple(s) for s in "bd"]),
            ([tuple(s) for s in "bd"],[tuple(s) for s in "ac"]),
            ([tuple(s) for s in "ab"],[tuple(s) for s in "cd"]),
            ([tuple(s) for s in "ad"],[tuple(s) for s in "bc"]),
            ([(123+i,) for i in range(100)],[(223+i,) for i in range(100)]),
            ([(223+i,) for i in range(100)],[(123+i,) for i in range(100)]),
            ([(173+i,) for i in range(10)],[(123+i,) for i in range(100)]),
            ([(123+4*i,) for i in range(100)],[(223+2*i,) for i in range(10)]),
            ([(123+4*i,) for i in range(100)],[(224+2*i,) for i in range(10)]),
            ]

mrg_common = [(123+4*i,) for i in range(100)]

mergelist = ([('merge_lists',[List()]*2,{},[])] +
             [('merge_lists',[data_to_sllist(s) for s in d],{},sorted(d[0]+d[1])) for d in mrg_data] +
             [('merge_lists',[data_to_sllist(mrg_common)]*2,{},sorted(mrg_common*2))])

sort_data = [data_to_sllist([]),
             data_to_sllist(["abc"]),
             data_to_sllist(["abc","def"]),
             data_to_sllist(["def","abc"]),
             data_to_sllist(["abc","abc"]),
             data_to_sllist(["a","b","c"]),
             data_to_sllist(["a","c","b"]),
             data_to_sllist(["a","b","b"]),
             data_to_sllist(["b","b","c"]),
             data_to_sllist(["a","b","a"]),
             data_to_sllist(["c","b","c"]),
             data_to_sllist(["c","b","a"]),
             data_to_sllist(["a","c","b"]),
             data_to_sllist([(333+i)%1000 for i in range(100)]),
             data_to_sllist([(444)%1000 for i in range(128)]),
             data_to_sllist([(555-i)%1000 for i in range(100)]),
             data_to_sllist([(666+31*i)%1000 for i in range(100)]),
             data_to_sllist([(66+31*i)%100 for i in range(100)]),
             data_to_sllist([(66+(i*(i+1)//2)+31*i)%100 for i in range(100)]),
    ]

mergesort = [('merge_sort',[d],{'_ans':sorted(sllist_to_list(d),key=attrgetter('data'))},None) for d in sort_data]

get_good_data = [('a',0),
                  ('a',-1),
                  ('cb',0),
                  ('cb',1),
                  ('cb',-1),
                  ('cb',-2),
                  ('def',0),
                  ('def',1),
                  ('def',2),
                  ('def',-1),
                  ('def',-2),
                  ('def',-3),
                  ('ghijkponml',0),
                  ('ghijkponml',1),
                  ('ghijkponml',2),
                  ('ghijkponml',3),
                  ('ghijkponml',4),
                  ('ghijkponml',5),
                  ('ghijkponml',6),
                  ('ghijkponml',7),
                  ('ghijkponml',8),
                  ('ghijkponml',9),
                  ('ghijkponml',-1),
                  ('ghijkponml',-2),
                  ('ghijkponml',-3),
                  ('ghijkponml',-4),
                  ('ghijkponml',-5),
                  ('ghijkponml',-6),
                  ('ghijkponml',-7),
                  ('ghijkponml',-8),
                  ('ghijkponml',-9),
                  ('ghijkponml',-10),
                  ]

get_bad_data = [('',0),
                 ('',1),
                 ('',-1),
                  ('a',1),
                  ('a',2),
                  ('a',3),
                  ('a',-2),
                  ('a',-3),
                  ('a',-4),
                  ('cb',2),
                  ('cb',3),
                  ('cb',20),
                  ('cb',-3),
                  ('cb',-4),
                  ('cb',-20),
                  ('def',3),
                  ('def',4),
                  ('def',-4),
                  ('def',-5),
                  ('ghijkponml',10),
                  ('ghijkponml',11),
                  ('ghijkponml',100),
                  ('ghijkponml',-11),
                  ('ghijkponml',-12),
                  ('ghijkponml',-100),
                  ]

slgetitemg = ([('get_item',[data_to_sllist(d[0]),d[1]],{},d[0][d[1]]) for d in get_good_data])

slgetitemb = ([('get_item',[data_to_sllist(d[0]),d[1]],{},None) for d in get_bad_data])

slc_data = ['','a','cb','def','ijknml']
slc_data = [list(s) for s in ['','a','cb','def','ijknml']]

slice = ([('slice',[data_to_sllist(d),start,stop,step],{},d[start:stop:step]) for d in slc_data for start in range(-len(d)-2,len(d)+2) for stop in range(-len(d)-2,len(d)+2,3) for step in (-3,-1,1,3) ] +
         [('slice',[data_to_sllist(d),start,stop,step],{},d[start:stop:step]) for d in slc_data for stop in range(-len(d)-2,len(d)+2) for start in range(-len(d)-2,len(d)+2,3) for step in (-3,-1,1,3) ] +
         [('slice',[data_to_sllist(d),start,stop],{},d[start:stop]) for d in slc_data for start in range(-len(d)-2,len(d)+2) for stop in range(start-1,len(d)+2,3) ] +
         [('slice',[data_to_sllist(d),start,stop],{},d[start:stop]) for d in slc_data for start in range(-len(d)-2,len(d)+2) for stop in range(-len(d)-2,-start+2,3) ] +
         [('slice',[data_to_sllist(d),start,stop],{},d[start:stop]) for d in slc_data for stop in range(-len(d)-2,len(d)+2) for start in range(stop-2,len(d)+2,3) ] +
         [('slice',[data_to_sllist(d),start,stop],{},d[start:stop]) for d in slc_data for stop in range(-len(d)-2,len(d)+2) for start in range(-stop-2,2,3) ] +
         [('slice',[data_to_sllist(d),stop],{},d[:stop]) for d in slc_data for stop in range(-len(d)-2,len(d)+2) ])


def makedict(l):
    return {name:eval(name) for name in l}

lset = makedict([
        'cycle',
        'palindrome',
        'intersect',
        'mergelist',
        'slgetitemg',
        'slgetitemb',
        'slice',
        ])

mset = makedict([
                 'reverse',
                 'mergesort',
                 ])


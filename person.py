class person:
    def __init__(
        self,
        name, #string
        birthplace=None, #string
        birthday=None, #string
        mom=None, #person
        dad=None, #person
        partner=None, #person
        children=None, #person lista
        sources=None, #string lista
        job=None, #string
        info=None #string lista
    ):
        self.name = name
        self.birthplace = birthplace
        self.birthday = birthday
        self.mom = mom
        self.dad = dad
        self.partner = partner
        self.children = children
        self.sources = sources
        self.job = job
        self.info = info

    def find_regex(self,regex):
        found = False
        if self.name != None and regex.lower() in self.name.lower():
            found = True
        if self.birthday != None and regex.lower() in self.birthday.lower():
            found = True
        if self.birthplace != None and regex.lower() in self.birthplace.lower():
            found = True
        if self.job != None and regex.lower() in self.job.lower():
            found = True
        if self.info != None and regex.lower() in self.info.lower():
            found = True
        if self.sources != None and regex.lower() in self.sources.lower():
            found = True
        return found

    def to_string_none(x):
        if x == None:
            return 'Okand'
        return x

    def to_string(self):
        return f'{self.name}, {to_string_none(self.birthplace)}, {to_string_none(self.birthday)}'

    def to_string_rec(self):
        assert False, 'Not implemented'

    def string_list_pretty(lst):
        lengths = [0]*max(len(l) for l in lst)
        for l in lst:
            for i,x in enumerate(l):
                lengths[i] = max(lengths[i],len(x))
        out = []
        for l in lst:
            o = ''
            for i,x in enumerate(l):
                o += (x + ' '*(lengths[i]+2-len(x)))
            out.append(o)
        return out

    def get_info(self):
        string_list_pretty([
        ['Namn:', self.name],
        ['Fodelseort:', to_string_none(self.birthplace)],
        ['Fodelsedag:', to_string_none(self.birthday)],
        ['Mor:', mom.to_string() if mom != None else 'Okand'],
        ['Far:', dad.to_string() if dad != None else 'Okand'],
        ['Partner:', partner.to_string() if partner != None else 'Okand'],
        ['Barn:', ','.join([child.to_string() for child in children]) if children != None else 'Okand'],
        ['Jobb:', to_string_none(self.job)],
        ['Info:', ';'.join(self.info) if self.info != None else ''],
        ['Kallor:', ';'.join(self.sources) if self.sources != None else '']
        ])

    def print_info(self):
        print('\n'.join(get_info(self)))

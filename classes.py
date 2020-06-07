class Course:

    def __init__(self, Id, name, VH, correlatives):
        self.Id = Id
        self.name = name
        self.VH = VH
        self.correlatives = correlatives
        
        self.correlatives2 = correlatives.copy()
        
        self.assigned = False
        self.depth = 1
        self.eligibility = False

        if self.correlatives[0] == '–':
            self.eligibility = True
            self.correlatives2.remove('–')
        
        else:
            self.eligibility = False
        
        if '*' in self.name:
            self.depth = 1
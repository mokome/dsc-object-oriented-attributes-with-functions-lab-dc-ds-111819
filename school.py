class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
        
    def add_student(self, name, grade_level):
        if self.roster.get(grade_level): self.roster[grade_level].append(name)
        else: self.roster[grade_level] = [name]
        # self.roster[grade_level] = self.roster.get(grade_level, [name]).append(name)
        
    def grade(self, grade_level):
        return self.roster.get(grade_level, [])
    
    def sort_roster(self):
        for g in self.roster:
            self.roster[g].sort()
        
        return self.roster
        
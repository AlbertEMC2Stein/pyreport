class classproperty:
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)
    

#####################################################################


class Switch:
    def __init__(self, name, option1, option2):
        self.name = name
        self.option1 = option1
        self.option2 = option2
        self.current = option1

    def toggle(self):
        if self.current == self.option1:
            self.current = self.option2
        else:
            self.current = self.option1

    def __call__(self):
        return self.current
    

#####################################################################


class ReportMaker:
    def __init__(self, report_name):
        self.report_name = report_name
        self.report = open(report_name, "w")

    def make(self):
        print("Making report...")
        raise NotImplementedError("This method is not yet available.")
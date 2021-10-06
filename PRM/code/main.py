from math import floor, ceil, lcm

class shin2003:
    def __init__(self,):
        self.tree = None

class task_model:
    def __init__(self, p, e):
        self.p = p ## Period
        self.e = e ## execution time requirement
        self.utilization = e / p

class schuduling_model(task_model):
    '''
    A scheduling model can also be a task for a higher-level scheduling model.
    '''
    def __init__(self, algorithm, resource):
        self.workload = []  ## a list of tasks
        self.resource = resource
        if algorithm in ['edf', 'rm']:
            self.algorithm = algorithm
        else:
            raise("algorithm must in ['edf', 'rm'].")
        
    def dbf(self, t):
        if self.algorithm == 'edf':
            return sum([floor(self.t / i.p) * i.e for i in self.workload])
        elif self.algorithm == 'rm':
            return 
            
    def ldbf(self, t):
        if self.algorithm == 'edf':
            return self.utilization * t    
        elif self.algorithm == 'rm':
            pass

    def schedulable(self):
        for i in range(1, 2 * lcm(*[x.p for x in self.workload])+1):
            if self.dbf(i) > self.resource.sbf(i):
                return False
        return True

    

class periodic_resource_model:
    def __init__(self, pi, theta):
        self.Pi = pi ## Period
        self.Theta = theta ## resource guarantee
        self.capacity = theta / pi

    def sbf(self, t):
        temp = floor((t - (self.Pi - self.Theta)) / self.Pi)
        epsilon = max(t - 2*(self.Pi - self.Theta) - self.Pi * temp, 0)
        return temp * self.Theta + epsilon
    
    def lsbf(self, t):
        return self.Theta / self.Pi * (t - 2 * (self.Pi - self.Theta))

if __name__ == '__main__':
    test = periodic_resource_model(5, 3)
    for i in range(1, 15):
        print(i, test.sbf(i), test.lsbf(i))
    print(test.capacity)
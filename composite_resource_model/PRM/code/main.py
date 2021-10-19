from math import floor, ceil, lcm

class shin2003:
    def __init__(self,):
        self.tree = None

class task_model:
    def __init__(self, p, e):
        self.p = p ## Period
        self.e = e ## execution time requirement
        self.priority = 1 / p ## priority for RM model
        self.utilization = e / p

class schuduling_model(task_model):
    '''
    A scheduling model can also be a task for a higher-level scheduling model.
    '''
    def __init__(self, algorithm, resource, workload):
        ## a list of tasks sorted by priority
        self.workload = sorted(workload, key=lambda x:x.priority, reverse=True)
        self.resource = resource
        if algorithm in ['edf', 'rm']:
            self.algorithm = algorithm
        else:
            raise("algorithm must in ['edf', 'rm'].")
        
    def dbf(self, t):
        if self.algorithm == 'edf':
            return sum([floor(self.t / i.p) * i.e for i in self.workload])
    
    # def tbf(self, e):
    #     temp = self.
    #     # if self.algorithm == 'rm':
    #     #     result = []
    #     #     for i in sorted(self.workload, key=lambda x:x.priority, reverse=True):
    #     #         result.
            
    def ldbf(self, t):
        if self.algorithm == 'edf':
            return self.utilization * t    
        elif self.algorithm == 'rm':
            pass

    def schedulable(self):
        if self.algorithm == 'edf':
            for i in range(1, 2 * lcm(*[x.p for x in self.workload])+1):
                if self.dbf(i) > self.resource.sbf(i):
                    return False
            return True
        # ------- I am not sure my understanding of RM bound is correct
        # elif self.algorithm == 'rm':
        #     temp = []
        #     for i, v in enumerate(self.workload):
        #         temp.append(v.e + sum([x / self.workload[ii].p * self.workload[ii].e
        #          for ii, x in enumerate(temp)]))
        #         if self.resource.tbf()

    

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

    def tbf(self, theta):
        if theta - self.Theta * floor(theta / self.Theta) > 0:
            temp = self.Pi - self.Theta + theta - self.Theta * floor(theta / self.Theta)
        else:
            temp = 0
        return self.Pi - self.Theta + self.Pi * floor(theta / self.Theta) + temp
    
    def ltbf(self, theta):
        return self.Pi / self.Theta * theta + 2 * (self.Pi - self.Theta)


if __name__ == '__main__':
    test = periodic_resource_model(5, 3)
    for i in range(1, 15):
        print(i, test.sbf(i), test.lsbf(i))
    print(test.capacity)
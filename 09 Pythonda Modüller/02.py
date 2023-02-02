import random 
print(dir(random))
"""
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', 
'_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
"""
print(random.random()*100)
print(random.uniform(60, 100)) # from to
print(random.randint(60, 100))
names=["ahmad","ali","khaled","huseyin"]
print(names[random.randint(0, len(names)-1)])
print(random.choice(names))
print(random.choice("Hello World"))
l1=list(range(10))
print(l1)
random.shuffle(l1)
print(l1)
l2=range(100)
res=random.sample(l2, 10)
print("**",res)
l3=[0,1]
for i in range(16-1):
    print(random.sample(names, 4))
for i in range(4):
    print(random.sample(l3, 2))
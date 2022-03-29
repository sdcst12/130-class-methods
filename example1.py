#!python3

class example:
    var1 = 10
    var2 = "hello"
    total = 0

    @classmethod
    def run(cls):
        print( cls.var1 )
        print( cls.var2 )
    
    @classmethod
    def sum(cls,a,b):
        cls.total = a + b
        return

if __name__ == "__main__":
    example.run()
    example.sum(3,4)
    print(example.total)
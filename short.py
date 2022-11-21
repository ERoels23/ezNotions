def run():
    class customClass:
        def classFunc(self):
            y = 2
            return y
    class uncustomClass:
        def unclassFunc(self):
            y = 1
            return y
    
    z = customClass()
    zz = uncustomClass()
    a = z.classFunc()
    aa = zz.unclassFunc()

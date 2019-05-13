import prefunction

class Control(object):

    temp = 0
    settemp = 1
    @prefunction.Check(temp = temp, settemp= settemp)
    def function(self, *args, **kwargs):
        #self.result = self.kwargs['result']
        if True:
            print 'Heater Turn ON'
        else:
            print 'Heater Turn OFF'

if __name__ == '__main__':
    print 'Initial'
    main = Control()
    main.function()
    print 'Finished'
    
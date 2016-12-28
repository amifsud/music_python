from hook import HookManager

class MyHook(HookManager):
    def __init__(self):
        HookManager.__init__(self)
        self.stack=()
        
        self.KeyDown = self.keyDownCallback
        self.KeyUp = self.keyUpCallback 
        
        self.start()
        
    def keyDownCallback(self, event):
        self.stack = self.stack + (event,)   
        
    def keyUpCallback(self, event):
        self.stack = self.stack + (event,) 

    def ckeanStack(self):
        self.stack = ()        
   
if __name__ == '__main__':
    
    hm = MyHook()
 

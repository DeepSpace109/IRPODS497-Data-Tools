import BackEnd
    
class Utils(BackEnd.BackEnd):
    def __init__(self,filename:str) -> None:
        super().__init__(filename)

    def filterDataBy(self,column:str, value:str):
        return self.df[self.df[column]==value]
class Wrapper:
    def wrap(this, string, length):
        if len(string) <= length:
            return string
        
        if " " not in string:
            string = string[0:length]+"\n"+string[length:len(string)]
            return string
            
        string=string.replace(" ","\n")
            
            
        return string
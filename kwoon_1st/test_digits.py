import unittest        

class TestForDigits(unittest.TestCase):
    
    def test_two(self):
        display=SegmentDisplay()
        self.assertEqual(display.show(2),[["._."],
                                          ["._|"],
                                          ["|_."]])
    def test_three(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(3),[["._."],
                                    ["._|"],
                                    ["._|"]])
    def test_four(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(4),[["..."],
                                    ["|_|"],
                                    ["..|"]])
                                    
    def test_five(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(5),[["._."],
                                    ["|_."],
                                    ["._|"]])
    def test_six(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(6),[["._."],
                                    ["|_."],
                                    ["|_|"]])
                                    
    def test_seven(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(7),[["._."],
                                    ["..|"],
                                    ["..|"]])
                                    
    def test_eight(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(8),[["._."],
                                    ["|_|"],
                                    ["|_|"]])
                                    
    def test_nine(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(9),[["._."],
                                    ["|_|"],
                                    ["..|"]])  
    def test_zero(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(0),[["._."],
                                    ["|.|"],
                                    ["|_|"]])     
                                    
    def test_one(self):
        d = SegmentDisplay()
        self.assertEqual(d.show(1),[["..."],
                                    ["..|"],
                                    ["..|"]])                                                                                                     
                                    
    def test_two_digits(self):
        d= SegmentDisplay()
        self.assertEqual(d.show(10),[["...","._."],
                                     ["..|","|.|"],
                                     ["..|","|_|"]])
                                     
    def test_three_digits(self):
        d= SegmentDisplay()
        self.assertEqual(d.show(123),[["...","._.","._."],
                                      ["..|","._|","._|"],
                                      ["..|","|_.","._|"]])
        
        
        
        
class SegmentDisplay:
    def show(self,integer):
        dict = {
                0:[["._."],
                    ["|.|"],
                    ["|_|"]],
                1:[["..."],
                    ["..|"],
                    ["..|"]],
                2:[["._."],
                   ["._|"],
                   ["|_."]],
                3:[["._."],
                   ["._|"],
                   ["._|"]],
                4:[["..."],
                   ["|_|"],
                   ["..|"]],
                5:[["._."],
                   ["|_."],
                   ["._|"]],
                6:[["._."],
                   ["|_."],
                   ["|_|"]],
                7:[["._."],
                   ["..|"],
                   ["..|"]],
                8:[["._."],
                   ["|_|"],
                   ["|_|"]],
                9:[["._."],
                   ["|_|"],
                   ["..|"]]              
                }
                
        if (integer < 10):
            return dict[integer]
        
        elif (integer >= 10 and integer < 100):
            integer_first = integer / 10;
            list_first = dict[integer_first]
            
            integer_last = integer % 10;
            list_last = dict[integer_last]
            
            list_first[0] += list_last[0]
            list_first[1] += list_last[1]
            list_first[2] += list_last[2]
            
        elif (integer >= 100 and integer < 1000):
            integer_first = integer/100;
            list_first = dict[integer_first]
            
            integer_middle = (integer-(100*integer_first))/10;
            list_middle = dict[integer_middle]
            
            integer_last = integer % 10;
            list_last = dict[integer_last]
            
            (list_first[0] += list_middle[0]) += list_last[0]
            (list_first[1] += list_middle[1]) += list_last[1]
            (list_first[2] += list_middle[2]) += list_last[2]
            
            return list_first
        
if __name__ == '__main__':
    unittest.main()


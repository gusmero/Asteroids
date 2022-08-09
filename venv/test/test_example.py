import unittest



from space_rocks.utils import get_random_velocity, get_random_position
from pygame.math import Vector2 , Vector3


class MyTest(unittest.TestCase):
    
  
    def test_case_1(self):
        print("\n\nRunning Test 1....\n\n")
 
        self.assertTrue(1)
        print("\n\nFinished Test 1\n\n")



    # def test_case_2(self):
    #     print("\n\nRunning Test 2  get_random_velocity....\n\n")
    #     self.assertIsNotNone(get_random_velocity(1,3))
    #     self.assertIsInstance(get_random_velocity(1,3), Vector2)
    #     self.assertIsNot(get_random_velocity(1,3), Vector3)
    #     print("\n\nFinished Test 1\n\n")


    
    
if __name__ == '__main__':
    unittest.main()
    
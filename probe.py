# -*- coding: utf-8 -*-
"""
Maze runner

given a map, represented by a square array of strings, 
how to explore it from position (0, 0) down to the bottom right corner?

If a given cell owns a '0', this is an available position. If the 
cell owns a '*' this is an obstacle.
"""
import csv

with open('map.csv') as f:
    reader = csv.reader(f)
    MAP = [row for row in reader]

class Rover:
    '''
    Rover class. It implements left, right, up, down methods to iterate
    along the Map. Each one of those returns True of False wether the 
    position was updated successfully.
    
    On construction, the rover is positioned at (0, 0) in the map.
    '''
    def __init__(self, Map):
        self.Map = [row[:] for row in Map]
        self.i = 0
        self.j = 0
        self.rows = len(Map)
        self.cols = len(Map[0])
                
    def right(self):
        if self.j < self.cols - 1 and self._is_clean(self.i, self.j + 1):
            old_pos = self.pos()
            self.j += 1
            self._update_map(old_pos, self.pos())
            return True
        else:
            return False
            
    def left(self):
        if self.j > 0 and self._is_clean(self.i, self.j - 1):
            old_pos = self.pos()
            self.j -= 1
            self._update_map(old_pos, self.pos())
            return True
        else:
            return False
            
    def up(self):
        if self.i > 0 and self._is_clean(self.i - 1, self.j):
            old_pos = self.pos()
            self.i -= 1
            self._update_map(old_pos, self.pos())            
            return True
        else:
            return False
        
    def down(self):
        if self.i < self.rows - 1 and self._is_clean(self.i + 1, self.j):
            old_pos = self.pos()
            self.i += 1
            self._update_map(old_pos, self.pos())
            return True
        else:
            return False
        
    def pos(self):
        '''
        Returns the rover position.
        '''
        return (self.i, self.j)
        
    def goal(self):
        '''
        This is the goals' position (Bottom right corner of the Map)
        '''
        return (self.rows - 1, self.cols - 1)
        
    def _is_clean(self, i, j):
        '''
        Wether we can jump onto (i, j)
        '''
        assert 0 <= i <= self.rows and 0 <= j <= self.cols
        return self.Map[i][j] != '*'

    def _mark_map(self, i, j, chr):
        '''
        Mark Map[i][j] with the given character
        '''
        self.Map[i][j] = chr
        
    def _update_map(self, old_pos, new_pos):
        '''
        Update map. old_pos in map goes as a '0' and new_pos 
        goes as an 'M' representing the rover.
        '''
        i0, j0 = old_pos
        i1, j1 = new_pos
        self._mark_map(i0, j0, '0')
        self._mark_map(i1, j1, 'M')
        
    def map(self):
        '''
        String representation of the map. In ipython it is more 
        convenient timply print self.Map for a given Rover instance
        '''
        return '\n'.join([' '.join(row) for row in self.Map])


def explore(map):
    '''
    Write an algorithm to reach the goal here.
    '''
    rover = Rover(map)
    try:
        while rover.pos() != rover.goal():
            if rover.right() or rover.down():
                print rover.pos()
            elif rover.left() or rover.down():
                print rover.pos()
            else:
                print 'We are dead Jim >_<'
    except KeyboardInterrupt:
        print rover.map()
        
        
if __name__ == '__main__':
    explore(MAP)



    
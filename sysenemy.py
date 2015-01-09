#sysenemy.py
#
#sysenemy contains information about the enemy characters

class EnemyFighter(object):

    def __init__(self, level, hp, strength):
        self.level = level
        self.strength = strength
        self.maxhp = hp

    def attackmoves(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        attacks = [self.a, self.b, self.c, self.d]

    

# http://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
import math

class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return ("(" + str(self.vector)[1:-1] + ")").replace(' ', '')

    def add(self, other):
        if len(self.vector) != len(other.vector): raise Exception("The vector are not of the same length")
        return Vector([self.vector[i] + other.vector[i] for i in xrange(len(self.vector))])

    def subtract(self, other):
        if len(self.vector) != len(other.vector): raise Exception("The vectors are not of the same length")
        return Vector([self.vector[i] - other.vector[i] for i in xrange(len(self.vector))])

    def dot(self, other):
        if len(self.vector) != len(other.vector): raise Exception("The vectors are not of the same length")
        return sum([self.vector[i] * other.vector[i] for i in xrange(len(self.vector))])

    def norm(self):
        return math.sqrt(sum([self.vector[i] ** 2 for i in xrange(len(self.vector))]))

    def equals(self, other):
        if len(self.vector) != len(other.vector): return False
        return sum([self.vector[i] == other.vector[i] for i in xrange(len(self.vector))]) == len(self.vector)
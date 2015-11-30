__author__ = 'guangshun'
import psutil
from twisted.enterprise import adbapi

class A():

    @classmethod
    def cm(cls):
        print cls.__name__
    @staticmethod
    def sm():
        print '----'

    def s(self):
class B(A):
    pass

if __name__=='__main__':
    A.cm()
    B.cm()
    A.sm()
    B.sm()


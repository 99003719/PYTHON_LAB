
from assign_2.PY import *
from assign_3.PY import *
import pytest

def t1_fun():
    assert close_to_mean([1,2,3,4,5,6]) == 3
    assert close_to_mean([1,0,2,9,11,7]) == 2

def t2_fun():
    assert element_small_than_mean([1,2,3,4,5]) == [1,2,3]
    assert element_small_than_mean([1,2,0,1,9]) == [1,2,0,1]   

def t3_fu():
    assert bus(30,((1,2,3),(2,2,4))) == 27
    assert bus(40.((1.5,6),(2,3,4))) == 38

def t4_fun():
    assert a_s([1, 2, 3, 4, 5,6,7], 5) == 10.0
    assert a_s([0.1, 0.9, 2.1, 3.2, 0.9, 1.1], 4) == 2.75


def t5_fun():
    assert diff([1,2,3,4,5,6,7]) == 1
    assert diff([2,4,7,8]) == 6

def t6_fun():
    assert odd([3,3,4,3,3]) == 3
    assert odd([1,7,7,7,7]) == 7


def t7_fun():
    assert number([1,2,3,5]) == 2
    assert number([1,2,3,4,1,1,2,-1]) == 4


def t8_fun():
    assert iso("aish") == True
    assert iso("sagar") == False
    

def t9_fun():
    assert shuff(135) == 531
    assert shuff(4175) == 7541

def t10_fun():
    assert ip("192.168.1.251") == 3232236027
    assert ip("117.211.19.12") == 1976767244
    assert ip("192.256.1.1") == None
    assert ip(1976767244) == "117.211.19.12"
    
def t11_fun():
    assert m_t("10:09:35") == "10:9:35"
    assert m_t("09:88:90") == "10:29:30"

def t12_fun():
    assert m_d("33/11/2011") == "3/12/2011"
    assert m_d("29/2/2012") == "29/2/2012"
    assert m_d("11/15/2018") == "11/3/2019"

def t13_fun():
    assert mex("hai") == ['Hai','hAi','haI']
    assert mex("jack") == ['Jack','jAck','jaCk','jacK']

def t14_fun():
    assert acc_string("abcd") == "A-Bb-Ccc-Dddd"
    assert acc_string("aish") == "A-Ii-Sss-Hhhh"
    
def t15_fun():
    assert rth((112,211,299)) == None
    assert rth((255,0,255)) == "0XFF00FF"
    assert rth((90,11,199)) == "0XA5B7C"    
    
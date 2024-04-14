import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_declare_1(self):
    #     input = """func f() begin
    #     hello[1]
    #     end
    #           """
    #     expect = """Program([VarDecl(Id(hello), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(3.0)))), VarDecl(Id(world), None, dynamic, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(list), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(5.0), NumLit(4.0), NumLit(3.0), NumLit(2.0), NumLit(1.0)))])"""
    #     self.assertTrue(TestAST.test(input,expect,301))
        
    def testdeclare7(self):
        input = """
            func main()
            func main()
            begin
                number a 
                a[1,2,3] <- (10 + 20)*30
            end
        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), BinaryOp(*, BinaryOp(+, NumLit(10.0), NumLit(20.0)), NumLit(30.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test3(self):
        input = """
func f(number arr[10], number x)

func f(number a[5], number n)
    return   
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, CallExpr(Id(test), [ArrayLit(StringLit(abc), StringLit(def)), NumLit(1.0)]))"
        self.assertTrue(TestAST.test(input, expect, 302))

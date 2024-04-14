import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """var a <- 50
                bool b[4] <- [true,false,true,false]
                func main()
                begin 
                    number e <- (a + a) * 100 + - 2.5e-3
                    string f 
                    bool d <- b[6] and b[3]
                end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """
        func test(number a, number b)
            return a*b
        func main()
        begin
            number a <- test(10,20) + test(20,40)
            number b <- test(a,a) * test(a,20)
        end        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self):
        input = """
        func test(string a[2], number b)
            return a[b]...a[b-1]
        func main()
        begin
            var a <- test(["abc","def"],1)
        end        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """
        func test(string a[2], number b)

        func test1()
            var a <- test(["abc","def"],1)

        func test(string a[2], number b)
            return a[b]...a[b-1]

        func main()
        begin
            test1()
        end        
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, CallExpr(Id(test), [ArrayLit(StringLit(abc), StringLit(def)), NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
        bool a[2,2,3] <- [[[true,false,true],[true,false,true]],[[true,false,true],[true,false,true]]]      
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
        var a <- 100
        func sqr(number a)
            return a*a
        func main()
        begin
            var b <- true
            for a until a < 100 by a + 1
            begin
                a <- sqr(a)
                begin
                    break
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
        func main()
        begin
            number x <- 10
            if (x > 0)
            begin
                x <- x + 1
            end
            elif (x < 0)
            begin
                number i <- 0
                for i until i > 5 by i + 1 
                begin
                    x <- x * 2
                    continue
                end 
            end
            elif (x = 10)
                x <- 2
            else x <- 100
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
            input = """
            number a[2,3] <- [[5,6,7,6],[5,6,7,6]]
            func a(number b)
            begin
                return 10
            end
            
            func main()
            begin
                number b <- a(10)
                b <- a[2,3] + b 
            end
            
            """
            expect = "successful"
            self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
            input = """
            func main()
            begin
                dynamic b 
                number a
                b <- a
                b <- b + 1 
            end
            
            """
            expect = "successful"
            self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
            input = """
            func main()
            begin
                dynamic b 
                dynamic c
                b <- b + c
            end
            
            """
            expect = "successful"
            self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
        func main()
        begin
            dynamic b 
            dynamic c
            dynamic d
            var e <- 2
            b <- b + c
            d <- "track"..."gps"
            e <- not ((true and false) or e)
        end
        
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, BinaryOp(and, BooleanLit(True), BooleanLit(False)), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """
        func test(number a)

        func callTest() begin
            number a <- test(100)
            return a
        end

        func test(number a)
            return true
        func main()
        begin
            callTest()
        end
        
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 411))  

    def test12(self):
        input = """
        func main()
        begin
            dynamic i
            dynamic cond 
            dynamic x 
            for i until cond by x
            begin
                x <- i * 2 + 1
                i <- cond 
            end
        end
        
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i), Id(cond))"
        self.assertTrue(TestChecker.test(input, expect, 412))  

    def test13(self):
        input = """
        func main()
        begin
            number a[1,2,3] <- [[[1,2,3]]]
        end
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 413))  

    def test14(self):
        input = """
        func main()
        begin
            var a <- readNumber()
            writeNumber(a)
            dynamic b <- readBool()
            write(b)
            string c <- readString()
            writeString(c) 
        end
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 414))  

    def test15(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        func b(number a)
            return a
        func main()
        begin
            a <- c
        end
        
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 415))  

    def test16(self):
        input = """
        number a[1,2] <- [[1,2],[1,2]]
        func main()
        begin
            writeNumber(a[1,2])
            write((a[0,0] * a[1,1] > 100) and (a[0,1] * a[1,0] < 100))
        end
        
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 416))  

    def test17(self):
        input = """func a (number b, number c, number d)
                func a (number b, number c, number d)
                begin 
                end
                func a (number b, number c, number d)
        """
        expect = "Redeclared Function: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """func test()
        begin
            string a[1,2] <- [["hello", "world"]]
            begin
                return a[1,2]
            end
        end
        func main()
        begin
            number s <- test()
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(s), NumberType, None, CallExpr(Id(test), []))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """func test()
        begin
            number a <- 10
            number b <- 20
            if (a + b > 10)
                return a
            elif (a + b = 10)
                return a + b
            else return true
        end
        func main()
        begin
            bool s <- test() and test()
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, CallExpr(Id(test), []), CallExpr(Id(test), []))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """func test()
        begin
            return [[1,2,3],[1,2,3]]
        end
        func main()
        begin
            writeNumber(test()[0,0])
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 420))  

    def test21(self):
        input = """func test()
        begin
            return [[1,2,3],[1,2,3]]
        end
        func main()
        begin
            writeNumber(test()[0,0,0])
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(test), []), [NumLit(0.0), NumLit(0.0), NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 421)) 

    def test22(self):
        input = """func test()
        begin
            return [[1,2,3],[1,2,3]]
        end
        func main()
        begin
            writeNumber(test()["1","2"])
        end
        """
        expect = "Type Mismatch In Expression: StringLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 422)) 

    def test23(self):
        input = """func test()
        begin
            return [[1,2,3],[1,2,3]]
        end
        func main()
        begin
            writeNumber(test()[1,1] + test()[1])
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(test), []), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            a <- b
        end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """func test()
        begin
            dynamic a
            return a
        end 
        func main()
        begin
            test()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
        func test()

        func test1()
        begin
            number a <- test()
            return a
        end

        func test()
        begin
            dynamic a
            return a...a
        end 
        func main()
        begin
            string s <- test()
        end
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(..., Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test28(self):
        input = """
        dynamic a
        func test()

        func test1()
        begin
            string b <- test()
            return b
        end

        func test()
        begin
            return a
        end 
        func main()
        begin
            number temp <- a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(temp), NumberType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """
        dynamic a
        func test()
        
        func test2()

        func test1()
        begin
            string b <- test() + test2()
            return b
        end

        func test()
        begin
            return a
        end 
        func main()
        begin
            number temp <- test2() + a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, BinaryOp(+, CallExpr(Id(test), []), CallExpr(Id(test2), [])))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
        func main()
        begin
            return a
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        input = """
        func main()
        begin
            var a <- 10
            return a
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
        func a()
        begin
            return 10
        end
        
        func main()
        begin
            var b <- a
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
        func a()
        begin
            return [true,false,true]
        end

        func b()
        begin
            return [false,true,false]
        end
        
        func main()
        begin
            var a <- a()
            var b <- b()
            dynamic c
            c <- not (a[0] and b[0])
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), None, var, CallExpr(Id(a), []))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
        func a()
        begin
            return [true,false,true]
        end

        func b()
        begin
            return [false,true,false]
        end
        
        func main()
        begin
            bool a[3] <- a()
            bool b[3] <- b()
            dynamic c
            c <- not (a[0] and b[0])
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        input = """
        func a()
        begin
            return [true,false,true]
        end

        func b()
        begin
            return [[false,true,false,true]]
        end
        
        func main()
        begin
            bool a[3] <- a()
            bool b[1,4] <- b()
            b <- a
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
        number a <- 10
        bool b <- true
        string c[4] <- ["this","is","a","string"]
        
        func main()
        begin
            dynamic d
            d <- a > 5
            b <- d and (c[0] == c[1]) 
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        input = """
        func main()
        begin
            dynamic d
            dynamic e
            if (d > 10)
                e <- true
            elif (d == 10)
                e <- false 
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(d), NumLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
        func main()
        begin
            dynamic d
            dynamic e
            if (d > 10)
                e <- -10
            elif (d = 10)
                e <- -10 * d + 100 / 20
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
        func test(number a, number b)
            return a + b + c
        number c
        func main()
        begin
            test(c,c)
        end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
        func test(number a, number b)
            return a + b + c
        number c
        func main()
        begin
            test(c,c)
        end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
        func main()
        begin
            number b[4] <- [1,2,true,"false"]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True), StringLit(false))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
        func main()
        begin
            number a <- -b[0] * 10
        end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """
        func main()
        begin
            number a <- -b()[0] * 10
        end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
        func main()
        begin
            dynamic b
            dynamic c
            bool a[4] <- [true and false, b or false, not c, not b and not c]
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
        func voidfunc()
        func test() begin
            number a <- voidfunc()
            return a
        end 
        func voidfunc()
            return
        func main()
        begin
            number a <- test()
        end
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            if (a + b)
                a <- b
        end
        """
        expect = "Type Mismatch In Statement: If((BinaryOp(+, Id(a), Id(b)), AssignStmt(Id(a), Id(b))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
        number a
        func main()
        begin
            string a 
            dynamic b
            if ((a...b) == "hello world")
                a <- true
            
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
        number a
        func test(number a, string b)
            return [a,a,a,a]
        func main()
        begin
            number a[4] <- test(a)
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
        number a <- 10
        func test(number a, string b)
            return [[b,b,b],[a,a,a]]
        func main()
        begin
            number a[2,3] <- test(a, "string")
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(b), Id(b), Id(b)), ArrayLit(Id(a), Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
        number a <- 10
        func test(number a, string b)
            return 1
        func main()
        begin
            number a <- test(a, a)
        end
        """
        expect = "Type Mismatch In Expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
        string a <- "abc"
        func test(string a, string b)
        begin
            dynamic c
            return c...a
        end
        func main()
        begin
            string b     <- test(a, a)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
        number a <- foo(123) 
        func main() begin
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
        func main() begin
            number a[2, 3] <- [[1,2,3],[4,5,6]]
            for i until i >= 2 by 1 begin
                for j until j >= 3 by 1 begin
                    a[i, j] <- i + j
                end
            end
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
        func main() begin
            number a[2, 3] <- [[1,2,3],[4,5,6]]
            dynamic i
            dynamic j
            for i until i >= 2 by 1 begin
                for j until j >= 3 by 1 begin
                    a[i, j] <- i + j
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
        func main() begin
            var x <- 1
            for x until x >= 10 by 0 begin
                x <- x * 2
            end
            dynamic arr <- x
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """
        number arr[1,2] <- [[1,2]]
        func overwrite(number arr[1,2])
        begin 
            arr[0,0] <- 10
            arr[0,1] <- 5
            return arr
        end
        func main() begin
            arr <- overwrite(arr)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
        func main(number a, number b) begin
            if (a+b != 10) begin
                return a+b
            end
            else begin
                return a-b
            end
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
        number arr[1,2] <- [[1,2]]
        func overwrite(number arr[1,2])
        begin 
            arr[0,0] <- 10
            arr[0,1] <- 5
            return arr
        end
        func main() begin
            arr <- overwrite(arr)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """
        number arr[1,2] <- [[1,2]]
        func overwrite(number arr[1,2])
        begin 
            arr <- [[2,3]]
            return arr
        end
        func main() begin
            arr <- overwrite(arr)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """
        number arr[1,2] <- [[1,2]]
        func overwrite(number arr[1,2])
        begin 
            number b[1,2] <- [[2,3]]
            arr <- b
            return arr
        end
        func main() begin
            arr <- overwrite(arr)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """
        number arr[1,2] <- [[1,2]]
        func overwrite(number arr[1,2])
        begin 
            number b[1,2] <- [[2,3]]
            arr <- b
            return arr
        end
        func main() begin
            number temp_ans <- overwrite(arr)[0,1]
            dynamic c <- temp_ans * 2
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        input = """
        func main()
        begin
            number a <- not 5
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        input = """
        dynamic i
        func main()
        begin
            dynamic i
            i <- 10
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 463))  

    def test64(self):
        input = """
        dynamic i
        func main()
        begin
            dynamic i
            i <- foo()
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 464))  

    def test65(self):
        input = """
        dynamic i
        func foo(number a, number b)
            return a * b 
        func main()
        begin
            dynamic i
            i <- foo(10)
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(10.0)])"
        self.assertTrue(TestChecker.test(input, expect, 465)) 

    def test66(self):
        input = """
        dynamic i
        func foo(string a)
            return a...a
        func main()
        begin
            dynamic i
            i <- foo(10)
        end
        """
        expect = "Type Mismatch In Expression: NumLit(10.0)"
        self.assertTrue(TestChecker.test(input, expect, 466)) 

    def test67(self):
        input = """
        dynamic i
        func foo(string a)
        begin 
        end

        func main()
        begin
            dynamic i
            i <- foo(10)
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(10.0)])"
        self.assertTrue(TestChecker.test(input, expect, 467)) 

    def test68(self):
        input = """
        string a[2] <- ["string", "string1"]

        func main()
        begin
            dynamic i
            i <- a[1]...a[0]
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 468)) 

    def test69(self):
        input = """
        string a[2,2] <- [["string", "string1"],["hello","world"]]

        func main()
        begin
            dynamic i
            string arr <- "hello world"
            i <- arr[0,0]...arr[0,1]
        end
        """
        expect = "Type Mismatch In Expression: Id(arr)"
        self.assertTrue(TestChecker.test(input, expect, 469)) 

    def test70(self):
        input = """
        string a[2,2] <- [["string", "string1"],["hello","world"]]

        func foo()
            return 5 + 6
        func main()
        begin
            dynamic i
            i <- a[0+10,5-5]...a[foo() - 11, 3 < 4]
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(<, NumLit(3.0), NumLit(4.0))"
        self.assertTrue(TestChecker.test(input, expect, 470)) 

    def test71(self):
        input = """
        string a[2,2] <- [["string", "string1"],["hello","world"]]

        func foo()
            return 5 + 6
        func main()
        begin
            dynamic i
            i <- a[0+10,5-5,(foo()-5)/6]...a[foo() - 11, 3 < 4]
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(10.0)), BinaryOp(-, NumLit(5.0), NumLit(5.0)), BinaryOp(/, BinaryOp(-, CallExpr(Id(foo), []), NumLit(5.0)), NumLit(6.0))])"
        self.assertTrue(TestChecker.test(input, expect, 471)) 

    def test72(self):
        input = """
        string a[2,2] <- [["string", "string1"],["hello","world"]]

        func foo()
            return 5 + 6
        func main()
        begin
            dynamic i
            i <- a[0+10,5-5,(foo()-5)/6]...a[foo() - 11, 3 < 4]
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(10.0)), BinaryOp(-, NumLit(5.0), NumLit(5.0)), BinaryOp(/, BinaryOp(-, CallExpr(Id(foo), []), NumLit(5.0)), NumLit(6.0))])"
        self.assertTrue(TestChecker.test(input, expect, 472)) 

    def test73(self):
        input = """
        func foo()
            return 5 + 6
        func foo_str()
            return "5"..."6"
        func main()
        begin
            dynamic i
            i <- foo() 
            var j <- foo_str()
            i <- j
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i), Id(j))"
        self.assertTrue(TestChecker.test(input, expect, 473)) 

    def test74(self):
        input = """
        func foo()
            return 5 + 6
        func foo_str()
        begin
            dynamic str
            return str
        end
        func main()
        begin
            dynamic i
            i <- foo() 
            var j <- foo_str()
            i <- j
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(str))"
        self.assertTrue(TestChecker.test(input, expect, 474)) 

    def test75(self):
        input = """
        func main()
        begin
            dynamic i
            dynamic j
            i <- j
        end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(i), Id(j))"
        self.assertTrue(TestChecker.test(input, expect, 475)) 

    def test76(self):
        input = """
        func foo(number a) begin
            begin 
                if (a + a * 2) 
                    return true
                else 
                    return false
            end
        end

        func main()
        begin
            bool a <- foo(100)
        end
        """
        expect = "Type Mismatch In Statement: If((BinaryOp(+, Id(a), BinaryOp(*, Id(a), NumLit(2.0))), Return(BooleanLit(True))), [], Return(BooleanLit(False)))"
        self.assertTrue(TestChecker.test(input, expect, 476)) 

    def test77(self):
        input = """
        func foo(number a) begin
            begin 
                if (a + a * 2 > 0) 
                    return true
                elif (a + a - 2) 
                    return false
            end
        end

        func main()
        begin
            bool a <- foo(100)
        end
        """
        expect = "Type Mismatch In Statement: If((BinaryOp(>, BinaryOp(+, Id(a), BinaryOp(*, Id(a), NumLit(2.0))), NumLit(0.0)), Return(BooleanLit(True))), [(BinaryOp(-, BinaryOp(+, Id(a), Id(a)), NumLit(2.0)), Return(BooleanLit(False)))], None)"
        self.assertTrue(TestChecker.test(input, expect, 477)) 

    def test78(self):
        input = """
        func main()
        begin
            dynamic i
            dynamic x
            for i until i > 100 by i + 1
                x <- x * 2
            break
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 478)) 

    def test79(self):
        input = """
        func main()
        begin
            dynamic i
            dynamic x
            for i until i > 100 by i + 1
                x <- x * 2
            begin
                begin
                    continue
                end
            end
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 479)) 

    def test80(self):
        input = """
        func foo()
            return [1,2,3]

        func check(number arr[3])
        begin
            if ((arr[0] > 10) and (arr[1] < 10))return true
            else return false
        end

        func foo2(number arr[3])
            return arr[0] + arr[1] + arr[2]

        func main()
        begin
            dynamic i
            dynamic x
            number arr[3] <- foo()
            for i until check(arr) by foo2(arr)
                x <- x * 2
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 480)) 

    def test81(self):
        input = """
        func foo()
            return

        func foo2()
            return foo()

        func main()
        begin
            foo2()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        func foo()
            return 10

        func foo2()
            return foo()

        func main()
        begin
            foo2()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2), [])"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83(self):
        input = """
        func main()
        begin
            dynamic b
            number a[1] <- [b]
            
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84(self):
        input = """
        func main() 

        func main() begin
            return true and not (false and "true")
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, BooleanLit(False), StringLit(true))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        input = """
        func fibo(number n) 
        begin
            if (n <= 2) return 1
            number f1 <- 0
            number f2 <- 1
            number f3 <- f1 + f2
            number i <- 2
            for i until i > n by 1 begin
                f3 <- f1 + f2
                f1 <- f2
                f2 <- f3
            end
            return f3
        end
        func main() begin 
            writeNumber(fibo(50))
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test86(self):
        input = """
        func foo(number a)
        begin
            return
        end
        func foo(number a, number b)
        begin
            return
        end
        func main() begin 
            foo()
        end
        """
        expect = "Redeclared Function: Id(foo)"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = """
        func main() begin 
            number i
            for i until true by 1
            begin
                if (i > 10) break
                else continue
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        input = """
        func sqr(number a)
            return a*a

        func sum(number arr[5])
        begin
            dynamic total <- 0
            dynamic i 
            for i until i = 5 by 1
            begin
                total <- total + sqr(arr[i])
            end
            return total
        end

        func main() begin 
            write(sum([1,2,3,4,5]) > 1000)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test89(self):
        input = """
        func gcd(number a, number b)
        begin
            for b until b = 0 by 0
                a <- b
                b <- a % b
            return a
        end

        func main() begin 
            number a <- readNumber()
            number b <- readNumber()
            writeNumber(gcd(a,b))
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90(self):
        input = """        
        func main() begin 
            string strArr[5] <- ["this","is","a","string","hihi"]
            dynamic i
            string ans
            for i until i = 5 by 1
            begin
                ans <- ans + strArr[i]
            end
            writeString(ans)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(ans), ArrayCell(Id(strArr), [Id(i)]))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91(self):
        input = """
        func foo(number a, bool b) begin
            return [[[1,2],[1,2],[1,2]]]
        end        

        func funcfunc(number a, number b, number c)
        begin
            if (a + b = c)
                writeNumber(c)
            else writeNumber(a + b) 
        end

        func main() 
        begin
            number x <- 10
            number i <- 0
            for i until i > x by x-2
                if (i >= 1) break
                elif (x <= 1) continue
                elif (b[10,2+3] < foo(1,true)[1,2-2,3*4]) 
                    funcfunc(1,2,3)
                else i <- i*10
        end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        input = """
        func main(number a, number b) begin
            number x <- 100
            if (a+b != x) begin
                return a+b
            end
            else begin
                return a-b
            end
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93(self):
        input = """
        func main() begin
            number a[2, 3] <- [[1,2,3],[4,5,6]]
            for i until i >= 2 by 1 begin
                for j until j >= 3 by 1 begin
                    a[i, j] <- i + j
                end
            end
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94(self):
        input = """
        number a
        func main() begin
            number b <- a
            number arr[2] <- [a,b]
            writeNumber(arr[0])
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
        input = """
        func foo(number a, number b)
        begin
            if (a < b) writeNumber(b-a)
            else writeNumber(a+b)
        end

        func main() begin
            number num1 <- readNumber()
            number num2 <- readNumber()
            foo(num1, num2)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96(self):
        input = """
        func foo(bool a, bool b, bool c)
        begin
            if (a) write(a)
            elif (b) write(b)
            elif (c) write(c)
            else write((a and b) and not c)
        end

        func main() begin
            bool a <- readBool()
            bool b <- readBool()
            bool c <- readBool()
            foo(a,b,c)
        end
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97(self):
        input = """
        func foo(number a, number b, string c)
        begin
            ans <- ""
            for a until a = b by 1
            begin
                ans <- ans + c
            end
            return ans
        end

        func main() begin
            number a <- readNumber()
            number b <- readNumber()
            string c <- readString()
            writeString(foo(a,b,c))
        end
        """
        expect = "Undeclared Identifier: ans"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98(self):
        input = """
        func len(string a)
            return 10

        func merge(string arr[10])
        begin
            string ans <- ""
            dynamic i <- 0
            for i until i = 10 by 1
            begin
                ans <- ans...arr[i]
                if (len(ans) > 100)
                    break
            end
            return ans
        end

        func main() begin
            string arr[10]
            dynamic i <- 0
            for i until i = 10 by 1
                arr[i] <- readString()
            merge(arr)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(merge), [Id(arr)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99(self):
        input = """
        func main() begin
            return 10
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))

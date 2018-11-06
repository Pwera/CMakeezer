#include <fakeit.hpp>

#include <gtest/gtest.h>
//#include <gmock/gmock.h>
class Turtle {
public:
    virtual ~Turtle() {}
    virtual void PenUp() = 0;
    virtual void PenDown() = 0;
    virtual void Forward(int distance) = 0;
    virtual void Turn(int degrees) = 0;
    virtual void GoTo(int x, int y) = 0;
    virtual int GetX() const = 0;
    virtual int GetY() const = 0;
};
//class MockTurtle : public Turtle {
//public:
//    MOCK_METHOD0(PenUp, void());
//    MOCK_METHOD0(PenDown, void());
//    MOCK_METHOD1(Forward, void(int distance));
//    MOCK_METHOD1(Turn, void(int degrees));
//    MOCK_METHOD2(GoTo, void(int x, int y));
//    MOCK_CONST_METHOD0(GetX, int());
//    MOCK_CONST_METHOD0(GetY, int());
//};
//using namespace std;
//
//class Object{
//public:
//    Object() {}
//
//};
////class myTestFixture1 : public ::testing::Test {
////public:
////    myTestFixture1() {
////    }
////
////    void SetUp() {
////    }
////
////    void TearDown() {
////    }
////
////    ~myTestFixture1() {
////    }
////
////};
//
//
//// Tests negative input.
//TEST(IsPrimeTest, Negative) {
//    // This test belongs to the IsPrimeTest test case.
//
//    EXPECT_FALSE(IsPrime(-1));
//    EXPECT_FALSE(IsPrime(-2));
//    EXPECT_FALSE(IsPrime(INT_MIN));
//}
//
//// Tests some trivial cases.
//TEST(IsPrimeTest, Trivial) {
//    EXPECT_FALSE(IsPrime(0));
//    EXPECT_FALSE(IsPrime(1));
//    EXPECT_TRUE(IsPrime(2));
//    EXPECT_TRUE(IsPrime(3));
//}
//
//// Tests positive input.
TEST(sdv, Positive) {
    EXPECT_FALSE(false);
    fakeit::Mock<Turtle> mock;
    const Turtle &turtle = mock.get();
    turtle.GetX();
//    EXPECT_TRUE(IsPrime(5));
//    EXPECT_FALSE(IsPrime(6));
//    EXPECT_TRUE(IsPrime(23));
}


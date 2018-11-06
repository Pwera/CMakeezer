#include <HippoMocks/hippomock.h>

class CFoo {
public:
    bool Func1() {
        bool ret = false;
        if (Func2()) {
            //do something
            ret = true;
        }
        else {
            //do something else
        }
        return ret;
    }

    bool Func2() {
        return true;
    }

};

TEST_CASE("Hippomocks example", "[sanity]") {
    MockRepository mocks;
    CFoo* pFoo = mocks.Mock<CFoo>();
    mocks.ExpectCall(pFoo, CFoo::Func2).Return(true);
    REQUIRE(pFoo->Func1() == true);
    mocks.ExpectCall(pFoo, CFoo::Func2).Return(false);
    REQUIRE(pFoo->Func1() == false);
}

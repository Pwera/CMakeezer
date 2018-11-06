#include <lambda.hpp>
using namespace lambda;
using namespace lambda::streams;
int main(){
    let multipleOf = curry(flip([](auto x, auto y) { return x % y == 0; }));
    let even = multipleOf(2);
    // Find the sum of all the multiples of 3 or 5 below 1000.
    ints(0, 1000) | filter(multipleOf(3) || multipleOf(5)) | sum;
}
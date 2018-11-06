#include <function2/function2.hpp>
#include <thread>
#include <chrono>
#include <iostream>
#include <continuable/continuable.hpp>
#include <clue/concurrent_queue.hpp>
#include <rapidjson/document.h>
#include <zmq.h>
using namespace std;
using namespace std::chrono;
using namespace clue;

struct functional_executor {
    auto post() const {
        return [](auto &&) {};
    }
};

struct stateful_callable {
    std::string test;

    void operator()() {
    }
};

class Manager {
    clue::concurrent_queue<std::string> &que;
public:
    Manager(concurrent_queue<string> &que_) : que(que_) {}
    void save() {
        que.push("??");
        que.push("!");
    }
};

int main() {
    fu2::function<void() const> fun = [] {
        using namespace std::chrono_literals;
        std::cout << "Hello waiter" << std::endl; // flush is intentional
        std::this_thread::sleep_for(2s);
    };
    fun();
    std::string test = "hey";
    fu2::function<void()> fn = stateful_callable{std::move(test)};

    auto fn2 = std::move(fn);
    fn();
    (void) fn2;
    functional_executor e;
    auto executor = &e;
    clue::concurrent_queue<std::string> que;
    std::cout << ":D\n";
     Manager manager(que);
    manager.save();

    rapidjson::Document document;
    document.Parse("");

};
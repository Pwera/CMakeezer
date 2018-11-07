cmake_minimum_required (VERSION 3.10)
project (Projecto)
include(FeatureSummary)
set(CMAKE_CXX_STANDARD 14)

find_package(Threads)                       #Threads::Threads
find_package(benchmark)                     #benchmark::benchmark
find_package(SFML 2.4.2 COMPONENTS audio graphics window system)

find_package(function2)
find_package(FakeIt)                        #FakeIt::FakeIt
find_package(Immer)                         #immer
#find_package(OpenCv 3.3.0)
find_package(Hana)                          #hana
find_package(GTest 1.8.0)                   #GTest::GTest GTest::Main
find_package(GMock 1.8.0)                  #TODO: We have to add FindGMock.cmake
#find_package(cpr)                          #cpr::cpr
#find_package(log4cplus)                    #log4cplus::log4cplus
find_package(continuable)                   #continuable::continuable-base continuable::continuable
find_package(CLUE 1.0)                      #clue::clue
find_package(Catch2 2.2.2)                  #Catch2::Catch2
find_package(RapidJSON 1.1.0)
find_package(ZeroMQ 4.3.1)                  #libzmq libzmq-static
find_package(Backward)                      #Backward::Backward
find_package(curl 7.61.0)
find_package(tinydnn 1.0.0)                 #TinyDNN::tiny_dnn
find_package(brigand)
find_package(Alloy 1.0.0)
find_package(tacopie)                       #tacopie::tacopie
find_package(cpp_redis)                     #cpp_redis::cpp_redis
find_package(variant)                       #variant::variant
find_package(dynamix)                       #dynamix::dynamix
find_package(lambda)                        #lambda::lambda
find_package(HippoMocks)
find_package(Metal)
find_package(zlib)
find_package(libev)
find_package(mongoose)

if(MSVC) ## TODO: Finish me
    set(CMAKE_CXX_FLAGS_RELEASE "/MT /O2 /Ob2 /DNDEBUG")
    set(CMAKE_CXX_FLAGS_DEBUG "/MTd /Zi /Ob0 /Od /RTC1")
endif()

function(CreateOptionalTargetWithDependency SampleName  sources dependency)
    if (TARGET ${dependency})
        message(INFO "  Create target: ${SampleName} with dependency: ${dependency} from sources: ${sources}")
        add_executable(${SampleName} ${sources})
        target_link_libraries(${SampleName} PRIVATE ${dependency})
    endif()
endfunction()

CreateOptionalTargetWithDependency(Function2Sample src/function2.cpp function2::function2)      ##TODO: FInish Me
#[[
CreateOptionalTargetWithDependency(BenchmarkSample src/googlebenchmark_ut.cpp benchmark::benchmark)
CreateOptionalTargetWithDependency(ZmqSample src/zmq.cpp libzmq)                                ##TODO: FInish Me
if(NOT MSVC)
    CreateOptionalTargetWithDependency(ImmerSample src/immer.cpp immer) 
endif()
CreateOptionalTargetWithDependency(BrigandSample src/brigand.cpp brigand::brigand)
#CreateOptionalTargetWithDependency2(TinyDnnSample src/TinyDnn.cpp TinyDNN::tiny_dnn Threads::Threads)  ##TODO: FInish Me
CreateOptionalTargetWithDependency(ClueSample src/clue.cpp "CLUE::clue;Threads::Threads")
#CreateOptionalTargetWithDependency(BackwardSample src/backward.cpp Backward::Backward)
CreateOptionalTargetWithDependency(AlloySample src/Alloy.cpp Alloy)
CreateOptionalTargetWithDependency(TacopieSample src/Tacopie.cpp tacopie::tacopie)
CreateOptionalTargetWithDependency(RedisCppSample src/RedisCpp.cpp cpp_redis::cpp_redis)
CreateOptionalTargetWithDependency(VariantSample src/Variant.cpp variant::variant)
CreateOptionalTargetWithDependency(DynamixSample src/Dynamix.cpp dynamix::dynamix)
#CreateOptionalTargetWithDependency(LambdaSample src/Lambda.cpp lambda::lambda)
CreateOptionalTargetWithDependency(MetalSample src/Metal.cpp Metal)
if(TARGET zlib::zlib) 
    CreateOptionalTargetWithDependency(ZlibSample src/Zlib.cpp zlib::zlib) #Provided by Cmakeezer
else()
    CreateOptionalTargetWithDependency(ZlibSample src/Zlib.cpp ZLIB::ZLIB) #Provided by Cmake
endif()
CreateOptionalTargetWithDependency(MongooseSample src/Mongoose.cpp mongoose::mongoose)
]]


enable_testing()

if (TARGET FakeIt::FakeIt AND TARGET GTest::GTest AND TARGET GTest::Main)
    add_executable(tester fakeit_gtest_ut.cc)
    add_test(tester tester)
    target_link_libraries(tester PRIVATE GTest::GTest GTest::Main FakeIt::FakeIt)
endif()

if (TARGET Catch2::Catch AND EnableCatchSample)
    add_executable(catch_ut catch_ut.cpp)
    add_test(catch_ut catch_ut)
    target_link_libraries(catch_ut PRIVATE Catch2::Catch)
endif()


feature_summary(WHAT ALL FATAL_ON_MISSING_REQUIRED_PACKAGES)

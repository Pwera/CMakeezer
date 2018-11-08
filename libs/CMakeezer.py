import subprocess
import os
import platform

currentPath =os.getcwd()
def is_tool(name):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True

print("cmake\texist [ " + str(is_tool("cmake")) + " ]")    
print("gcc\texist [ " + str(is_tool("gcc")) + " ]")    
print("ninja\texist [ " + str(is_tool("ninja")) + " ]")    
print("cl\texist [ " + str(is_tool("cl")) + " ]")
print("clang\texist [ " + str(is_tool("clang")) + " ]")

#if is_tool("ninja") : 
	#UserGenerator="Ninja"
	#UserGenerator="Visual Studio 15 2017 Win64"
	#UserGenerator="MinGW Makefiles"
#else:
if platform.system() == "Windows" :
	if is_tool("gcc") :
		#UserGenerator="Ninja"
		UserGenerator="MinGW Makefiles"
	else: 
		UserGenerator="Visual Studio 15 2017 Win64"
		#UserGenerator="Ninja"
else :
	UserGenerator="Unix Makefiles"

generator_s_opt = UserGenerator.replace(" ", "")
InstallationPrefix=currentPath+"/../../repo/"+generator_s_opt
InstallationPrefix=InstallationPrefix.replace("\\", "/")
inst_opt="-DCMAKE_INSTALL_PREFIX="+ InstallationPrefix
module_opt="-DCMAKE_MODULE_PATH="+ InstallationPrefix
prefix_opt="-DCMAKE_PREFIX_PATH="+ InstallationPrefix
generator_opt="-G"+UserGenerator

def my_function(lib, *dupa):
	hOption = "-H"+str(currentPath) + "/"+lib
	bOption = "-B"+str(currentPath) +"/../../generated/" +generator_s_opt+"/" + lib
	bOption2 = str(currentPath) +"/../../generated/"+generator_s_opt+"/" + lib
	
	subprocess.call(["cmake",  generator_opt, hOption, bOption, inst_opt, module_opt,prefix_opt, "-DBUILD_SHARED_LIBS=OFF"] +  list(dupa))
	if is_tool("gcc") :
		if is_tool("ninja") :
			subprocess.call(["cmake","--build", bOption2])
		else :
			subprocess.call(["cmake","--build", bOption2, "--", "-j8"])
	else :
		subprocess.call(["cmake","--build", bOption2])
	subprocess.call(["cmake","--build", bOption2, "--target" ,"install"])

	return

'''
#my_function("zlib")
my_function("curl", "-DBUILD_TESTING=OFF")

my_function("googletest", "-DBUILD_GTEST=ON", "-DBUILD_GMOCK=ON", "-Dgtest_build_tests=OFF",  "-Dgtest_build_samples=OFF")
my_function("Catch2" , "-DCATCH_ENABLE_WERROR=OFF", "-DBUILD_TESTING=FALSE", "-DNOT_SUBPROJECT=FALSE")
my_function("hof", "-DBUILD_EXAMPLES=OFF")
my_function("immer", "-DCHECK_BENCHMARKS=OFF", "-DENABLE_SANITIZER=OFF", "-DENABLE_COVERAGE=OFF")
my_function("cxxopts", "-DCXXOPTS_BUILD_EXAMPLES=OFF", "-DCXXOPTS_BUILD_TESTS=OFF")
my_function("variant-1", "-DWITH_TESTS=OFF")
my_function("atria", "-DENABLE_TEST=OFF")
my_function("GSL", "-DGSL_TEST=OFF")
my_function("asio")
my_function("FakeIt")
my_function("SDL", "-DSDL_TEST=OFF")
my_function("tacopie")
my_function("hana")
my_function("fmem", "-DBUILD_TESTING=OFF")
my_function("gherkin-c", "-DBUILD_EXAMPLES=OFF")
my_function("gherkin-cpp")
my_function("brigand")
my_function("clue", "-DBUILD_TESTS=OFF", "-DENABLE_COVERAGE=OFF", "-DBUILD_EXAMPLES=OFF")
my_function("asyncplusplus")
my_function("libzmq", "-DWITH_DOC=OFF", "-DBUILD_TESTS=OFF") #submodule
my_function("CppMicroServices", "-DUS_BUILD_TESTING=OFF", "-DUS_BUILD_EXAMPLES=OFF")
my_function("function2", "-DBUILD_TESTS=OFF")
my_function("continuable", "-DCTI_CONTINUABLE_WITH_EXAMPLES=OFF", "-DCTI_CONTINUABLE_WITH_TESTS=OFF") #deps
my_function("benchmark" , "-DBENCHMARK_ENABLE_TESTING=OFF")
my_function("json" , "-DJSON_BuildTests=OFF")
my_function("tiny-dnn") #Include
my_function("SFML" , "-DSFML_BUILD_DOC=OFF")
my_function("metal")
my_function("GUnit")
my_function("valuable", "-DBUILD_TESTS=OFF")
my_function("hippomocks")
my_function("trompeloeil")
my_function("alloy", "-DBUILD_TEST=OFF", "-DBUILD_SAMPLES=OFF")
my_function("libpcap")
my_function("te")
my_function("sqlite_orm", "-DSqliteOrm_BuildTests=OFF", "-DSqliteOrm_BuildExamples=OFF")
my_function("cat", "-DBUILD_TESTS=OFF", "-DBUILD_EXAMPLES=OFF")
my_function("rapidjson", "-DBUILD_TESTS=OFF", "-DBUILD_DOC=OFF", "-DRAPIDJSON_BUILD_THIRDPARTY_GTEST=OFF")
my_function("dynamix" , "-DDYNAMIX_BUILD_EXAMPLES=OFF", "-DDYNAMIX_BUILD_TUTORIALS=OFF", "-DDYNAMIX_BUILD_UNIT_TESTS=OFF")
my_function("cmcstl2")
my_function("lambda", "-DBUILD_TEST=OFF")
my_function("libtins", "-DLIBTINS_BUILD_TESTS=ON", "-DLIBTINS_BUILD_EXAMPLES=ON")
my_function("variant")
#my_function("Synca")
my_function("range-v3", "-DRANGE_V3_TESTS=OFF" ,"-DRANGE_V3_EXAMPLES=OFF")
my_function("libraries")
my_function("lager", "-DBUILD_EXAMPLES=OFF", "-DBUILD_TESTS=OFF", "-DBUILD_DEBUGGER=OFF")
my_function("nana")
my_function("dyno")
my_function("glfw")
my_function("cpp_redis" , "-DBUILD_TESTS=OFF", "-DBUILD_TESTS=ON")
my_function("libev")
my_function("mongoose", "-DBUILD_EXAMPLES=OFF", "-DENABLE_SSL=OFF")
my_function("cxx_function")
'''
#my_function("cpr", "-DBUILD_CPR_TESTS=OFF")

#my_function("YourProjectStartHere")

my_function("kangaru", "-DKANGARU_BUILD_EXAMPLES=ON", "-DKANGARU_TEST=ON")

print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")
print("\n\nRepository is ready to use!\nRun CMake with argument  " + prefix_opt+ "\n")
print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")
print("##############################################################")
## TODO : CMAKE_TOOLCHAIN_FILE
## TODO: git clone --recurse-submodules -j8  
#toolset_opt="-TLLVM-vs2014"
#s_opt="-DCMAKE_CXX_COMPILER=clang++"
#toolset_opt="-Tv141_clang_c2"
#toolset_opt=""
#my_function("wt", "-DBUILD_EXAMPLES=OFF", "-DINSTALL_EXAMPLES=OFF", "-DINSTALL_DOCUMENTATION=OFF", "-DENABLE_LIBWTTEST=OFF")
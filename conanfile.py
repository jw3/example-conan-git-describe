from conans import ConanFile, tools
import os

build_dir = os.getenv("BUILD_DIR", "build")

def parse_version():
    conan_version = os.getenv("PLUGIN_VERSION", "snapshot")
    if os.path.exists(build_dir + "/VERSION"):
        conan_version = tools.load(build_dir + "/VERSION")
    return conan_version

class GitexampleConan(ConanFile):
    name = "git-example"
    version = parse_version()
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Gitexample here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]


conan and git describe
===

we like to use git describe to dynamically version both release and development builds.

how can this process be integrated with conan to dynamically specify the version, and perhaps even specify the channel (al la .isSnapshot)

### steps
- add conanfile; `conan new git-example/0.1`
- modify conanfile; ...
- run cmake which generates the version string
- export package; `conan export-pkg . foo/bar -f`

If the cmake build dir is not `build` then specify it with environment

`BUILD_DIR=cmake-build-debug conan export-pkg . ......`

Override the CMake derived settings with environment
- `CONAN_NAME` - package name
- `CONAN_VERSION` - package version

### references
- https://github.com/conan-io/conan/issues/548

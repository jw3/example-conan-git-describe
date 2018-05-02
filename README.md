conan and git describe
===

we like to use git describe to dynamically version both release and development builds.

how can this process be integrated with conan to dynamically specify the version, and perhaps even specify the channel (al la .isSnapshot)

### steps
- add conanfile; `conan new git-example/0.1`
- modify conanfile; ...

### references
- https://github.com/conan-io/conan/issues/548

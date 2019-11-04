name:     hugo
version:  0.47.1
release:  1
source:   https://github.com/gohugoio/%{name}/archive/v%{version}.tar.gz -> %{name}-%{version}.tar.gz

packager: Olivier Dᴏꜱꜱᴍᴀɴɴ <pkgxx@dossmann.net>
url:      http://gohugo.io/
summary:  The world’s fastest static site generator
dependencies: go, git

@configure
  export GOPATH="${HOME}/go"
  export PATH="${PATH}:${HOME}/go/bin"
  install -d "${GOPATH}/src/github.com/gohugoio"
  cp -a "$(pwd)" "${GOPATH}/src/github.com/gohugoio/hugo"
  cd "${GOPATH}/src/github.com/gohugoio/hugo"
  go get -u github.com/golang/dep/cmd/dep
  dep ensure
  go get github.com/magefile/mage

@build
  export GOPATH="${HOME}/go"
  export PATH="${PATH}:${HOME}/go/bin"
  cd "${GOPATH}/src/github.com/gohugoio/hugo"
  HUGO_BUILD_TAGS=extended mage install

@install
  export GOPATH="${HOME}/go"
  cd "${GOPATH}/src/github.com/gohugoio/hugo"
  install -Dm755 "${GOPATH}/bin/%{name}" "%{pkg}/usr/bin/%{name}"

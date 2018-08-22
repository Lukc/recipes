name:     hugo
version:  0.47.1
release:  1
source:   https://github.com/gohugoio/%{name}/archive/v%{version}.tar.gz

packager: Olivier Dᴏꜱꜱᴍᴀɴɴ <pkgxx@dossmann.net>
url:      http://gohugo.io/
summary:  The world’s fastest static site generator
dependencies: go, git

@build
  go get github.com/magefile/mage
  cd v%{version}
  mage vendor
  HUGO_BUILD_TAGS=extended mage install

@install
 cd v%{version}
 install -Dm755 "${name}" "${pkg}/usr/bin/%{name}"

name:     wgetpaste
version:  2.28
release:  1
source:   http://wgetpaste.zlin.dk/%{name}-%{version}.tar.bz2

packager: Olivier Dᴏꜱꜱᴍᴀɴɴ <pkgxx@dossmann.net>
url:      http://wgetpaste.zlin.dk/
summary:  Command that sends text to pastebin-like website
dependencies: bash, wget

@install

@build
	cd %{name}-%{version}
	install -d %{pkg}/usr/bin
	cat wgetpaste _wgetpaste > %{pkg}/usr/bin/wgetpaste
	chmod +x %{pkg}/usr/bin/wgetpaste

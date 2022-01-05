Name:     libxslt
Version:  1.1.34
Release:  6
Summary:  XSLT Transformation Library
License:  MIT
URL:      http://xmlsoft.org/libxslt/
Source0:  https://github.com/GNOME/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bug-fix https://github.com/GNOME/libxslt/
Patch0: CVE-2015-9019.patch
Patch1: Fix-variable-syntax-in-Python-configuration.patch
Patch2: Fix-clang-Wconditional-uninitialized-warning-in-libx.patch
Patch3: Fix-clang-Wimplicit-int-conversion-warning.patch
Patch4: Fix-implicit-int-conversion-warning-in-exslt-crypto..patch
Patch5: Fix-quadratic-runtime-with-text-and-xsl-message.patch
Patch6: Fix-double-free-with-stylesheets-containing-entity-n.patch

BuildRequires: gcc make libtool autoconf automake libgcrypt-devel pkgconfig(libxml-2.0) >= 2.6.27

%description
Libxslt is the XSLT C library developed for the GNOME project

%package  devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: libgcrypt-devel libgpg-error-devel

%description  devel
%{name} allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
chmod 644 python/tests/*
autoreconf -vfi
%configure --disable-static --disable-silent-rules --with-python 
%make_build

%install
%make_install
%delete_la
pushd $RPM_BUILD_ROOT/%{_includedir}/%{name}; touch -m --reference=xslt.h ../../bin/xslt-config;popd

%check
%make_build tests

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README FEATURES AUTHORS
%license Copyright
%{_bindir}/xsltproc
%{_libdir}/libxslt.so.*
%{_libdir}/libexslt.so.*
%{_libdir}/libxslt-plugins/
%{_mandir}/man1/xsltproc.1*

%files devel
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/xsltConf.sh
%{_datadir}/aclocal/libxslt.m4
%{_includedir}/libxslt/
%{_includedir}/libexslt/
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_bindir}/xslt-config

%files help
%doc %{_docdir}/%{name}-%{version}
%doc %{_mandir}/man3/*
%exclude %{_docdir}/%{name}/{ChangeLog,NEWS,README,FEATURES,AUTHORS}
%exclude %{_docdir}/../licenses/Copyright

%changelog
* Jan Wed 05 2022 fuanan <fuanan3@huawei.com> - 1.1.34-6
- Fix test command

* Sat Oct 23 2021 panxiaohe<panxiaohe@huawei.com> - 1.1.34-5
- Fix double-free with stylesheets containing entity nodes

* Thu Oct 29 2020 wangchen<wangchen137@huawei.com> - 1.1.34-4
- remove python2

* Wed Sep 23 2020 yangzhuangzhuang<yangzhuangzhuang1@huawei.com> - 1.1.34-3
- sync patches from LTS branch

* Wed Sep 23 2020 yangzhuangzhuang<yangzhuangzhuang1@huawei.com> - 1.1.34-2
- Fix the large loop found in xsltApplyStylesheetUser through fuzzing testcase xslt.

* Mon Jun 22 2020 linwei<linwei54@huawei.com> - 1.1.34-1
- update to 1.1.34

* Sat Jan 11 2020 zhangguangzhi<zhanguangzhi3@huawei.com> - 1.1.32-7
- del patch to be consistent with open source

* Tue Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-6
- fix bug in community files

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-5
- Fix CVE-2019-18197 and CVE-2019-13118

* Tue Sep 03 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-4 
- Package init

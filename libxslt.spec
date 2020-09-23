Name:     libxslt
Version:  1.1.34
Release:  3
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

%package -n python2-libxslt
%{?python_provide:%python_provide python2-libxslt}
Summary:        Development files for %{name}
BuildRequires:  python2-devel python2-libxml2
Requires:       %{name} = %{version}-%{release}
Requires:       python2-libxml2
Provides:       %{name}-python = %{version}-%{release}

%description  -n python2-libxslt
The python2-libxslt package contains the python2 bindings for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

%build
chmod 644 python/tests/*
autoreconf -vfi
export PYTHON=/usr/bin/python2
%configure --disable-static --disable-silent-rules --with-python 
%make_build

%install
%make_install
%delete_la
pushd $RPM_BUILD_ROOT/%{_includedir}/%{name}; touch -m --reference=xslt.h ../../bin/xslt-config;popd

%check
make check

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

%files -n python2-libxslt
%{_libdir}/python2.7/site-packages/libxslt.py*
%{_libdir}/python2.7/site-packages/libxsltmod.so
%{_docdir}/libxslt-python-1.1.34/*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%changelog
* Wed Sep 23 2020 yangzhuangzhuang<yangzhuangzhuang1@huawei.com> - 1.1.34-3
- Fix the large loop found in xsltApplyStylesheetUser through fuzzing testcase xslt.

* Tue Jun 23 2020 openEuler xuping<xuping21@huawei.com> - 1.1.34-2
- quality enhancement synchronization github patch

* Mon May 11 2020 openEuler Buildteam<buildteam@openeuler.org> - 1.1.34-1
- update to 1.1.34

* Sat Jan 11 2020 zhangguangzhi<zhanguangzhi3@huawei.com> - 1.1.32-7
- del patch to be consistent with open source

* Mon Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-6
- fix bug in community files

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-5
- Fix CVE-2019-18197 and CVE-2019-13118

* Tue Sep 03 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-4 
- Package init

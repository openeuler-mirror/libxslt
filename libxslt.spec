Name:     libxslt
Version:  1.1.32
Release:  6
Summary:  XSLT Transformation Library
License:  MIT
URL:      http://xmlsoft.org/libxslt/
Source0:  https://github.com/GNOME/%{name}/archive/v%{version}.tar.gz
# Fedora specific patches
Patch0:   multilib.patch
Patch1:   libxslt-1.1.26-utf8-docs.patch
# PATCH-FIX-UPSTREAM bug-fix https://github.com/GNOME/libxslt/
Patch6000:0009-Fix-handling-of-RVTs-returned-from-nested-EXSLT-func.patch
Patch6001:0012-Fix-EXSLT-functions-returning-RVTs-from-outer-scopes.patch
Patch6002:0014-Variables-need-extern-in-static-lib-on-Cygwin.patch
Patch6003:0018-Fix-misleading-indentation-in-security.c.patch
Patch6004:0025-Fix-memory-leak-in-EXSLT-functions-error-path.patch
Patch6005:0026-Initialize-ctxt-output-before-evaluating-global-vars.patch
Patch6006:0027-Backup-context-node-in-exsltFuncFunctionFunction.patch
Patch6007:0031-Always-set-context-node-before-calling-XPath-iterato.patch
Patch6008:0032-Fix-float-casts-in-exsltDateDuration.patch
# PATCH-CVE-UPSTREAM 
Patch6009:CVE-2015-9019.patch
Patch6010:CVE-2019-11068.patch
# PATCH-FIX-UPSTREAM bug-fix https://github.com/GNOME/libxslt/
Patch6011:0004-Fix-check-of-xsltTestCompMatch-return-value.patch
Patch6012:0012-Fix-integer-overflow-in-_exsltDateDayInWeek.patch
Patch6013:0014-Fix-uninitialized-read-of-xsl-number-token.patch
Patch6014:0015-Fix-numbering-in-non-Latin-scripts.patch
Patch6015:0019-Avoid-quadratic-behavior-in-xsltSaveResultTo.patch
Patch6016:0023-Fix-insertion-of-xsl-fallback-content.patch
Patch6017:0025-Fix-unsigned-integer-overflow-in-date.c.patch
Patch6018:CVE-2019-18197.patch
Patch6019:CVE-2019-13118.patch

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
%{_docdir}/libxslt-python-1.1.32/*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%changelog
* Mon Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-6
- fix bug in community files

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-5
- Fix CVE-2019-18197 and CVE-2019-13118

* Tue Sep 03 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.32-4 
- Package init

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JSON-Any
Version  : 1.39
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-Any-1.39.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-Any-1.39.tar.gz
Summary  : '(DEPRECATED) Wrapper Class for the various JSON classes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-JSON-Any-license = %{version}-%{release}
Requires: perl-JSON-Any-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Test::Without::Module)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution JSON-Any,
version 1.39:
(DEPRECATED) Wrapper Class for the various JSON classes

%package dev
Summary: dev components for the perl-JSON-Any package.
Group: Development
Provides: perl-JSON-Any-devel = %{version}-%{release}
Requires: perl-JSON-Any = %{version}-%{release}

%description dev
dev components for the perl-JSON-Any package.


%package license
Summary: license components for the perl-JSON-Any package.
Group: Default

%description license
license components for the perl-JSON-Any package.


%package perl
Summary: perl components for the perl-JSON-Any package.
Group: Default
Requires: perl-JSON-Any = %{version}-%{release}

%description perl
perl components for the perl-JSON-Any package.


%prep
%setup -q -n JSON-Any-1.39
cd %{_builddir}/JSON-Any-1.39

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-JSON-Any
cp %{_builddir}/JSON-Any-1.39/LICENSE %{buildroot}/usr/share/package-licenses/perl-JSON-Any/ed631350617669e849a7971ebfbeb02063011435
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JSON::Any.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-JSON-Any/ed631350617669e849a7971ebfbeb02063011435

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/JSON/Any.pm

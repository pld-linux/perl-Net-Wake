#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	Wake
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Wake perl module
Summary(pl.UTF-8):	Moduł perla Net::Wake
Name:		perl-Net-Wake
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c9514b5fb43a06b3343b5c0a498b624e
URL:		http://search.cpan.org/dist/Net-Wake/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Wake: this package sends wake-on-lan packets to turn on machines
that are wake-on-lan capable.

%description -l pl.UTF-8
Moduł Net::Wake wysyła pakiety wake-on-lan w celu włączenia maszyn
obsługujących tę funkcję.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/Wake.pm
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
Summary:	Net-Wake perl module
Summary(pl):	Modu³ perla Net-Wake
Name:		perl-Net-Wake
Version:	0.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Wake-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Wake This package sends wake-on-lan packets to turn on machines
that are wake-on-lan capable.

%prep
%setup -q -n Net-Wake-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.gz
%{perl_sitelib}/Net/Wake.pm
%{_mandir}/man3/*

%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Wake
Summary:	Net-Wake perl module
Summary(pl):	Modu³ perla Net-Wake
Name:		perl-Net-Wake
Version:	0.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Wake: this package sends wake-on-lan packets to turn on machines
that are wake-on-lan capable.

%description -l pl
Modu³ Net-Wake wysy³a pakiety wake-on-lan w celu w³±czenia maszyn
obs³uguj±cych tê funkcjê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Wake
Summary:	Net::Wake perl module
Summary(pl):	Modu� perla Net::Wake
Name:		perl-Net-Wake
Version:	0.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f6b9d89888153ef4f8c0e55456f6c80e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Wake: this package sends wake-on-lan packets to turn on machines
that are wake-on-lan capable.

%description -l pl
Modu� Net::Wake wysy�a pakiety wake-on-lan w celu w��czenia maszyn
obs�uguj�cych t� funkcj�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

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
